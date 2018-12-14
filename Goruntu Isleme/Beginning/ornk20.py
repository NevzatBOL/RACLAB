#-*-coding utf-8 -*-
#Image Perspektifi Alma
import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('resimler/sudoku.png')
rows,cols,ch=img.shape

pts1=np.float32([[40,26],[425,30],[9,445],[475,441]]) #Perspektifi alinacak cercevenin noktalari
pts2=np.float32([[0,0],[300,0],[0,300],[300,300]]) #perspektif ile tasinacak noktalar.

M=cv2.getPerspectiveTransform(pts1,pts2)

dst=cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('input')
plt.subplot(122),plt.imshow(dst),plt.title('output')
plt.show()
