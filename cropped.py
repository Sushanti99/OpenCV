import cv2
import numpy as numpy
image=cv2.imread('apple.jpg')
height,width=image.shape[:2]

start_row,start_col=int(height*.25),int(width*.25)

end_row,end_col=int(height*.25),int(width*.25)

cropped=image[start_row:end_row,start_col:end_col]

cv2.imshow('Original image',image)
cv2.waitKey(0)
cv2.imshow('Cropped image',cropped)
cv2.waitKey(0)

cv2.destroyAllWindows()