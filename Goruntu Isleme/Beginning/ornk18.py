#-*-coding: utf-8-*-
#Image Dondurme (Rotation)
import numpy as np
import cv2

img=cv2.imread('resimler/futbol.jpg',0)
rows,cols=img.shape

#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html#geometric-transformations
#buradan matamatiksel formulune bakabilirsiniz.
M=cv2.getRotationMatrix2D((cols/2,rows/2),110,1) #rotasyon degeri
dst=cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('rotaion',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
