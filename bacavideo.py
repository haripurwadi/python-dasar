import cv2
import numpy as np

cap = cv2.VideoCapture('video\\TownCentreXVID.avi')

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([40, 0, 40])
    upper = np.array([100, 255, 100,])

    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((1,1), np.uint8)
   
    cv2.imshow('frame', frame)
  
    k = cv2.waitKey(30) &  0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()