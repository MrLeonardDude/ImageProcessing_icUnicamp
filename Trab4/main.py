'''
Padroes Utilizados para o programa:
    interpolacao tipo 1 = Ponto Mais Proximo
    interpolacao tipo 2 = Bilinear
    interpolacao tipo 3 = Bicubica
    interpolacao tipo 4 = Lagrange

    Observacao para a implementacao da rotacao:
    Para se evitar o problema de bordas, o responsavel pelo projeto utilizou
    de uma expansao da imagem original para garantir que a imagem toda seria
    rotacionada
Exemplos:
    (- cury/16 + ory/2) -> y
    (- curx/2 + orx/2) -> x
'''
import argparse
from skimage import io
from skimage import img_as_float
from skimage import color
import numpy as np
from math import cos
from math import sin
from math import floor
from math import ceil
from math import radians
from math import pow


def interpol_PMP(orx, ory, curx, cury, escale, angle, x_, y_, input_):
    if(escale > 0):
        x = int(x_ / escale)
        y = int(y_ / escale)
    else:
        x = int(((x_ - curx/2) * cos(-angle) - (y_ - cury/2) * sin(-angle)))
        y = int(((x_ - curx/2) * sin(-angle) + (y_ - cury/2) * cos(-angle)))
    output = 0
    if 0 < x < orx:
        if 0 < y < ory:
            output = (input_[x, y])
    return output


def interpol_bili(orx, ory, curx, cury, escale, angle, x_, y_, input_):
    if(escale > 0):
        x = x_ / escale
        y = y_ / escale
    else:
        x = ((x_ - curx/2) * cos(-angle) - (y_ - cury/2) * sin(-angle))
        y = ((x_ - curx/2) * sin(-angle) + (y_ - cury/2) * cos(-angle))
    output = 0
    if 0 < x + 1 < orx:
        if 0 < y + 1 < ory:
            viz_1_x = int(floor(x))
            viz_1_y = int(floor(y))
            viz_2_x = int(ceil(x))
            viz_3_y = int(ceil(y))
            dx = x - viz_1_x
            dy = y - viz_1_y
            output = (1 - dx)*(1 - dy)*input_[viz_1_x, viz_1_y]
            output = output + dx*(1-dy)*input_[viz_2_x, viz_1_y]
            output = output + (1-dx)*(dy)*input_[viz_1_x, viz_3_y]
            output = output + dx*dy*input_[viz_2_x, viz_3_y]
    return output


def aux_cubi_P(t):
    if t > 0:
        return t
    return 0


def aux_cubi_R(s):
    r = pow(aux_cubi_P(s+2), 3)
    r = r - 4*pow(aux_cubi_P(s+1), 3)
    r = r + 6*pow(aux_cubi_P(s), 3)
    r = r - 4*pow(aux_cubi_P(s-1), 3)
    r = r / 6
    return r


def interpol_cubi(orx, ory, curx, cury, escale, angle, x_, y_, input_):
    if(escale > 0):
        x = x_ / escale
        y = y_ / escale
    else:
        x = (x_ - curx/2) * cos(-angle) - (y_ - cury/2) * sin(-angle)
        y = (x_ - curx/2) * sin(-angle) + (y_ - cury/2) * cos(-angle)
    output = 0
    if 1 < x - 1 < orx - 3:
        if 1 < y - 1 < ory - 3:
            viz_1_x = (floor(x))
            viz_1_y = (floor(y))
            dx = x - viz_1_x
            dy = y - viz_1_y
            for m in range(-1, 3):
                for n in range(-1, 3):
                    output = output + aux_cubi_R(m - dx) * aux_cubi_R(dy - n) * input_[int(x) +m, int(y) +n]
    return output


def aux_lag_L(x, y, dx, n, input_):
    L = 0
    L = L + (-dx) * (dx - 1) * (dx-2) * input_[int(x) - 1, int(y) + n - 2]/6
    L = L + (dx+1)*(dx-1)*(dx-2)*input_[int(x), int(y)+n-2]/2
    L = L + (-dx)*(dx+1)*(dx-2)*input_[int(x)+1, int(y)+n-2]/2
    L = L + dx*(dx+1)*(dx-1)*input_[int(x)+2, int(y)+n-2]/6
    return L


