import cv2
import numpy as np

image=cv2.imread('face4.jpg')
cv2.imshow('original',image)
cv2.waitKey(0)

blank_image=np.zeros((image.shape[0],image.shape[1],3))

original_image=image

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edged=cv2.Canny(gray,50,200)
cv2.imshow('1-canny edges',edged)
cv2.waitKey(0)

contours,hierarchy=cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
print('Number ofcontoursfound=',len(contours))

cv2.drawContours(black_image,contours,-1,(0,255,0),3)
cv2.imshow('2-All contours over blank image',blank_image)
cv2.waitKey(0)

cv2.drawContours(image,contours,-1,(0,255,0),3)
cv2.imshow('3-All contours',image)
cv2.waitKey(0)

cv2.destroyAllWindows()
