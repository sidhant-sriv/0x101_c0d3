path = r'/home/sidhant/Pictures/Webcam/sidface.jpg'
import cv2
src = cv2.imread(path)
window_name = 'Image'
image = cv2.flip(src, 1)
cv2.imshow(window_name, image)
cv2.waitKey(0)
