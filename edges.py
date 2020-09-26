import cv2
import numpy as np

image=cv2.imread('test_image.jpg') #Gives image in the form of numpy array


#Canny edge detection

"""Copying image array rather than assigning is the good practice
because in this way it doesnt change original image"""

lane_image=np.copy(image)
gray_image=cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
blur_image=cv2.GaussianBlur(gray_image,(5,5),0)

canny=cv2.Canny(blur_image,50,150)

cv2.imshow("Image",canny)
cv2.waitKey(0) # keep the image as long as we dont press any key from keyboard 
