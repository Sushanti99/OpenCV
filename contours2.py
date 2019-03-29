import cv2
import numpy as np

img=cv2.imread('finalenigma.jpg')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(img,127,255,0)
thresh=cv2.bitwise_not(thresh)
edges=cv2.Canny(thresh,10,200)

contours,hierarchy=cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt=contours[0]
#M=cv2.moments(cnt)
#area=cv2.contourArea(cnt)
#perimeter=cv2.arcLength(cnt,True)

#print(area)
#print(M)

#cx=int(M['m10']/M['m00'])
#cy=int(M['m01']/M['m00'])

#print(cx)
#print(cy)

epsilon=0.3*cv2.arcLength(cnt,True)
approx=cv2.approxPolyDP(cnt,epsilon,True)
cv2.drawContours(img,contours,-1,(0,255,0),3)

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
