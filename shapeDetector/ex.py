#resized = imutils.resize(image, width=600)
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()

# loop over the contours
for c in cnts:
	# compute the center of the contour, then detect the name of the
	# shape using only the contour
	M = cv2.moments(c)
	cX = int((M["m10"] / M["m00"]) * ratio)
	cY = int((M["m01"] / M["m00"]) * ratio)
	shape = sd.detect(c)
	# multiply the contour (x, y)-coordinates by the resize ratio,
	# then draw the contours and the name of the shape on the image
	c = c.astype("float")
	c *= ratio
	c = c.astype("int")
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (255, 255, 255), 2)
	# show the output image
	cv2.imshow("Image", image)
	cv2.waitKey(0)


###SECOND
resized = imutils.resize(image,width=300)
ratio = image.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
edged = cv2.Canny(gray, 30, 150)

ksize = 3
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize,ksize))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
#thresh = cv2.morphologyEx(edged, cv2.MORPH_OPEN, kernel)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
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
        print(vX, vY, shape)
    # multiply the contour (x, y)-coordinates by the resize ratio,
    # then draw the contours and the name of the shape on the image
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
     # show the output image
        cv2.imshow("Image", image)
        cv2.waitKey(0)

cv2.imshow("Image", image)
cv2.waitKey(0)
