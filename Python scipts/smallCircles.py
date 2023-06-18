import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('IMG_2317.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)


circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=30,param2=30,minRadius=15,maxRadius=50)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

print(circles.shape[1])

#plt.imshow(cimg, cmap='jet')
#plt.show()

cv2.namedWindow('detected circles',cv2.WINDOW_KEEPRATIO)
cv2.imshow('detected circles',cimg)
