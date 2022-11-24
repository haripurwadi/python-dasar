#konversi gambar video
import cv2 # menyertakan library cv2 dari opencv
import time
(512, 512, 3)
camera=cv2.VideoCapture("video\\TownCentreXVID.avi") # membaca kamera HP
#instal ipwebcam dari playstore, jalankan, klik star server
while True: #selelu diakhiri dengan tanda :
    ret, image = camera.read() #ret = menunjukan gagal atau cerhasil
    if ret:
        #menulis teks
        print(image.shape[1])
        cv2.putText(image,"HELLO", (100,100), cv2.FONT_HERSHEY_SIMPLEX,4, (0,0,255), 12)
        cv2.circle(image, (int(image.shape[1]/2), int(image.shape[0]/2)), 100, (0,255,0), 3)
        #image=cv2.flip(image,0) # sama tidak di flip
        #image=cv2.rotate(image,rotateCode=cv2.ROTATE_90_CLOCKWISE) #rotasi
        #image=cv2.resize(image, (200,200)) #tanpa pertimbangan
        
        faktor = 0.5
        image=cv2.resize(image, None, fx=faktor, fy=faktor) #rezize dengan penskalaan
        #image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow("display", image)
        if cv2.waitKey(10) == 27: # delay 10 detik, 27 = tombol esc
            break

cv2.imwrite("demo.jpg", image)
cv2.destroyAllWindows()
camera.release()



