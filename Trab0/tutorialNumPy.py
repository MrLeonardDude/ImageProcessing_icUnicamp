from scipy import misc
from scipy import ndimage
from skimage import exposure as exp
import numpy as np
import matplotlib.pyplot as plt

#Pede-se o input da imagem que sera avaliada
img_name = input('Digite o nome da imagem:')

# Utilizando misc e pyplot, a imagem eh aberta
img = misc.imread(img_name + '.png')
plt.imshow(img, cmap='gray')
plt.show()

#Funcao responsavel pelo desenho do Histograma de Imagem
def drawHistogram(img):
    #flatten the array to a vector
    a = np.asarray(img).reshape(-1)
    plt.hist(a, bins='auto')
    plt.xlabel('Shades of Grey')
    plt.title('Histograma de Imagens')
    plt.ylabel('Frequency')
    plt.show()
drawHistogram(img)

#Funcao responsavel pela impressao das Estatisticas da Imagem
def getParameters(img):
    x, y = img.shape
    mini, medi, maxim = img.min(), img.mean(), img.max()
    print 'largura:', x
    print 'altura:', y
    print 'Intensidade minima:', mini
    print 'Intensidade media:', medi
    print 'Intensidade maxima:', maxim
getParameters(img)

#Funcao responsavel pela transformacao negativa da imagem
def changeBrightnessNegative(img):
    aux_img = 255 - img
    plt.imshow(aux_img, cmap='gray')
    plt.show()
changeBrightnessNegative(img)

#Funcao responsavel pela transformacao de intervalo da imagem
def changeBrightnessSpecific(img):
    le_img = img
    le_img = exp.rescale_intensity(le_img, in_range=(0,255), out_range = (120,180))
    plt.imshow(le_img, cmap='gray')
    plt.show()
changeBrightnessSpecific(img)
