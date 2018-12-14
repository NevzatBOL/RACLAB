#-*- coding: utf-8 -*-
#Matplotlib İle Resmi Görüntüleme
import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('resimler/python.jpg',0) #resim okunur.
plt.imshow(img, cmap='gray', interpolation ='bicubic') #resim gray formatında tanımlandı.
plt.xticks([]), plt.yticks([])
plt.show() #resim pyplot ile gösterilir
