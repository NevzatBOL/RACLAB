#-*-coding: cp1254-*-
###Hareket Algılama2##

import numpy as np
import cv2

cam=cv2.VideoCapture('videolar/test.mp4')

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
	ret,frame=cam.read()
	if frame is not None:
		fgmask=fgbg.apply(frame)
		cv2.imshow('frame',fgmask)

		if cv2.waitKey(30) & 0xFF == 27:
			break
	else:
		break
cam.release()
cv2.destroyAllWindows()
