#-*-coding: utf-8-*-
###Şerit Takibi6###

import numpy as np
import cv2

def unwarp(img, src, dst):
    h,w = img.shape[:2]

    M = cv2.getPerspectiveTransform(src, dst)
    Minv = cv2.getPerspectiveTransform(dst, src)

    warped = cv2.warpPerspective(img, M, (w,h), flags=cv2.INTER_LINEAR)
    return warped, M, Minv

def hls_thresh(img, thresh=(180, 255)):
    hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    hls_l = hls[:,:,1]
    hls_l = hls_l*(255/np.max(hls_l))

    binary_output = np.zeros_like(hls_l)
    binary_output[(hls_l > thresh[0]) & (hls_l <= thresh[1])] = 255
    return binary_output

def sliding_window_polyfit(img):
    histogram = np.sum(img[img.shape[0]//2:,:], axis=0)

    midpoint = np.int(histogram.shape[0]//2)
    quarter_point = np.int(midpoint//2)

    leftx_base = np.argmax(histogram[quarter_point:midpoint]) + quarter_point
    rightx_base = np.argmax(histogram[midpoint:(midpoint+quarter_point)]) + midpoint
    
    nwindows = 10
    window_height = np.int(img.shape[0]/nwindows)

    nonzero = img.nonzero()
    nonzeroy = np.array(nonzero[0])
    nonzerox = np.array(nonzero[1])

    leftx_current = leftx_base
    rightx_current = rightx_base

    margin = 40
    minpix = 10

    left_lane_inds = []
    right_lane_inds = []
    rectangle_data = []

    for window in range(nwindows):  
        win_y_low = img.shape[0] - (window+1)*window_height
        win_y_high = img.shape[0] - window*window_height
        win_xleft_low = leftx_current - margin
        win_xleft_high = leftx_current + margin
        win_xright_low = rightx_current - margin
        win_xright_high = rightx_current + margin
        rectangle_data.append((win_y_low, win_y_high, win_xleft_low, win_xleft_high, win_xright_low, win_xright_high))
    
        good_left_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) & (nonzerox >= win_xleft_low) & (nonzerox < win_xleft_high)).nonzero()[0]
        good_right_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) & (nonzerox >= win_xright_low) & (nonzerox < win_xright_high)).nonzero()[0]
 
        left_lane_inds.append(good_left_inds)
        right_lane_inds.append(good_right_inds)

        if len(good_left_inds) > minpix:
            leftx_current = np.int(np.mean(nonzerox[good_left_inds]))
        if len(good_right_inds) > minpix:        
            rightx_current = np.int(np.mean(nonzerox[good_right_inds]))

    left_lane_inds = np.concatenate(left_lane_inds)
    right_lane_inds = np.concatenate(right_lane_inds)

    leftx = nonzerox[left_lane_inds]
    lefty = nonzeroy[left_lane_inds] 
    rightx = nonzerox[right_lane_inds]
    righty = nonzeroy[right_lane_inds] 

    left_fit, right_fit = (None, None)
    if len(leftx) != 0:
        left_fit = np.polyfit(lefty, leftx, 2)
    if len(rightx) != 0:
        right_fit = np.polyfit(righty, rightx, 2)
    
    return left_fit, right_fit


def draw_lane(original_img, binary_img, l_fit, r_fit, Minv):
    new_img = np.copy(original_img)
    if l_fit is None or r_fit is None:
        return original_img

    warp_zero = np.zeros_like(binary_img).astype(np.uint8)
    color_warp = np.dstack((warp_zero, warp_zero, warp_zero))

    h,w = binary_img.shape
    ploty = np.linspace(0, h-1, num=h)
    left_fitx = l_fit[0]*ploty**2 + l_fit[1]*ploty + l_fit[2]
    right_fitx = r_fit[0]*ploty**2 + r_fit[1]*ploty + r_fit[2]

    pts_left = np.array([np.transpose(np.vstack([left_fitx, ploty]))])
    pts_right = np.array([np.flipud(np.transpose(np.vstack([right_fitx, ploty])))])
    pts = np.hstack((pts_left, pts_right))

    cv2.fillPoly(color_warp, np.int_([pts]), (0,255, 0))
    cv2.polylines(color_warp, np.int32([pts_left]), isClosed=False, color=(255,0,255), thickness=15)
    cv2.polylines(color_warp, np.int32([pts_right]), isClosed=False, color=(0,255,255), thickness=15)

    newwarp = cv2.warpPerspective(color_warp, Minv, (w, h)) 
    result = cv2.addWeighted(new_img, 1, newwarp, 0.5, 0)
    return result


def green_filter(frame):
	Lower = np.array([50, 100, 100])
	Upper = np.array([70, 255, 255])	

	blurred=cv2.GaussianBlur(frame,(11,11),0)
	hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)

	mask=cv2.inRange(hsv,Lower,Upper)
	mask=cv2.erode(mask,None,iterations=2)
	mask=cv2.dilate(mask,None,iterations=2)

	_,cnts,_=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	if len(cnts)>0:
		c=max(cnts,key=cv2.contourArea)
		x,y,w,h=cv2.boundingRect(c)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),0)
		return x,y,w,h

def white_filter(frame):
	sobel=hls_thresh(frame) 

	_,cnts,_ = cv2.findContours(sobel.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
	for i,c in enumerate(cnts):
		if cv2.contourArea(c)<300:
			continue
		x,y,w,h=cv2.boundingRect(c)
		cv2.line(frame,(x,y),(x+w,y+h),(0,0,255),5)
		
		if x+w > 200:
    			cv2.putText(frame,'full line',(x+20,y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2,cv2.LINE_AA)


cam=cv2.VideoCapture('videolar/serit1.mp4')
while(1):
	ret,frame=cam.read()	
	if ret:   		
		h,w=frame.shape[:2]

		#src noktaları ornek29.py kullanılarak tespit edilebilir.
		src = np.float32([(130,530),
				  (885,530), 
				  (380,350),
				  (590,350)])
		dst = np.float32([(400,h),
				  (w-400,h),
				  (400,0),
				  (w-400,0)])

		Img_warp, M, Minv = unwarp(frame, src, dst)
		sobel=hls_thresh(Img_warp)

		left_fit, right_fit = sliding_window_polyfit(sobel)

		result = draw_lane(frame, sobel, left_fit, right_fit, Minv)

		a,b,c,d=green_filter(result) 
		white_filter(result[b:b+d,a:a+c])
		cv2.imshow("frame",result)
	if cv2.waitKey(10) & 0xFF ==27:
		break
cam.release()
cv2.destroyAllWindows()