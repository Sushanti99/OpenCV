import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('stones.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

'''corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

plt.imshow(img),plt.show()
'''

sift = cv2.SIFT()
kp = sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp)

cv2.imshow('stones.jpg',img)

img=cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('stones.jpg',img)
sift = cv2.SIFT()
kp, des = sift.detectAndCompute(gray,None)

cv2.imshow('stones.jpg',img)
k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()

