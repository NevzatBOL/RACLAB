import cv2
import numpy as np

red_lower = np.array([0, 100, 100],np.uint8)
red_upper = np.array([10, 255, 255],np.uint8)


cam = cv2.VideoCapture(1)

while(cam.isOpened()):
	_,frame = cam.read()

	w,h,_=frame.shape
	
	left_camera=frame[:,:h/2]
	right_camera=frame[:,h/2:]

	blur=cv2.GaussianBlur(left_camera,(5,5),0)
	hsv=cv2.cvtColor(left_camera,cv2.COLOR_BGR2HSV)

	red=cv2.inRange(hsv, red_lower, red_upper)
	red=cv2.erode(red,None,iterations=2)
	red=cv2.dilate(red,None,iterations=2)


	_,cntr,_=cv2.findContours(red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	for i,c in enumerate(cntr):
		if cv2.contourArea(c)<1000:
			continue
		x,y,w,h=cv2.boundingRect(c)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),0)
		cv2.putText(frame,"Kirmizi",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))

    	cv2.imshow('frame',left_camera)
	if cv2.waitKey(1) & 0xFF ==27:
		break

cam.release()
cv2.destroyAllWindows()       
		

