#-*- coding: utf-8 -*-
#Basit Image Islemleri
import numpy as np
import cv2

img = cv2.imread('resimler/python.jpg')

px = img[150,150] #resmin x=150,y=150 pixcel degerlerini degiskene atar.
print px #girilen pixcel dederlerindeki rgb yi ekrana basar.

blue = img[150,150,0] #girilen x,y pixcelindeki 0(b),1(g),2(r) degiskene atar. 
print blue

img[150,150]=[255,255,255] #girilen pixcel deðerlerinin rgb degerleri degistirildi.
print img[150,150]

img.item(10,10,2) #grilen x,y pixcelindeki 0(b),1(g),2(r) nin degerini verir.
img.itemset((10,10,2),100) #girilen (x,y pixcelindeki 0(b),1(g),2(r)) degerini degistirir.

print "shape : ", img.shape #resmin pixcel degerlerini ve kaç boyutlu oldugunu verir.

print "size : ", img.size #toplam pixcel sayısını verir.

print "type : ", img.dtype #resmin türünü verir.
