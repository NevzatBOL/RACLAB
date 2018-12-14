#-*-coding: utf-8 -*-
#copyMakeBorder
import numpy as np
import cv2
from matplotlib import pyplot as plt

blue=[0,0,255]

img=cv2.imread('resimler/opencv.png')

#cv2.copyMakeBorder(img,x,y,skalaX,skalaY,event)
replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE) #Son ögeyi cogaltır. (aaaaaa | abcdefgh | hhhhhhh)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT) #resmi aynalar. (fedcba|abcdefgh|hgfedcb)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101) #resmi aynalar. (gfedcb|abcdefgh|gfedcba)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP) #(cdefgh | abcdefgh | abcdefg)
constant = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT, value=blue) #resmin etrafına kenarlık ekler.

plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT101')
plt.subplot(234),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(235),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()
