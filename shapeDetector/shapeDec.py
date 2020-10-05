import sys
import cv2
import imutils
import numpy as np
import time
sys.path.append(".")
from os import system
from shape import ShapeDetector

start = time.time()
mapC = sys.argv[1]
#Bitwise and to seperate image
# --------------------------------------------
image = cv2.imread(mapC)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([0, 0, 0])
upper = np.array([15, 15, 15])
mask = cv2.inRange(hsv, lower, upper)
cv2.imwrite("Black.png", mask);

resized = imutils.resize(image,width=300)
ratio = image.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray, 7)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
edged = cv2.Canny(gray, 30, 150)

ksize = 3
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize,ksize))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# ~ cnts = cnts[0] if imutils.is_cv2() else cnts[1]
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()
vX = 0
vY = 0
end = [0,0]
for c in cnts:
    # compute the center of the contour, then detect the name of the
    # shape using only the contour
     M = cv2.moments(c)
     if M["m00"] != 0:
        cX = int((M["m10"] / M["m00"]))
        cY = int((M["m01"] / M["m00"]))
        vX = cX
        vY = cY
        shape = sd.detect(c)
    # multiply the contour (x, y)-coordinates by the resize ratio,
    # then draw the contours and the name of the shape on the image
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
     # show the output image
        ##cv2.imshow("Image", image)
        ##cv2.waitKey(0)

##cv2.imshow("Image", image)
#cv2.waitKey(0)

#Color Mask
#Blue color
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
bLower = np.array([110,50,50])
bUpper = np.array([130,255,255])
#Green Color
gLower = np.array([40, 100, 20])
gUpper = np.array([73,255,255])
# Black color
lower = np.array([0, 0, 0])
upper = np.array([255, 255, 10])
#Red color
rLower = np.array([0,50,50])
rUpper = np.array([10,255,255])


colVal = 0
vals = [[rLower,rUpper],[gLower,gUpper],[bLower,bUpper]]
checks = 0
found = False
while(checks!=len(vals) and found == False):
    xLower = vals[checks][0]
    xUpper = vals[checks][1]
    mask = cv2.inRange(hsv, xLower, xUpper)
    cv2.imwrite("Image1.png", mask);
    ##cv2.imshow('image', resized)
    ##cv2.waitKey(0)
    res = cv2.bitwise_and(image,image, mask= mask)
    cv2.imwrite("Res.png", res)
    ##cv2.imshow('mask', mask)
    #cv2.waitKey(0)
    img1 = cv2.imread("Image1.png")

#----------------------------------------------
    resized = imutils.resize(img1,width=300)
    ratio = img1.shape[0] / float(resized.shape[0])
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 7)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    edged = cv2.Canny(gray, 30, 150)

    ksize = 1
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize,ksize))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # ~ cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cnts = imutils.grab_contours(cnts)
    sd = ShapeDetector()
    vX = 0
    vY = 0

    for c in cnts:
        # compute the center of the contour, then detect the name of the
        # shape using only the contour
         M = cv2.moments(c)
         if M["m00"] != 0:
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
            vX = cX
            vY = cY
            shape = sd.detect(c)
            #print(vX*ratio, vY*ratio, shape)
            if(shape == "pentagon"):
                print(vX, vY)
                #cv2.imshow("FOUND",mask)
                cv2.imwrite( "Found.png", mask);
                found = True
                colVal = checks
                print("Pentagon found at {},{}".format(vX,vY))
                print("Found in Rotation ",checks)
            #print(vX, vY, shape)
        # multiply the contour (x, y)-coordinates by the resize ratio,
        # then draw the contours and the name of the shape on the image
            c = c.astype("float")
            c *= ratio
            c = c.astype("int")
            cv2.drawContours(img1, [c], -1, (0, 255, 0), 2)
            cv2.putText(img1, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 0, 0), 2)
         # show the output image
            #cv2.imshow("Image", img1)
            #cv2.waitKey(0)
            if(found == True):
                break
    checks+=1

#-----------------------------------------------
    edged = cv2.Canny(mask, 30, 150)
    #cv2.imshow("Edged", edged)
    #cv2.waitKey(0)
