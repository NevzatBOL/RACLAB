#-*-coding: utf-8-*-
###Şerit Takibi3 - Renk Uzayları###

import numpy as np
import cv2

def unwarp(img, src, dst):
    h,w = img.shape[:2]

    M = cv2.getPerspectiveTransform(src, dst)
    Minv = cv2.getPerspectiveTransform(dst, src)

    warped = cv2.warpPerspective(img, M, (w,h), flags=cv2.INTER_LINEAR)
    return warped, M, Minv

def RGB(img, r_th=120, g_th=100, b_th=50):
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]

    binary = np.zeros_like(R)
    binary[(R >= r_th) & (G >= g_th) & (B >= b_th)] = 255
    return binary

def HSV_V(img, threshold = (100,255)):
    hlv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    V = hlv[:,:,2]

    binary = np.zeros_like(V)
    binary[(V >= threshold[0]) & (V <= threshold[1])] = 255
    return binary

def HLS_L(img, threshold = (100,255)):
    hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    L = hls[:,:,1]

    binary = np.zeros_like(L)
    binary[(L >= threshold[0]) & (L <= threshold[1])] = 255
    return binary

def HLS_S(img, threshold = (100,255)):
    hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    S = hls[:,:,2]

    binary = np.zeros_like(S)
    binary[(S >= threshold[0]) & (S <= threshold[1])] = 255
    return binary

def LUV_L(img, threshold = (100,255)):
	luv = cv2.cvtColor(img, cv2.COLOR_RGB2LUV)
	L = luv[:, :, 0]

	binary = np.zeros_like(L)
	binary[(L >= threshold[0]) & (L <= threshold[1])] = 255
	return binary

def LUV_U(img, threshold = (0,90)):
	luv = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
	U = luv[:,:,1]

	binary = np.zeros_like(U)
	binary[(U >= threshold[0]) & (U <= threshold[1])] = 255
	return binary

def LUV_V(img, threshold = (150,255)):
	luv = cv2.cvtColor(img, cv2.COLOR_RGB2LUV)
	V = luv[:, :, 2]

	binary = np.zeros_like(V)
	binary[(V >= threshold[0]) & (V <= threshold[1])] = 255
	return binary

def LAB_L(img, threshold = (140,255)):
	lab = cv2.cvtColor(img, cv2.COLOR_RGB2Lab)
	L = lab[:, :, 0]

	binary = np.zeros_like(L)
	binary[(L >= threshold[0]) & (L <= threshold[1])] = 255
	return binary

def LAB_B(img, threshold = (140,255)):
	lab = cv2.cvtColor(img, cv2.COLOR_RGB2Lab)
	B = lab[:, :, 2]

	binary = np.zeros_like(B)
	binary[(B >= threshold[0]) & (B <= threshold[1])] = 255
	return binary

def combine(binary1,binary2):
	combine = np.zeros_like(binary1)
	combine[(binary1 == 255) & (binary2 == 255)] = 255
	return combine

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

		#RGB
		#binary=RGB(frame)

		#HSV
		#binary=HSV_V(frame)

		#HSL
		#binary=HLS_L(frame)
		#binary=HLS_S(frame)
		
		#LUV
		#binary=LUV_L(frame)
		#binary=LUV_U(frame)
		#binary=LUV_V(frame)
		
		#LAB
		#binary=LAB_L(frame)
		#binary=LAB_B(frame)

		#binary = combine(LUV_L(frame), LAB_B(frame))
		binary = combine(LUV_L(frame), HLS_S(frame))		
		
		cv2.imshow("Filtre",binary)
	if cv2.waitKey(10) & 0xFF ==27:
		break
cam.release()
cv2.destroyAllWindows()