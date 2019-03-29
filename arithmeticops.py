import cv2 as cv2
import numpy as np

img1=cv2.imread('finalenigma.jpg')
img2=cv2.imread('sush.jpg')

x=cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