b,g,r = image[vY, vX]
if b == 255:
    print("color is Blue")
elif g == 255:
    print("color is Green")
else:
    print("color is Red")

#-----------------------------------------------

#Center of circle pixels
img1 = cv2.imread("Found.png")
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray, 7)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
edged = cv2.Canny(gray, 30, 150)

ksize = 1
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize,ksize))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# ~ cnts = cnts[0] if imutils.is_cv2() else cnts[1]
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()

for c in cnts:
    # compute the center of the contour, then detect the name of the
    # shape using only the contour
     M = cv2.moments(c)
     if M["m00"] != 0:
        cX = int((M["m10"] / M["m00"]))
        cY = int((M["m01"] / M["m00"]))
        shape = sd.detect(c)
        #print(vX*ratio, vY*ratio, shape)
        if(shape == "circle"):
            #cv2.imshow("cic",mask)
            cv2.imwrite( "cic.png", mask);
            end[0] = cX
            end[1] = cY
            print("circle found at {},{}".format(end[0],end[1]))
        #print(vX, vY, shape)
    # multiply the contour (x, y)-coordinates by the resize ratio,
    # then draw the contours and the name of the shape on the image
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(img1, [c], -1, (0, 0, 255), 2)
        cv2.putText(img1, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 0, 0), 2)
     # show the output image
        #cv2.imshow("CIC", img1)
        #cv2.waitKey(0)


#Color isolation
#-----------------------------------------------------
image = cv2.imread(mapC)
#Not using resized
#resized = imutils.resize(image, width=600)

    # Converts images from BGR to HSV
#Blue color
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#mask = cv2.inRange(hsv, lower_range, upper_range)
#COLOR MASK
mask = cv2.inRange(hsv, vals[colVal][0], vals[colVal][1])
#BLACK MASK
mask2 = cv2.inRange(hsv, lower, upper)

cv2.imwrite("Color_Image.png", mask);
#cv2.imshow('image', resized)
#cv2.waitKey(0)
##cv2.imshow('mask', mask)
##cv2.waitKey(0)
##cv2.imshow('mask2', mask2)
##cv2.waitKey(0)

img1 = cv2.imread("Black.png")
img2 = cv2.imread("Color_Image.png")

alpha = 1
    # Python 3
if 0 <= alpha <= 1:
    alpha = 1
# [load]
src1 = cv2.imread(cv2.samples.findFile('Black.png'))
src2 = cv2.imread(cv2.samples.findFile('Color_Image.png'))
# [load]
if src1 is None:
    print("Error loading src1")
    exit(-1)
elif src2 is None:
    print("Error loading src2")
    exit(-1)
# [blend_images]
#since images don't overlap alpha = 1 and beta = 1 and gamma = 0.0
beta = 1
dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)
# [blend_images]
# [display]
#cv2.imshow('dst', dst)
cv2.imwrite("Path.png", dst);
#cv2.waitKey(0)

###Corner detection of correct Map
#-----------------------------------------------------
# img = cv2.imread("Path.jpg")
# resized = imutils.resize(img,width=1400)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray,2,3,0.04)
#
# #result is dilated for marking the corners, not important
# dst = cv2.dilate(dst,None)
#
# # Threshold for an optimal value, it may vary depending on the image.
# img[dst>0.01*dst.max()]=[0,0,255]
#
# #cv2.imshow('dst',img)
# #cv2.waitKey(0)
#-----------------------------------------------------

### Threshold of correct Map
#------------------------------
image = cv2.imread("Path.png")
# resized = imutils.resize(image, width=300)
# ratio = image.shape[0] / float(resized.shape[0])
# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray, 7)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()
##cv2.imshow("TreshPath",thresh)
cv2.imwrite("TreshPath.png", dst);
#cv2.waitKey(0)
# -------------------------------

run = "path.py Path.png Home.png {} {} {} {}".format(vX, vY, end[0], end[1])
system(run)
end = time.time()
total = end - start
print('total time elasped: {}'.format(total))
