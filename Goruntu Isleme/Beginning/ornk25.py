#-*-coding: utf-8 -*-
#Image Filtresi - 2D Convolution
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('resimler/opencv.png')

#5*5 lik birim matris ile resim çarpılarak determinantı alınıyor.
#sonuç 25 e bölünerek her 5*5 lik pixel e çıkan deger yazılır.
kernel=np.ones((5,5),np.float32)/25 
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Orginal')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]),plt.yticks([])
plt.show()
