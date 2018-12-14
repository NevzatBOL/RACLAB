#-*-coding: utf-8 -*-
#Image Filtreleri
import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('resimler/opencv.png')

#5*5lik pixcellerin ortalamasını alır ve tüm pixcellere yazar.
blur=cv2.blur(img,(5,5)) 
gaus=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img,5) #girilen pixcel degerinin ortanca degerini hesaplar
bilateral=cv2.bilateralFilter(img,9,75,75)

plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(232),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]),plt.yticks([])
plt.subplot(233),plt.imshow(gaus),plt.title('Gaussian')
plt.xticks([]),plt.yticks([])
plt.subplot(234),plt.imshow(median),plt.title('Median')
plt.xticks([]),plt.yticks([])
plt.subplot(235),plt.imshow(bilateral),plt.title('Bilateral')
plt.xticks([]),plt.yticks([])
plt.show()
