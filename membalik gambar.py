#membalik gambar video
import cv2 # menyertakan library cv2 dari opencv
import time

camera=cv2.VideoCapture("http://192.168.43.1:8080/video") # membaca kamera HP
#instal ipwebcam dari playstore, jalankan, klik star server
while True: #selelu diakhiri dengan tanda :
    ret, image = camera.read() #ret = menunjukan gagal atau cerhasil
    if ret:
        #image=cv2.flip(image,0) # sama tidak di flip
        #image=cv2.rotate(image,rotateCode=cv2.ROTATE_90_CLOCKWISE) #rotasi
        #image=cv2.resize(image, (200,200)) #tanpa pertimbangan
        
        faktor = 0.5
        image=cv2.resize(image, None, fx=faktor, fy=faktor) #rezize dengan penskalaan
        cv2.imshow("display", image)
        if cv2.waitKey(50) == 27: #27 = tombol esc
            break
cv2.destroyAllWindows()
camera.release()
