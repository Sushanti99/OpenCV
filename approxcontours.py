import cv2
import numpy as np

image=cv2.imread('sush.jpg')
orig_image=image.copy()

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

contours,hierarchy=cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

for c in contours:
	x,y,w,h=cv2.boundingRect(c)
	cv2.rectangle(orig_image,(x,y),(x+w,y+h),(0,0,255),2)
	cv2.imshow('Bounding Rect',orig_image)

cv2.waitKey(0)

for c in contours:
	accuracy=0.001*cv2.arcLength(c,True)
	approx=cv2.approxPolyDP(c,accuracy,True)
	cv2.drawContours(image,[approx],0,(0,255,0),2)
	cv2.imshow('Approx Poly DP',image)

cv2.waitKey(0)
cv2.destroyAllWindows()
