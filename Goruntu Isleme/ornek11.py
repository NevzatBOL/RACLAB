#-*-coding: cp1254-*-
###Sekil Algılama1###

import numpy as np
import cv2

img=cv2.imread('resimler/shapes_and_colors.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
#resmin arkası siyah şekiller beyaz olmalıdır.
#thresh=cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)[1]
thresh=cv2.threshold(blur,60,255,cv2.THRESH_BINARY)[1]

cv2.imshow("blur",blur)
cv2.imshow("thresh",thresh)

_,cntr,_=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for c in cntr:
	M=cv2.moments(c)
	cx=int(M['m10']/M['m00'])
	cy=int(M['m01']/M['m00'])

	cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
	cv2.circle(img,(cx,cy),7,(0,0,255),-1)
	cv2.putText(img,"center",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2)

	cv2.imshow("image",img)
	cv2.waitKey(0)
