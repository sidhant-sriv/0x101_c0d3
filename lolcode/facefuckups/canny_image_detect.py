import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/sidhant/Pictures/Webcam/sidface.jpg',0)
edges = cv2.Canny(img,50,50)

cv2.imshow('Edges',edges)
cv2.waitKey(0)
