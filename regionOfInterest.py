import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):

    gray_image=cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
    blur_image=cv2.GaussianBlur(gray_image,(5,5),0)
    canny=cv2.Canny(blur_image,50,150)
    return canny

def region_of_interest(image):
    height=image.shape[0]

    """Vertices are specified by observing the Image
    Also,fillPoly function takes only array of polygons thus we need to pass
    in an array form eventhough there is only single polygon"""

    polygons=np.array([[(200,height),(1100,height),(550,250)]])

    """zero like Creates a black image of same dimension as that of original Image
    Then we draw the polygon of region of interest on that black image"""

    mask=np.zeros_like(image)
    cv2.fillPoly(mask,polygons,255)

    """Now to get the edges of lane we perform "bitwiseand" of masked image
    with canny image so that only edges corresponding to lanes are visible"""

    masked_image=cv2.bitwise_and(image,mask)
    return masked_image

image=cv2.imread('test_image.jpg')
lane_image=np.copy(image)
canny=canny(lane_image)

cv2.imshow("Image",region_of_interest(canny))
cv2.waitKey(0)
