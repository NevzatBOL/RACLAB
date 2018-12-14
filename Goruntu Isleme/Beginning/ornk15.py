#-*-coding: utf-8-*-
#Renk Filtreleme
import numpy as np
import cv2

#flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print flags

#renklerin filitre degerlerinin bulunması:
#blue = np.uint8([[[255,0,0 ]]])
#hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
#print hsv_blue
#[[[120 255 255]]]
#
#green = np.uint8([[[0,255,0 ]]])
#hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
#print hsv_green
#[[[ 60 255 255]]]
#
#red = np.uint8([[[0,0,255]]])
#hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
#print hsv_red
#[[[  0 255 255]]]
#
#lower = [H-10, 100,100]
#upper = [H+10, 255, 255]

cap=cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()
    if ret :
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        lower_blue=np.array([110,50,50]) #filitre matrisi olusturuldu
        upper_blue=np.array([130,255,255])

        mask=cv2.inRange(hsv, lower_blue, upper_blue) #filitre olusturuldu.
        res=cv2.bitwise_and(frame,frame,mask=mask) #resme filitre uygulandı.

        cv2.imshow('hsv',hsv)
        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)

    if cv2.waitKey(5) & 0xFF ==27:
        break

cap.release()
cv2.destroyAllWindows()

