#-*-coding: utf-8 -*-
#Morphological Transformations
import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('resimler/j.png',0)

kernel = np.ones((5,5),np.uint8)

#getStructuringElement fonksiyonu kullanılarakta kernel filteri olusturulabilir.
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

kernel = np.ones((9,9),np.uint8)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

plt.subplot(3,3,1),plt.imshow(img,cmap='gray')
plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(3,3,2),plt.imshow(erosion,cmap = 'gray')
plt.title('Erosion'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,3),plt.imshow(dilation,cmap = 'gray')
plt.title('Dilation'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,4),plt.imshow(opening,cmap = 'gray')
plt.title('Opening'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,5),plt.imshow(closing,cmap = 'gray')
plt.title('Closing'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,6),plt.imshow(gradient,cmap = 'gray')
plt.title('Gradient'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,7),plt.imshow(tophat,cmap = 'gray')
plt.title('Tophat'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,8),plt.imshow(blackhat,cmap = 'gray')
plt.title('Blackhat'), plt.xticks([]), plt.yticks([])
plt.show()
