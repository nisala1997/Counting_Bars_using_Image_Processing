import numpy as np
import cv2
import matplotlib.pyplot as plt

img_g=cv2.imread('IMG_23421.jpg',cv2.IMREAD_COLOR)
img=cv2.cvtColor(img_g,cv2.COLOR_BGR2GRAY)

kernel=np.ones((5,5),np.uint8)


ret,thresh=cv2.threshold(img,80,255,cv2.THRESH_BINARY)
dilate=cv2.dilate(thresh,kernel,2)
ret,thresh1=cv2.threshold(dilate,127,255,cv2.THRESH_BINARY)

sure_bg = cv2.dilate(thresh1,kernel,iterations=3)
dist_transform = cv2.distanceTransform(thresh1,cv2.DIST_L1,3)
ret, sure_fg = cv2.threshold(dist_transform,0.03*dist_transform.max(),255,0)

sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

ret, markers = cv2.connectedComponents(sure_fg)
markers = markers+1
markers[unknown==255] = 0

markers = cv2.watershed(img_g,markers)
img_g[markers == -1] = [255,0,0]

plt.imshow(img_g, cmap='jet')
plt.show()

#cv2.namedWindow('figure',cv2.WINDOW_KEEPRATIO)
#cv2.imshow('figure',unknown)
