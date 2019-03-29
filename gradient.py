import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('finalenigma.jpg',0)

laplacian=cv2.Laplacian(img,cv2.CV_64F)
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap='gray',1)
plt.title('original'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,1),plt.imshow(laplacian,cmap='gray',2)
plt.title('Laplacian'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,1),plt.imshow(sobelx,cmap='gray',3)
plt.title('Sobel X'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,1),plt.imshow(sobely,cmap='gray',4)
plt.title('Sobel Y'),plt.xticks([]),plt.yticks([])

plt.show()
