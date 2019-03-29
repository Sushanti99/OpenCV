import numpy as np 
import cv2
cap = cv2.VideoCapture(0)
while(True): 
	frame = cap.read()[1]
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	cv2.imshow('frame',gray)
	k=cv2.waitKey(10)
	if k==27:
		break

cv2.destroyAllWindows()
