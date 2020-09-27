# Identify The Lane Lines Using OpenCV  
In this project, using Canny Edge Detector and OpenCV library the lane lines are identified from a camera image.

## Installation
```bash
pip install opencv-python
pip install numpy
pip install matplotlib
```
### Canny Edge Detection Technique
In this technique, edges are identified by sharp changes in the intensities of adjacent pixels.
When we interpret an image as Numpy array,we get array of pixels where each pixel intensity is denoted by some numeric value ranging from 0 to 255.

* Gradient:
It is a measure of change in brightness over adjacent pixels. Strong gradient implies sudden or sharp change, which gives us edges.

The following steps are followed while applying this technique.

1. Convert an image from RGB to grayscale
<img src="https://github.com/medhavikulkarni611/LaneLines_CV/blob/master/test_image.jpg" width="400">   <img src="https://github.com/medhavikulkarni611/LaneLines_CV/blob/master/gray_image.png" width="400">

2. Reduce noise in image by applying Gaussian blur.
This step can be skipped as the canny method provided by OpenCV applies Gaussian blur with 5 X 5 kernal before performing edge detection

3. Apply Canny method
<img src="https://github.com/medhavikulkarni611/LaneLines_CV/blob/master/gray_image.png>   <img src="https://github.com/medhavikulkarni611/LaneLines_CV/blob/master/Canny_Edges.png" width="400">


Now the next step is to consider only region of interest and get only the lane edges and ignore the remaining part of image.

## Results
