import sys
import cv2
import imutils
import numpy as np
sys.path.append(".")

from shape import ShapeDetector

im = cv2.imread("Path.png")
# cv2.imshow("Path", im)
# cv2.waitKey(0)
# b,g,r = im[1082, 557]
#2936:924
#600:188

#print(b,g,r)
resized = imutils.resize(im, width=2936)
#cv2.imshow("resized", resized)
cv2.waitKey(0)
imgheight=im.shape[0]
imgwidth=im.shape[1]

y1 = 0
M = imgheight//20
N = imgwidth//20

for y in range(0,imgheight,M):
    for x in range(0, imgwidth, N):
        y1 = y + M
        x1 = x + N
        tiles = im[y:y+M,x:x+N]

        cv2.rectangle(im, (x, y), (x1, y1), (255, 0, 0),1)
        cv2.imwrite("save/" + str(x) + '_' + str(y)+".png",tiles)

cv2.imwrite("asas.png", im)
