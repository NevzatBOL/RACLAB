#-*-coding utf-8 -*-
#Affine Transformation
import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('resimler/sudoku.png')
rows,cols,ch=img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2=np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('input')
plt.subplot(122),plt.imshow(dst),plt.title('output')
plt.show()
