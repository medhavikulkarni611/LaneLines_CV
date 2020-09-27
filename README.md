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





