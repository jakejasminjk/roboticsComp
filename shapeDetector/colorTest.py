import sys
import cv2
import imutils
import numpy as np

image = cv2.imread('map-blue.png')
bLower = np.array([110,50,50])
bUpper = np.array([130,255,255])
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, bLower, bUpper)

cv2.imshow("Blue", mask)
cv2.waitKey(0)
