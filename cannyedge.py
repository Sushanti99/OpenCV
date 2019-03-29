import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('finalenigma.jpg')
edges=cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('edges'),plt.xticks([]),plt.yticks([])

plt.show()
