#-*- coding: utf-8 -*-
#Cizim Fonksiyonları
import numpy as np
import cv2

#siyah bir arka plan oluşturalım.
img = np.zeros((512,512,3), np.uint8)


cv2.line(img,(0,0),(511,511),(255,0,0),5) #Cizgi cizer

cv2.rectangle(img,(384,0),(510,128),(0,255,0),3) #Dikdortgen cizer

cv2.circle(img,(447,63), 63, (0,0,255), -1) #Daire cizer

cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1) #Elips cizer

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

#Yazı yazmak icin
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.CV_AA) #cv2.CV_AA to cv2.LINE_AA

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
