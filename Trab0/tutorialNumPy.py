from scipy import misc
from scipy import ndimage
from skimage import exposure
import numpy as np
import matplotlib.pyplot as plt

img_name = raw_input('Digite o nome da imagem:')

# open image file and stores it in a numpy array
img = misc.imread(img_name)
plt.imshow(img, cmap='gray')
plt.show()

#function 1
def drawHistogram(img):
    #flatten the array to a vector
    a = np.asarray(img).reshape(-1)
    plt.hist(a, bins='auto')
    plt.xlabel('Shades of Grey')
    plt.title('Histograma de Imagens')
    plt.ylabel('Frequency')
    plt.show()
drawHistogram(img)

#function 2
def getParameters(img):
    x, y = img.shape
    mini, medi, maxim = img.min(), img.mean(), img.max()
    print 'largura:', x
    print 'altura:', y
    print 'Intensidade minima:', mini
    print 'Intensidade media:', medi
    print 'Intensidade maxima:', maxim
getParameters(img)

#function 3
def changeBrightness(img):
    aux_img = 255 - img
    #print 'img original', img
    #print 'img ferrada', aux_img
    plt.imshow(aux_img, cmap='gray')
    plt.show()
changeBrightness(img)

def changeBrightnessSpecific(img):
    #aux_img = 120 + img*36/51
    #aux_img = aux_img.astype(int)
    #print ('img original', img)
    #print ('img ferrada', aux_img)
    skimage.exposure.rescale_intensity(img, in_range=(0, 255),out_range=(120, 180))
    plt.imshow(img, cmap='gray')
    plt.show()

changeBrightnessSpecific(img)

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
