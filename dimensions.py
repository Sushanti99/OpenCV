import numpy as np 
import cv2

img = cv2.imread('finalenigma.jpg',0)

font = cv2.FONT_HERSHEY_SIMPLEX 
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

