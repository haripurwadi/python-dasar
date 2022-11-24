#teknik overlay
import cv2 # menyertakan library cv2 dari opencv
import numpy as np

img = np.zeros((312,312,3), np.uint8)
img[:,:,0] = 225 # 2 = merah, 0 = biru 1= hijau 255 kejelasan warna max
img[:,:,2] = 225 #biru
#img[:,:,1] = 225

cv2.imshow("display", img)
cv2.waitKey(0)
cv2.destroyAllWindows()





