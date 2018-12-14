#-*- coding: utf-8 -*-
#Fare Eventleri ve Cizim
import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i] #cv2 eventlerini listeler.
print events

#ekrana tıklandıgında daire atan uygulama:
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK: #farenin sol tusuna çift tıklandıgında
        cv2.circle(img,(x,y),10,(255,0,0),-1) #circle(img,(x,y),çap,(B,G,R),-1) daire olusturur.
    elif event == cv2.EVENT_RBUTTONDBLCLK: #farenin sag tusuna çift tıklandıgında
        cv2.circle(img,(x,y),10, (0,255,0),-1)
    elif event == cv2.EVENT_FLAG_LBUTTON: #farenin sol tusuna tıklandıgında
        cv2.circle(img,(x,y),10, (0,0,255),-1)
    #elif event == cv2.EVENT_LBUTTONUP: #farenin sol tusunu bıraktıgında
        #cv2.circle(img,(x,y),10, (0,255,255),-1)
img = np.zeros((512,512,3), np.uint8) #(np.zeros((x,y (ekran boyutu),(1(beyaz) or (3(mavi)))))
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()
