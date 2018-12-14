#-*-coding: utf-8-*-
#Image Oteleme (Translation)
import numpy as np
import cv2

img=cv2.imread('resimler/futbol.jpg',0)
rows,cols=img.shape #resmin satır ve sutun degerleri alındı.

#M = [1 0 Tx]
#    [0 1 Ty]

M=np.float32([[1,0,100],[0,1,50]])
dst=cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
