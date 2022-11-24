#memberi warna (masking) dengan melakukan and atau or  
import cv2 # menyertakan library cv2 dari opencv
import numpy as np


image = cv2.imread("circles.jpg")
img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lowBlue = np.array([110, 10, 10])
highBlue = np.array([130, 255, 255])

masking = cv2.inRange (img, lowBlue, highBlue)
result=cv2.bitwise_and(image, image, mask=masking)

cv2.imshow("display", result)
cv2.waitKey(0)
cv2.destroyAllWindows()



