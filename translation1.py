import cv2
import numpy as np

img = cv2.imread('finalenigma.jpg',1)

res = cv2.resize(img,None,fx=1, fy=1, interpolation = cv2.INTER_AREA)

cv2.imshow('img',img)
cv2.imshow('res',res)

k=cv2.waitKey(507854)
if k==27:
	cv2.destroyAllWindows()
