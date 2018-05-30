from skimage import io
import argparse
import numpy as np

#Leitura dos Argumentos Passados
parser = argparse.ArgumentParser()
parser.add_argument('important_names', metavar='N', type=str, nargs='+', help='texts')
args = parser.parse_args()

#Abertura de Imagem e Tomada de Decisao do Plano de Bit Escolhido
plano_bits = int(args.important_names[1])
img = io.imread(args.important_names[0])
x, y, rgb = img.shape

#Inicializacao de Variaveis
list = []
curr_bit_message = 6
intMsg = 0
ctrl = 0
img_0_r = np.zeros((x,y))
img_0_r = np.zeros((x,y))
img_0_r = np.zeros((x,y))
img_0_r = np.zeros((x,y))
img_0_r = np.zeros((x,y))
img_0_r = np.zeros((x,y))
img_0_r = np.zeros((x,y))
img_0_r = np.zeros((x,y))
img_0_r = np.zeros((x,y))
img_0_r = np.zeros((x,y))
img_0_r = np.zeros((x,y))
img_0_r = np.zeros((x,y))
text_saida = open(args.important_names[2], 'w')

#Loop Principal de Extracao de Imagem
for i in range(0, x):
    if ctrl == 1:
        break;
    for j in range(0, y):
        if ctrl == 1:
            break;
        for k in range(0, rgb):
            if curr_bit_message < 0 :
                curr_bit_message = 6
                list.append(chr(intMsg))
                if intMsg == 3:
                    ctrl = 1
                    break;
                intMsg = 0
            intMsg = intMsg + ((img[i,j,k]&(1 << plano_bits))>> plano_bits)*(2**curr_bit_message)
            curr_bit_message = curr_bit_message-1

#Atribuicao de Planos de bit para as imagens
img_0_r = (img[:,:,0]&1)*255
img_0_g = (img[:,:,1]&1)*255
img_0_b = (img[:,:,2]&1)*255
img_1_r = ((img[:,:,0]&2)>>1)*255
img_1_g = ((img[:,:,1]&2)>>1)*255
img_1_b = ((img[:,:,2]&2)>>1)*255
img_2_r = ((img[:,:,0]&4)>>2)*255
img_2_g = ((img[:,:,1]&4)>>2)*255
img_2_b = ((img[:,:,2]&4)>>2)*255
img_7_r = ((img[:,:,0]&64)>>6)*255
img_7_g = ((img[:,:,1]&64)>>6)*255
img_7_b = ((img[:,:,2]&64)>>6)*255

io.imsave('ImagemPlano0corR.png',img_0_r)

io.imsave('ImagemPlano0corg.png',img_0_g)

io.imsave('ImagemPlano0corb.png',img_0_b)

io.imsave('ImagemPlano1corR.png',img_1_r)

io.imsave('ImagemPlano1corG.png',img_1_g)

io.imsave('ImagemPlano1corB.png',img_1_g)

io.imsave('ImagemPlano2corR.png',img_2_r)

io.imsave('ImagemPlano2corG.png',img_2_g)

io.imsave('ImagemPlano2corB.png',img_2_b)

io.imsave('ImagemPlano7corR.png',img_7_r)

io.imsave('ImagemPlano7corG.png',img_7_g)

io.imsave('ImagemPlano7corB.png',img_7_b)

list.pop()
#Fechamento de Arquivo
text_saida.write(''.join(list))
text_saida.closed
