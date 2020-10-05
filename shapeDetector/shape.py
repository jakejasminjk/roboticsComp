import cv2
class ShapeDetector:
    def __init__(self):
        pass
    def detect(self, c):
        # initialize the shape name and approximate the contour
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        # if the shape is a pentagon, it will have 5 vertices
        if (len(approx) <= 4):
            shape = "line"
        elif(len(approx) == 5):
            shape = "pentagon"
        # otherwise, we assume the shape is a circle
        elif(len(approx > 20)):
            shape = "circle"
        # return the name of the shape
        return shape
