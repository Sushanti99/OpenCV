import cv2
import numpy as np

image=cv2.imread('whereiswaldo.jpg')
cv2.imshow('Where is waldo?',image)
cv2.waitKey(0)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

template=cv2.imread('waldp.jpg',0)

result=cv2.matchTemplate(gray,template,cv2.TM_CCOEFF)
minval,maxval,minloc,maxloc=cv2.minMaxLoc(result)

topleft=maxloc
bottomright=(topleft[0]+50,topleft[1]+50)
cv2.rectangle(image,topleft,bottomright,(0,0,255),5)

cv2.imshow('Where is waldo?',image)
cv2.waitKey(0)

cv2.destroyAllWindows()