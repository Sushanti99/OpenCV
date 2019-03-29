import cv2 as cv2
import numpy as np

img=cv2.imread('finalenigma.jpg',0)

print(img.shape)
print(img.size)
print(img.dtype)

img[:,:,2]=0

cv2.imshow('img',img)
