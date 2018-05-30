import argparse
from skimage import io
from skimage import color
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('important_names', metavar='N', type=str, nargs='+', help='texts')
args = parser.parse_args()

img = io.imread(args.important_names[0])
gray_img = color.rgb2gray(img)
x, y = gray_img.shape

gray_img = 1 - gray_img

perfil = np.zeros(x)

io.imshow(gray_img, cmap='gray')
io.show()

'''
for i in range(0, x):
    for j in range(0, y):
        perfil[i] = perfil[i] + gray_img[i,j]

print (perfil)
'''
