import matplotlib.pyplot as plt
import numpy as np
from skimage import measure
from scipy import misc
from skimage import color, util
from skimage.measure import label, regionprops

#histograma - Item 1.4
def drawHistogram(img, img_name):
    a = np.asarray(img).reshape(-1)
    plt.hist(a, bins=[0,1500,3000,5000], rwidth=0.5)
    plt.savefig(img_name + 'histograma.png')
    plt.xlabel('Area')
    plt.title('histograma de area dos objetos')
    plt.ylabel('Numero de Objetos')
    plt.show()

#Pede-se o input da imagem que sera avaliada
img_name = input('Digite o nome da imagem:')
img = misc.imread(img_name + '.png')

#Transformacao de Cores - Item 1.1
grey_img = color.rgb2grey(img)
img_flip = util.invert(grey_img)
misc.imsave(img_name + 'Cinza.png', grey_img)
plt.imshow(grey_img, cmap='gray')
plt.show()

#------------------------------------------------------------------------------

#Contorno dos Objetos - Item 1.2
fig, ax = plt.subplots()
contours = measure.find_contours(grey_img, 0.8)
ax.imshow(grey_img, interpolation='nearest', cmap=plt.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
fig.savefig(img_name + 'Contorno.png')
#------------------------------------------------------------------------------

#Propriedades do Objeto - Item 1.3
label_img, num = label(img_flip, None, None, True, None)
regions = regionprops(label_img)
smallArea = 0
mediumArea = 0
bigArea = 0
regArray = []
print('Item 1.3 - Propriedades do Objeto')
for n, reg in enumerate(regions):
    regArray.append(reg.filled_area)
    if(reg.filled_area < 1500):
        smallArea = smallArea +1
    elif(reg.filled_area < 3000):
        mediumArea = mediumArea +1
    else:
        bigArea = bigArea + 1
    print('regiao: ', n, ' perimetro: ', int(reg.perimeter), ' area: ', reg.filled_area)

print()


fig2, ax2 = plt.subplots()
ax2.imshow(img_flip, cmap='gray')
for n, region in enumerate(regions):
    x, y = region.centroid
    ax2.text(y-10, x+10, str(n), style='italic')
plt.show()
fig2.savefig(img_name + 'Rotulado.png')

#------------------------------------------------------------------------------

# Histograma de  Area dos Objetos - 1.4 - Classificao dos Objetos
print('Item 1.4 - Classificao dos Objetos')
print('numero de regioes pequenas: ', smallArea)
print('numero de regioes medias: ', mediumArea)
print('numero de regioes grandes: ', bigArea)
drawHistogram(regArray, img_name)

#------------------------------------------------------------------------------
