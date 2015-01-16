#!/usr/bin/env python

import cv2
import cv2.cv as cv
import numpy as np
import sys

if __name__ == "__main__":
    try:
        img = cv2.imread(sys.argv[1], 0)
    except IndexError, e:
        print "Usage: %s <image>" % sys.argv[0]
        sys.exit(1)

    #img = cv2.medianBlur(img, 5)
    #cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img, cv.CV_HOUGH_GRADIENT, 1, 20,
                                param1=50,param2=30,minRadius=0,maxRadius=0)

    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('detected circles',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
