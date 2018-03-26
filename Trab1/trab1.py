from skimage import measure
import numpy as np
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.morphology import closing, square
from scipy import misc
from skimage import color, util
from skimage.measure import label, regionprops
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

def drawHistogram(img):
    #flatten the array to a vector
    a = np.asarray(img).reshape(-1)
    plt.hist(a, bins='auto')
    plt.xlabel('Area')
    plt.title('histograma de area dos objetos')
    plt.ylabel('Numero de Objetos')
    plt.show()


#Pede-se o input da imagem que sera avaliada
img_name = input('Digite o nome da imagem:')

# Utilizando misc e pyplot, a imagem eh aberta
img = misc.imread(img_name + '.png')
grey_img = color.rgb2grey(img)
img_flip = util.invert(grey_img)

#im = Image.fromarray(img)
#draw = ImageDraw.Draw(im)

label_img, num = label(img_flip, None, None, True, None)
regions = regionprops(label_img)

#for n, region in enumerate(regions):
#    x, y = region.local_centroid
#    draw.text((50*x, 50*y), "1", 1)

plt.imshow(im, cmap='gray')
plt.show()

# Display the image and plot all contours found
contours = measure.find_contours(grey_img, 0.8)
fig, ax = plt.subplots()
ax.imshow(grey_img, interpolation='nearest', cmap=plt.cm.gray)

#contorno - Item 1.2
for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()

smallArea = 0
mediumArea = 0
bigArea = 0
regArray = []

#Propriedades do Objeto - Item 1.3
for n, reg in enumerate(regions):
    regArray.append(reg.filled_area)
    if(reg.filled_area < 1500):
        smallArea = smallArea +1
    elif(reg.filled_area < 3000):
        mediumArea = mediumArea +1
    else:
        bigArea = bigArea + 1
    print('regiao: ', n, ' perimetro: ', int(reg.perimeter), ' area: ', reg.filled_area)

print('numero de regioes pequenas: ', smallArea)
print('numero de regioes medias: ', mediumArea)
print('numero de regioes grandes: ', bigArea)

drawHistogram(regArray)
