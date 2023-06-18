import numpy as np
import cv2

img=cv2.imread('IMG_23421.jpg',cv2.IMREAD_GRAYSCALE)



blur=cv2.blur(img,(5,5))
median = cv2.medianBlur(img,5)
kernel=np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(median, cv2.MORPH_OPEN, kernel)
ret,thresh1= cv2.threshold(opening,100,255,cv2.THRESH_BINARY)


im2,contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))
cv2.namedWindow('figure',cv2.WINDOW_KEEPRATIO)
cv2.imshow('figure',np.hstack((img,thresh1)))
