#menampilkan gambar
import cv2 # menyertakan library cv2 dari opencv
import time

camera=cv2.VideoCapture(0) # membaca kamera 1
while True: #selelu diakhiri dengan tanda :
    ret, image = camera.read() #ret = menunjukan gagal atau cerhasil
    if ret:
        cv2,imshow("display", image)
        if cv2.waitKey(50) == 27: #27 = tombol esc
            break
cv2.destroyAllWindows()