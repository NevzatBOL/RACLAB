#-*-coding: utf-8-*-
###Şerit Takibi - pointselect - src###

import numpy as np
import cv2
import matplotlib.pyplot as plt

cam=cv2.VideoCapture('videolar/serit1.mp4')

_,frame=cam.read()

src = np.float32([(130,530),
		  (885,530), 
		  (380,350),
		  (590,350)])

cv2.circle(frame,(src[0][0],src[0][1]), 10, (0,0,255), -1)
cv2.putText(frame,'first point',(src[0][0],src[0][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2,cv2.LINE_AA)

cv2.circle(frame,(src[1][0],src[1][1]), 10, (0,0,255), -1)
cv2.putText(frame,'second point',(src[1][0],src[1][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2,cv2.LINE_AA)

cv2.circle(frame,(src[2][0],src[2][1]), 10, (0,0,255), -1)
cv2.putText(frame,'third point',(src[2][0],src[2][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2,cv2.LINE_AA)

cv2.circle(frame,(src[3][0],src[3][1]), 10, (0,0,255), -1)
cv2.putText(frame,'fourth point',(src[3][0],src[3][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2,cv2.LINE_AA)
	 	
plt.imshow(frame)
plt.show()
