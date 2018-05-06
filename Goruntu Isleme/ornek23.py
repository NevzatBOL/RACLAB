#-*-coding: utf-8-*-
###Şerit Takibi1###

import numpy as np
import cv2

cam=cv2.VideoCapture('videolar/serit1.mp4')

def filter(img):
    lower = np.array([210,110,70])
    upper = np.array([255,255,255])
    return cv2.inRange(img, lower, upper)
    
def ROI(img):
    y_shape = img.shape[0]
    x_shape = img.shape[1]
    vertices = np.array([[x_shape/2, y_shape*0.6], [x_shape/2, y_shape*0.6],
            [x_shape, y_shape], [0, y_shape]], dtype=np.int32)
    return region_of_interest(img, [vertices])

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)  
  
    if len(img.shape) > 2:
        channel_count = img.shape[2]  
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
          
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def removeChannels(img):
    if len(img.shape) > 2:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img

def edge_detection(img): 
    img = removeChannels(img)
    blur = cv2.GaussianBlur(img,(5,5), 0)
    edges = cv2.Canny(blur, 50, 150)
    return edges

def draw_lines(img, lines, color=[255, 0, 0], thickness=5):
    for line in lines:
        for x1,y1,x2,y2 in line:
            slope = ((y2-y1)/(x2-x1))
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):

    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img

def weighted_img(img, initial_img):
    return cv2.addWeighted(initial_img, 0.8, img, 1.0, 0)

while(1):
	ret,frame=cam.read()
	if ret:
		original_image = np.copy(frame)
		threshold = filter(frame)
		roi = ROI(threshold)
		edge = edge_detection(roi)
		hough=hough_lines(edge, rho=1, theta=np.pi/180, threshold=10, min_line_len=40, max_line_gap=100)

		#cv2.imshow("Threshold",threshold)
		#cv2.imshow("ROI",roi)
		#cv2.imshow("Edge",edge)
		#cv2.imshow("Hough",hough)

		frame=cv2.bitwise_and(frame,frame, mask=hough)
		img = weighted_img(frame, original_image)
		cv2.imshow("frame",img)
	if cv2.waitKey(10) & 0xFF ==27:
		break
cam.release()
cv2.destroyAllWindows()
