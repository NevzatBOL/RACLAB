#-*-coding: utf-8-*-
###Şerit Takibi4###

import cv2
import numpy as np

def unwarp(img, src, dst):
    h,w = img.shape[:2]

    M = cv2.getPerspectiveTransform(src, dst)
    Minv = cv2.getPerspectiveTransform(dst, src)

    warped = cv2.warpPerspective(img, M, (w,h), flags=cv2.INTER_LINEAR)
    return warped, M, Minv

def bilateral_adaptive_threshold(img, ksize=30, C=11, mode='floor'):
    mask = np.zeros_like(img)

    kernel_l = np.array([[1] * (ksize) + [-ksize]], dtype=np.int16)
    kernel_r = np.array([[-ksize] + [1] * (ksize)], dtype=np.int16)
    kernel_u = np.array([[1]] * (ksize) + [[-ksize]], dtype=np.int16)
    kernel_d = np.array([[-ksize]] + [[1]] * (ksize), dtype=np.int16)

    if mode == 'floor':
        delta = C * ksize
    elif mode == 'ceil':
        delta = -C * ksize

    left_thresh = cv2.filter2D(img, cv2.CV_16S, kernel_l, anchor=(ksize,0), delta=delta, borderType=cv2.BORDER_CONSTANT)
    right_thresh = cv2.filter2D(img, cv2.CV_16S, kernel_r, anchor=(0,0), delta=delta, borderType=cv2.BORDER_CONSTANT)
    up_thresh = cv2.filter2D(img, cv2.CV_16S, kernel_u, anchor=(0,ksize), delta=delta, borderType=cv2.BORDER_CONSTANT)
    down_thresh = cv2.filter2D(img, cv2.CV_16S, kernel_d, anchor=(0,0), delta=delta, borderType=cv2.BORDER_CONSTANT)

    if mode == 'floor':
        mask[((0 > left_thresh) & (0 > right_thresh)) | ((0 > up_thresh) & (0 > down_thresh))] = 255
    elif mode == 'ceil':
        mask[((0 < left_thresh) & (0 < right_thresh)) | ((0 < up_thresh) & (0 < down_thresh))] = 255

    return mask

def filter_lane_points(img,filter_type='neighborhood',ksize_r=25,C_r=8,ksize_b=35,C_b=5,
                       mask_noise=False,ksize_noise=65,C_noise=10,noise_thresh=135):
        
        strel_lab_b = cv2.getStructuringElement(shape=cv2.MORPH_ELLIPSE, ksize=(55,55))
        strel_rgb_r = cv2.getStructuringElement(shape=cv2.MORPH_ELLIPSE, ksize=(29,29))
        strel_open = cv2.getStructuringElement(shape=cv2.MORPH_ELLIPSE, ksize=(5,5))
        # Extract RGB R-channel and LAB B-channel
        rgb_r_channel = img[:,:,0]
        lab_b_channel = (cv2.cvtColor(img, cv2.COLOR_RGB2LAB))[:,:,2]
        # Apply tophat morphology
        rgb_r_tophat = cv2.morphologyEx(rgb_r_channel, cv2.MORPH_TOPHAT, strel_rgb_r, iterations=1)
        lab_b_tophat = cv2.morphologyEx(lab_b_channel, cv2.MORPH_TOPHAT, strel_lab_b, iterations=1)
        if filter_type == 'bilateral':
            rgb_r_thresh = bilateral_adaptive_threshold(rgb_r_tophat, ksize=ksize_r, C=C_r)
            lab_b_thresh = bilateral_adaptive_threshold(lab_b_tophat, ksize=ksize_b, C=C_b)
        elif filter_type == 'neighborhood':
            rgb_r_thresh = cv2.adaptiveThreshold(rgb_r_channel, 255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=ksize_r, C=-C_r)
            lab_b_thresh = cv2.adaptiveThreshold(lab_b_channel, 255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=ksize_b, C=-C_b)
        else:
            raise ValueError("Unexpected filter mode. Expected modes are 'bilateral' or 'neighborhood'.")
        if mask_noise: 
            noise_mask_part1 = cv2.inRange(lab_b_channel, noise_thresh, 255)
            noise_mask_part2 = bilateral_adaptive_threshold(lab_b_channel, ksize=ksize_noise, C=C_noise)
            noise_bool = np.logical_or(np.logical_not(noise_mask_part1), noise_mask_part2)
            noise_mask = np.zeros_like(rgb_r_channel, dtype=np.uint8)
            noise_mask[noise_bool] = 255

            merged_bool = np.logical_and(np.logical_or(rgb_r_thresh, lab_b_thresh), noise_mask)
            merged = np.zeros_like(rgb_r_channel, dtype=np.uint8)
            merged[merged_bool] = 255
        else:
            merged_bool = np.logical_or(rgb_r_thresh, lab_b_thresh)
            merged = np.zeros_like(rgb_r_channel, dtype=np.uint8)
            merged[merged_bool] = 255

        opened = cv2.morphologyEx(merged, cv2.MORPH_OPEN, strel_open, iterations=1)

        return opened

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
		
		#binary = bilateral_adaptive_threshold(frame)
		binary = filter_lane_points(frame)

        cv2.imshow("Filtre",binary)
	if cv2.waitKey(10) & 0xFF ==27:
		break
cam.release()
cv2.destroyAllWindows()