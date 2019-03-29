import cv2 as cv2
import numpy as np

img1=cv2.imread('finalenigma.jpg')
img2=cv2.imread('sush.jpg')

res1=cv2.resize(img1,None,fx=1,fy=1,interpolation=cv2.INTER_AREA) 
res2=cv2.resize(img2,None,fx=1,fy=1,interpolation=cv2.INTER_AREA)

#x=cv2.addWeighted(res1,0.7,res2,0.3,0)

cv2.imshow('dst',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()

