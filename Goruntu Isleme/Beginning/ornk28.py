#-*-coding: utf-8 -*-
#Sobel ve Laplacian Filtreleri
import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('resimler/sudoku.png',0)

#CV_ farklı laplacelar kullanıla bilir.
#for i in dir(cv2):
#    if i.startswith('CV'):
#        print i

laplacian=cv2.Laplacian(img,cv2.CV_64F) 
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=11) #ksize degerleri degistirilerek sonuc iyilestirile bilir.
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=11)

plt.subplot(2,2,1),plt.imshow(img,cmap='gray')
plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()
