import cv2
import numpy as np
 
'''img = cv2.imread('scenery1.jpg',cv2.IMREAD_GRAYSCALE)
rows,cols = img.shape
 
denoised = cv2.GaussianBlur(img,(7,7),0)
filter = cv2.Laplacian(denoised,cv2.CV_64F)
 
cv2.imshow('Original',img)
cv2.imshow('Laplacian Filter',filter)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

img = cv2.imread('stones.jpg',cv2.IMREAD_GRAYSCALE)
 
'''filter = cv2.Canny(img,100,200)
 
cv2.imshow('Original',img)
cv2.imshow('Laplacian Filter',filter)'''
 

contour = (np.array([[[5,0]], [[2,2]], [[2,2]], [[0,5]]]),img)
contour, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.contourArea(contour[0])

cv2.imshow('stones.jpg',img)
cv2.waitKey(0)

