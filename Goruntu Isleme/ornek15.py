#-*-coding: cp1254-*-
###Yüz ve Göz Algılama###

import numpy as np
import cv2
import matplotlib.pyplot as plt

face=cv2.CascadeClassifier('DataSet/haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier('DataSet/haarcascade_eye.xml')

cam = cv2.VideoCapture(0)
i=0

while(1):
	ret, frame = cam.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces=face.detectMultiScale(gray, 1.3, 5)
     	
	'''
	if faces != ():
		i+=1
		name="face"+str(i)+".jpg"
		cv2.imwrite(name,frame)	'''

	for(x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray=gray[y:y+h,x:x+w]
		roi_color=frame[y:y+h,x:x+w]
		eyes=eye.detectMultiScale(roi_gray)
		for(ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xff == 27:
		break
cam.release()
cv2.destroyAllWindows()
