#teknik overlay
import cv2 # menyertakan library cv2 dari opencv

img=cv2.imread("lenna.png")
overlay = img.copy()
cv2.rectangle(overlay, (250, 3), (450,200), (0,255,0), -1)

image = cv2.addWeighted(overlay, 0.3, img, 0.7, 0) #totalnya harus 100%
cv2.imshow("display", image)
cv2.waitKey(0)
cv2.destroyAllWindows()




