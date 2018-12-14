#-*-coding: utf-8 -*-
#Canny Edge Detection
import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('resimler/cameraman.tif',0)
edges=cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('Edge'),plt.xticks([]),plt.yticks([])
plt.show()
