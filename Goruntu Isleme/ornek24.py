#-*-coding: utf-8-*-
###Şerit Takibi2###

import numpy as np
import cv2

def unwarp(img, src, dst):
    h,w = img.shape[:2]

    M = cv2.getPerspectiveTransform(src, dst)
    Minv = cv2.getPerspectiveTransform(dst, src)

    warped = cv2.warpPerspective(img, M, (w,h), flags=cv2.INTER_LINEAR)
    return warped, M, Minv

def abs_sobel_thresh(img, orient='x', thresh_min=100, thresh_max=255):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    sobel = cv2.Sobel(gray, cv2.CV_64F, orient=='x', orient=='y')
    abs_sobel = np.absolute(sobel)
    scaled_sobel = np.uint8(255*abs_sobel/np.max(abs_sobel))
    sxbinary = np.zeros_like(scaled_sobel)
    sxbinary[(scaled_sobel >= thresh_min) & (scaled_sobel <= thresh_max)] = 255

    return sxbinary

def mag_thresh(img, orient='x', thresh_min=100, thresh_max=255):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

    mag_sobel = np.sqrt(np.square(sobelx) + np.square(sobely))
    scaled_sobel = np.uint8(255*mag_sobel/np.max(mag_sobel))

    sxbinary = np.zeros_like(scaled_sobel)
    sxbinary[(scaled_sobel >= thresh_min) & (scaled_sobel <= thresh_max)] = 255

    return sxbinary

def dir_thresh(img, sobel_kernel=7, thresh=(100, 255)):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)

    abs_sobelx = np.absolute(sobelx)
   
    scaled_sobelx = np.uint8(255*abs_sobelx/np.max(abs_sobelx))

    binary_output =  np.zeros_like(scaled_sobelx)
    binary_output[(scaled_sobelx >= thresh[0]) & (scaled_sobelx <= thresh[1])] = 255
    return binary_output

def hls_thresh1(img, thresh=(25, 255)):
    hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    binary_output = np.zeros_like(hls[:,:,2])
    binary_output[(hls[:,:,2] > thresh[0]) & (hls[:,:,2] <= thresh[1])] = 255
    return binary_output

def hls_thresh2(img, thresh=(180, 255)):
    hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    hls_l = hls[:,:,1]
    hls_l = hls_l*(255/np.max(hls_l))

    binary_output = np.zeros_like(hls_l)
    binary_output[(hls_l > thresh[0]) & (hls_l <= thresh[1])] = 255
    return binary_output

cam=cv2.VideoCapture('videolar/serit2.mp4')
while(1):
	ret,frame=cam.read()	
	if ret:   
		h,w=frame.shape[:2]

		#src noktaları ornek27.py kullanılarak tespit edilebilir.
		src = np.float32([(575,464),
				  (707,464), 
				  (258,682), 
				  (1049,682)])
		dst = np.float32([(450,h),
				  (w-450,h),
				  (450,0),
				  (w-450,0)])

		#Img_warp, M, Minv = unwarp(frame, src, dst)
		#sobel=abs_sobel_thresh(frame) 
		#sobel=mag_thresh(frame) 
		#sobel=dir_thresh(frame) 
		#sobel=hls_thresh1(frame) 
		sobel=hls_thresh2(frame) 

		cv2.imshow("frame",sobel)
	if cv2.waitKey(10) & 0xFF ==27:
		break
cam.release()
cv2.destroyAllWindows()
