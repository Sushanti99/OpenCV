import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('finalenigma.jpg',0)

blur=cv2.blur(img,(5,5))

cv2.imshow('original',img)
cv2.imshow('Blurred',blur)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.import all function 
