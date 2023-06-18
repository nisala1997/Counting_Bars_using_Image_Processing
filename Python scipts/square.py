import numpy as np
import cv2
import argparse


refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
        
	global refPt, cropping
	
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True

	elif event == cv2.EVENT_LBUTTONUP:
                
		refPt.append((x, y))
		cropping = False

		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.namedWindow("image",cv2.WINDOW_KEEPRATIO)
		cv2.imshow("image", image)


image = cv2.imread('IMG_2321.jpg')
clone = image.copy()
cv2.namedWindow("image",cv2.WINDOW_KEEPRATIO)
cv2.setMouseCallback("image", click_and_crop)

while True:
	cv2.namedWindow('image',cv2.WINDOW_KEEPRATIO)
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
	
	if key == ord("r"):
		image = clone.copy()
		
	elif key == ord("c"):
		break

if len(refPt) == 2:
	roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	cv2.namedWindow('ROI',cv2.WINDOW_KEEPRATIO)
	cv2.imshow("ROI", roi)
	roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
	kernel = np.ones((50,50),np.uint8)
	blur = cv2.medianBlur(roi,15)
	ret,thresh=cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
	dilation = cv2.dilate(thresh,kernel,iterations = 1)
	ret,thresh1=cv2.threshold(dilation,127,255,cv2.THRESH_BINARY_INV)
	cv2.namedWindow('fig',cv2.WINDOW_KEEPRATIO)
	cv2.imshow("fig",thresh1)
	im2,contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	print(len(contours)-3)
	cv2.waitKey(0)
	
cv2.destroyAllWindows()


