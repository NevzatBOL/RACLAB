#-*-coding: utf-8 -*-
###Şerit Takibi2 - Sobel Filter###

import cv2
import numpy as np
from skimage import exposure

#skimage kurulu degilse asagıdaki satır kullanılarak kurulum yapılabilir.
#sudo pip2 install scikit-image 

def unwarp(img, src, dst):
    h,w = img.shape[:2]

    M = cv2.getPerspectiveTransform(src, dst)
    Minv = cv2.getPerspectiveTransform(dst, src)

    warped = cv2.warpPerspective(img, M, (w,h), flags=cv2.INTER_LINEAR)
    return warped, M, Minv

def abs_sobel_thresh(img, orient='x', sobel_kernel=3, thresh=(80,255)):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    if orient == 'x':
        abs_sobel = np.absolute(cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel))
    elif orient == 'y':
        abs_sobel = np.absolute(cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel))

    #scaled_sobel = np.uint8(255*abs_sobel/np.max(abs_sobel))
    scaled_sobel = np.uint8(abs_sobel)
    binary = np.zeros_like(scaled_sobel)
    binary[(scaled_sobel >= thresh[0]) & (scaled_sobel <= thresh[1])] = 255
    return binary

def mag_thresh(img, sobel_kernel=3, thresh=(100, 255)):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)

    mag_sobel = np.sqrt(sobelx**2 + sobely**2)
    scaled_sobel = np.uint8(255*mag_sobel/np.max(mag_sobel))

    binary = np.zeros_like(scaled_sobel)
    binary[(scaled_sobel >= thresh[0]) & (scaled_sobel <= thresh[1])] = 255
    return binary

def dir_thresh(img, sobel_kernel=7, thresh=(0.6, np.pi/2)):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)

    dir_sobel = np.arctan2(np.absolute(sobely), np.absolute(sobelx))
    binary = np.zeros_like(dir_sobel)
    binary[(dir_sobel >= thresh[0]) & (dir_sobel <= thresh[1])] = 255
    return binary

def combined(img, ksize = 5):
    gradx = abs_sobel_thresh(img, orient='x', sobel_kernel=ksize)
    grady = abs_sobel_thresh(img, orient='y', sobel_kernel=ksize)
    mag_binary = mag_thresh(img, sobel_kernel=ksize)
    dir_binary = dir_thresh(img, sobel_kernel=ksize)
    combined = np.zeros_like(dir_binary)
    #combined[((gradx == 255) & (grady == 255)) | ((mag_binary == 255) & (dir_binary == 255))] = 255
    #combined[(gradx == 255) | ((mag_binary == 255) & (dir_binary == 255))] = 255
    combined[(gradx == 255) & (mag_binary == 255)] = 255
    return combined

def gamma_(img, gamma=1.2):
	#gamma < 1 ise parlaklık artar.
	#gamma > 1 ise parlaklık azalır.
	return exposure.adjust_gamma(img, gamma)

cam=cv2.VideoCapture('videolar/serit2.mp4')
while(1):
	ret,frame=cam.read()
	if ret:	
		h,w=frame.shape[:2]

		#src noktaları ornek29.py kullanılarak tespit edilebilir.
		src = np.float32([(575,464),
		          (707,464), 
		          (258,682), 
		          (1049,682)])
		dst = np.float32([(450,h),
		          (w-450,h),
		          (450,0),
		          (w-450,0)])
		#Img_warp, M, Minv = unwarp(frame, src, dst)

		#binary = abs_sobel_thresh(frame)
		#binary = mag_thresh(frame)
		#binary = dir_thresh(frame)

		#binary = combined(frame)

		gamma = gamma_(frame)
		binary = combined(gamma)

		#cv2.imshow("Gamma",gamma)
		cv2.imshow("Filtre",binary)
	if cv2.waitKey(10) & 0xFF ==27:
		break
cam.release()
cv2.destroyAllWindows()
