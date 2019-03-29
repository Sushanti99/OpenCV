import cv2 as cv2
import numpy as np

img=cv2.imread('finalenigma.jpg')

print(img.shape)

ball=img[900:922,800:883]

img[100:122,200:283]=ball

cv2.imshow('img',img)

k=cv2.waitKey(0)

cv2.destroyAllWindows
