#-*-coding: utf-8-*-
#Adaptive Thresholding
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('resimler/cameraman.tif',0)
img=cv2.medianBlur(img,5) #resime median uygular.

ret,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY) #resmi siyah beyaza cevirdik.
#kenar bulma filtresi
#cv2.ADAPTIVE_THRESH_MEAN_C filtrenin esik degeri resmin ortalamasıdır.
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
cv2.THRESH_BINARY,11,4) #ilk deger siyah degeri, ikinci deger beyaz degeri.
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C esik degeri komsuluk degerlerinin agırlıklı toplamıdır.
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv2.THRESH_BINARY,11,4) #deger1%deger2!=0 olmalıdır.

titles=['Original Image', 'Global Thresholding (v = 127)','Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']

images=[img,th1,th2,th3]

for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
