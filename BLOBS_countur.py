#blobs untuk mencari countur biru (centroid, luas keliling ukuran dan komparasu)

import cv2 # menyertakan library cv2 dari opencv
import numpy as np


image = cv2.imread("circles.jpg")
img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lowBlue = np.array([110, 10, 10])
highBlue = np.array([130, 255, 255])

mask = cv2.inRange (img, lowBlue, highBlue)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)    #RETR_EXTERNAL = ambil kontur terbesar, jka di dlm kontur ada contur
print (len(contours))#jumlah countur
print(cv2.contourArea(contours[0])) #Luas

M = cv2.moments(contours[0]) # menghitung moment (pusat masa)
cx=int(M['m10']/M['m00'])#koordinat x
cy=int(M['m01']/M['m00'])#coordinat y
print("Centroid: ({}, {})".format(cx,cy))

imgx = cv2.drawContours(image, contours, -1, (0,255,0), 3) #memunculkan countour
cv2.circle(imgx, (cx, cy), 5,(0,0,255), -1) #memunculkan centroid pada gambar

#result=cv2.bitwise_and(image, image, mask=masking)

cv2.imshow("display", imgx)
cv2.waitKey(0)
cv2.destroyAllWindows()



