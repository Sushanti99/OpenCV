import cv2 as cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
	if event==cv2.EVENT_LBUTTONDBLCLK:
		cv2.line(img,(0,0),(511,511),(255,255,255),3)

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
	cv2.imshow('image',img)
	if cv2.waitKey(0):
		break

cv2.destroyAllWindows()
