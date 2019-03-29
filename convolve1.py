Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> import cv2 as cv2
import numpy as np
from scipy import ndimage
kernel_3x3= np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
kernel_5x5= np.array([[-1,-1,-1,-1,-1],[-1,1,2,1,-1],[-1,2,4,2,-1],[-1,1,2,1,-1],[-1,-1,-1,-1,-1]])
img=cv2.imread("finalenigma.jpg",0)
k3=ndimage.convolve(img,kernel_3x3)
k5=ndimage.convolve(img,kernel_5x5)
blurred=cv2.GaussianBlue(img,(11,11),0)
edger=cv2.Canny(img,100,200)
cv2.imshow('lol',egder)

>>> 
