#-*- coding: utf-8 -*-
#Kameradan Görüntü Alma
import numpy as np
import cv2

cap=cv2.VideoCapture(0) #kamerayı etkinlestirdik.

while cap.isOpened(): #Kamera aktifse döngüye girer.
    ret, frame = cap.read() #kameradan gelen görüntüleri okduk.
    if ret :
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #aldıgımız görüntüleri griye çevirdik.
        cv2.imshow('frame',gray) #gri görüntüleri ekrana bastırdık.
        #cv2.imshow('frame',frame) #renkli görüntüyü ekrana bastırdık.
    if cv2.waitKey(1) & 0xFF == ord('q'): #klavyeden q harfine basıldığında döngüden çıktık.
        break

cap.release() #kamerayı kapattık.
cv2.destroyAllWindows() #tüm acık ekranları kapattık.
