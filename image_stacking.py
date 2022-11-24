#image stacking (menyusun gambar)
import cv2 # menyertakan library cv2 dari opencv
import numpy as np

img=cv2.imread("lenna.png")
img=cv2.resize(img,(200,200))
copied = img.copy()
result = np.hstack((img,copied)) #hstack horisontal stack, verical = vstack

cv2.imshow("display", result)
cv2.waitKey(0)
cv2.destroyAllWindows()






