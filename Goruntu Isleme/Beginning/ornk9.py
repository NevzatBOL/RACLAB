#-*-coding: utf-8 -*-
#Trackbar ve Renk Paleti
import numpy as np
import cv2

def nothing(x):
    pass

img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

#RGB degerlerini alacagımız Tracbarları olusturduk.
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

switch = 'OFF - ON    '
cv2.createTrackbar(switch, 'image',0,1,nothing) #0-1 arası switch olusturduk.

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF ==27:
        break

    #Tackbarın pozisyon degerlerini degiskenlere attık.
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    s=cv2.getTrackbarPos(switch,'image')

    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r] #rgb degerlerine göre renk olusturduk.

cv2.destroyAllWindows()
