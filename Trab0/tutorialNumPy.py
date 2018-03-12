

from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

# open image file and stores it in a numpy array
img = misc.imread('baboon.png')
plt.imshow(img, cmap='gray')
plt.show()


def drawHistogram(img):
    #flatten the array to a vector
    a = np.asarray(img).reshape(-1)
    plt.hist(a, bins='auto')
    plt.xlabel('Shades of Grey')
    plt.title('Histograma de Imagens')
    plt.ylabel('Frequency')
    plt.show()

drawHistogram(img)

def getParameters(img):
    x, y = img.shape
    mini, medi, maxim = img.min(), img.mean(), img.max()
    print ('largura:', x)
    print ('altura:', y)
    print ('Intensidade minima:', mini)
    print ('Intensidade media:', medi)
    print ('Intensidade maxima:', maxim)

getParameters(img)

def changeBrightness(img):
    aux_img = 255 - img
    #print 'img original', img
    #print 'img ferrada', aux_img
    plt.imshow(aux_img, cmap='gray')
    plt.show()

changeBrightness(img)

# print image dimensions and type
#   print img.shape, img.dtype

# show image
#   plt.imshow(img, cmap='gray')
#   plt.show()

# save image in PNG format
#   misc.imsave('baboon2.png', img)

# calculate some statistical information
#   print  'img min     img mean        img max'
#   print  img.min(), img.mean(), img.max()

# apply rotation transformation
#   f = np.flipud(img)
#   plt.imshow(f)
#   plt.show()

# smooth image with Gaussian filter
#   g = ndimage.gaussian_filter(img, sigma=7)
#   h = ndimage.gaussian_filter(img, sigma=11)
#   plt.imshow(g)
#   plt.show()
#   plt.imshow(h)
#   plt.show()
