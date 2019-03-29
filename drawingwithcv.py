import cv2 as cv2
import numpy as np

img=np.zeros((511,511,1),np.uint8)

cv2.line(img,(0,0),(511,511),(255,255,255),5)

cv2.rectangle(img,(384,0),(200,128),(255,255,0),5)

cv2.circle(img,(447,63), 45, (255,0,0), -1)

cv2.ellipse(img,(256,256),(100,100),180,55,270,180,-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32) 
pts = pts.reshape((-1,1,2)) 
cv2.polylines(img,[pts],True,(255,0,0))

font = cv2.FONT_HERSHEY_SIMPLEX 
img=cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.CV_AA)

cv2.imshow('img',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
