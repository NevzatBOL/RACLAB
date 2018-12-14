#-*-coding: utf-8-*-
#Imagelerde Aritmatik Islemler - Bitsel Islemler
import numpy as np
import cv2

img1=cv2.imread('resimler/futbol.jpg')
img2=cv2.imread('resimler/opencv.png')

rows,cols,channels=img2.shape
roi=img1[0:rows, 0:cols]

img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) #resimi griye çevirir.
# resmi girilen degerler aralıgında filitre uygular.
ret, mask=cv2.threshold(img2gray, 10,255, cv2.THRESH_BINARY) #0-10->0 ve 10-255->1 yapar. 0(siyah) 1(beyaz)
mask_inv=cv2.bitwise_not(mask) #maskelenen resmi invertler.

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv) #mask_inv üzerine roi ekler.
img2_fg=cv2.bitwise_and(roi,img2,mask=mask) #mask üzerine img2 ve roi ekler.

dst=cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols]=dst

cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