def interpol_lag(orx, ory, curx, cury, escale, angle, x_, y_, input_):
    if(escale > 0):
        x = x_ / escale
        y = y_ / escale
    else:
        x = (x_ - curx/2) * cos(-angle) - (y_ - cury/2) * sin(-angle)
        y = (x_ - curx/2) * sin(-angle) + (x_ - curx/2) * cos(-angle)
    output = 0
    if 1 < x - 1 < orx - 4:
        if 1 < y - 1 < ory - 4:
            viz_1_x = (floor(x))
            viz_1_y = (floor(y))
            dx = x - viz_1_x
            dy = y - viz_1_y
            output = output + (-dy)*(dy-1)*(dy-2)*aux_lag_L(x, y, dx, 1, input_)/6
            output = output + (dy+1)*(dy-1)*(dy-2)*aux_lag_L(x, y, dx, 2, input_)/2
            output = output + (-dy)*(dy+1)*(dy-2)*aux_lag_L(x, y, dx, 3, input_)/2
            output = output + (dy)*(dy+1)*(dy-1)*aux_lag_L(x, y, dx, 4, input_)/6
    return output


def interpol_escale(orx, ory, x, y, output, input, escale, interpol_type):
    for i in range(0, x):
        for j in range(0, y):
            if(interpol_type == 0):
                output[i, j] = interpol_PMP(orx, ory, x, y, escale, 0, i, j, input)
            elif(interpol_type == 1):
                output[i, j] = interpol_bili(orx, ory, x, y, escale, 0, i, j, input)
            elif(interpol_type == 2):
                output[i, j] = interpol_cubi(orx, ory, x, y, escale, 0, i, j, input)
            elif(interpol_type == 3):
                output[i, j] = interpol_lag(orx, ory, x, y, escale, 0, i, j, input)
            else:
                exit
    return output


def interpol_rotate(orx, ory, x, y, output, input, angle, interpol_type):
    for i in range(0, x):
        for j in range(0, y):
            if(interpol_type == 0):
                output[i, j] = interpol_PMP(orx, ory, x, y, 0, angle, i, j, input)
            elif(interpol_type == 1):
                output[i, j] = interpol_bili(orx, ory, x, y, 0, angle, i, j, input)
            elif(interpol_type == 2):
                output[i, j] = interpol_cubi(orx, ory, x, y, 0, angle, i, j, input)
            elif(interpol_type == 3):
                output[i, j] = interpol_lag(orx, ory, x, y, 0, angle, i, j, input)
            else:
                exit
    return output


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--ang')
parser.add_argument('-e', '--fa')
parser.add_argument('-d', '--width', nargs=2)
parser.add_argument('-m', '--interp')
parser.add_argument('-i', '--img')
parser.add_argument('-o', '--output')

args = parser.parse_args()
img = io.imread(args.img + '.png')
img_gray = color.rgb2gray(img)
float_img = img_as_float(img_gray)
x_img, y_img = float_img.shape

if(args.fa > 0):
    x_amp = int(args.width[0])
    y_amp = int(args.width[1])
    img_amp = np.zeros((x_amp, y_amp))
    img_amp = interpol_escale(x_img, y_img, x_amp, y_amp, img_amp, img_gray, int(args.fa), int(args.interp))
    io.imsave(args.img + '_amp.png', img_amp)

elif(args.ang != 0):
    if (int(args.width[0]) > x_img):
        x_amp = int(args.width[0])
    else:
        exit
    if (int(args.width[1] > y_img)):
        y_amp = int(args.width[1])
    else:
        exit
    img_amp = np.zeros((x_amp, y_amp))
    img_amp = interpol_rotate(x_img, y_img, x_amp, y_amp, img_amp, img_gray, radians(float(args.ang)), int(args.interp))
    io.imsave(args.img + '_rot.png', img_amp)

else:
    exit

io.imshow(img_amp, cmap='gray')
io.show()
