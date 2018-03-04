#-*-coding: cp1254-*-
###Resim Üzerinde Başka Bir Parça Arama###
import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('resimler/futbol.jpg',0)
img2=img.copy()
template=cv2.imread('resimler/futbol2.jpg',0)
w,h=template.shape[::-1]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    method=eval(meth)
    img=img2.copy()

    res=cv2.matchTemplate(img,template,method)
    min_val,max_val,min_loc, max_loc=cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left=min_loc

    else:
        top_left=max_loc

    bottom_right=(top_left[0]+w,top_left[1]+h)

    cv2.rectangle(img,top_left,bottom_right,255,2)

plt.subplot(121),plt.imshow(res,cmap='gray')
plt.title('Matching Result'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap='gray')
plt.title('Detected Point'),plt.xticks([]),plt.yticks([])
plt.suptitle(meth)

plt.show()
