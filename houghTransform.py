import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_hough_lines(image,lines):
    lined_image=np.zeros_like(image)
    if lines is not None: #to check if there is atleast a single bin
        """Every line is a 2D array conatining line coordinates [[x1,y1,x2,y2]]
        These coordinates specify the line's parameters, as well as the location
        of lines w.r.t image space,ensuring that they are placed in the correct
        position"""
        for line in lines:
            x1,y1,x2,y2=line.reshape(4)
            cv2.line(lined_image,(x1,y1),(x2,y2),(0,255,0),5)
    return lined_image

def canny(image):

    gray_image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur_image=cv2.GaussianBlur(gray_image,(5,5),0)
    canny=cv2.Canny(blur_image,50,150)
    return canny

def region_of_interest(image):
    height=image.shape[0]
    polygons=np.array([[(200,height),(1100,height),(550,250)]])
    mask=np.zeros_like(image)
    cv2.fillPoly(mask,polygons,255)
    masked_image=cv2.bitwise_and(image,mask)
    return masked_image

image=cv2.imread('test_image.jpg')
lane_image=np.copy(image)
canny_image=canny(lane_image)
cropped_image=region_of_interest(canny_image)

"""precision of 2 pixels accompanied by a 1 degree precision in radians and 4th argument
is the threshold which tells the no of intersections threshold to select the
best bin, 5th arg is the placeholder and 6th arg is the length of a line in
pixels which we will accept at the output and the last one is the accpeted gap
between broken lines which basically contribute to a single line"""

hough_lines=cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
line_image=display_hough_lines(lane_image,hough_lines)
final_image=cv2.addWeighted(lane_image,1,line_image,1,1)
cv2.imshow("Image",final_image)
cv2.waitKey(0)
