#-*-coding: utf-8 -*-
#Image Boyutlandirma ile Goruntu Birlestirme
import numpy as np
import cv2

A=cv2.imread('resimler/apple.jpg')
B=cv2.imread('resimler/orange.jpg')


#600x600 piksel icin:
#600 -> 300 -> 150 -> 75 -> 37,5 #islem 75 te son bulmalidir.
#buyuzden 0. indisten 3. indise kadar kucultme islemi yapilabilir.
#512x512 piksel icin:
#512 -> 256 -> 128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 
#islem 8. indise kadar kucultme islemi yapilabilir.

G = A.copy()
gpA = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

G = B.copy()
gpB = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

lpA = [gpA[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)

lpB = [gpB[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
    LS.append(ls)

ls_ = LS[0]
for i in xrange(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

real = np.hstack((A[:,:cols/2],B[:,cols/2:]))

cv2. imshow("real",real)
cv2. imshow("ls",ls_)

cv2.waitKey(0)
cv2.destroyAllWindows()
