#-*-coding: cp1254-*-
###Araba Takip Etme###

import numpy as np
import cv2

cap = cv2.VideoCapture('videolar/slow.mp4')
ret,frame = cap.read()

# pencerenin başlangıç konumunu ayarladık.
r,h,c,w = 250,90,400,125
track_window = (c,r,w,h)

# takip edilecek alanı ayarladık.
roi = frame[r:r+h, c:c+w]
hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[10,180])
#[10,180] değerler değiştirilerek daha iyi sonuçlar elde edileblir.
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)


# sonlandırma ölçütleri ayarlandı. 1-10 iterasyon
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

while(1):
	ret ,frame = cap.read()
	if ret == True:
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
		# pencerenin yeni konumu alındı.
		ret, track_window = cv2.meanShift(dst, track_window, term_crit)
		# diktörgen içine aldırdık.
		x,y,w,h = track_window
		img = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
		cv2.imshow('Frame',img)

		k = cv2.waitKey(60) & 0xff
		if k == 27:
			break
	else:
		break

cv2.destroyAllWindows()
cap.release()
