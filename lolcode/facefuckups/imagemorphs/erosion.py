import cv2
import numpy as np

img = cv2.imread('/home/sidhant/Pictures/Webcam/sidface.jpg',0)
kernel = np.ones((3,3),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imshow('Erosion',erosion)
cv2.waitKey(0)
    