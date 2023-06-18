import numpy as np
import cv2 as cv

img=cv.imread('IMG_23151.jpg',cv.IMREAD_GRAYSCALE)


temp=cv.imread('temp.png',cv.IMREAD_GRAYSCALE)
ret,template=cv.threshold(temp,100,255,cv.THRESH_BINARY)
##
cv.imshow('figure',template)

w, h = template.shape[::-1]

res = cv.matchTemplate(img,template,cv.TM_CCOEFF_NORMED)
threshold = 0.6
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv.imwrite('res.png',img)


cv.namedWindow('fig',cv.WINDOW_KEEPRATIO)
cv.imshow('fig',img)

cv.imshow('fig1',temp)
