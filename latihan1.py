#menampilkan gambar
import cv2 # menyertakan library cv2 dari opencv
import time
img=cv2.imread("foto2.jpg")
cv2.imshow("display", img)
cv2.waitKey(0)#press any key
cv2,destroyAllWindows() 