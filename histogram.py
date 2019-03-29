import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('sush.jpg')

#plt.imshow([img],'gray')
#cv2.imshow('img',img)
#hist=cv2.calcHist([img],[0],None,[256],[0,256])
#plt.hist(img.ravel(),256,[0,256]);
#plt.show()

color=('b','g','r')
for i,col in enumerate(color):
	histr=cv2.calcHist([img],[i],None,[256],[0,256])
	plt.plot(histr,color=col)
	plt.xlim([0,256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
