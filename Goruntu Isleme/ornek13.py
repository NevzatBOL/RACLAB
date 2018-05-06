#-*-coding: utf-8-*-
###Hareket Algılama2##

import numpy as np
import cv2

cam=cv2.VideoCapture('videolar/test.mp4')

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
	ret,frame=cam.read()
	if ret:
		fgmask=fgbg.apply(frame)
		cv2.imshow('frame',fgmask)

	if cv2.waitKey(30) & 0xFF == 27:
		break

cam.release()
cv2.destroyAllWindows()
