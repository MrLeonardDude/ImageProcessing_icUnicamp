from skimage import measure
import numpy as np
from scipy import misc
from skimage import color
import matplotlib.pyplot as plt

#Pede-se o input da imagem que sera avaliada
img_name = input('Digite o nome da imagem:')

# Utilizando misc e pyplot, a imagem eh aberta
img = misc.imread(img_name + '.png')
grey_img = color.rgb2grey(img)

contours = measure.find_contours(grey_img, 0.8)

# Display the image and plot all contours found
fig, ax = plt.subplots()
ax.imshow(grey_img, interpolation='nearest', cmap=plt.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
