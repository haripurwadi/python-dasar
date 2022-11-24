import numpy as np
import cv2

cap = cv2.VideoCapture("http://192.168.43.1:8080/video") # membaca kamera HP
#instal ipwebcam dari playstore, jalankan, klik star server

while(True):
     ret, frame = cap.read()

     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     negatif = (255 - gray)

     brightness = (frame + 25)

     cv2.imshow('Gambar Asli' ,frame)
     cv2.imshow('Mengganti Brightness' ,brightness)
     cv2.imshow('frame' ,gray)
     cv2.imshow('invert' ,negatif)
     if cv2.waitKey(1) & 0xFF == ord('w'):
           break

cap.release()
cv2.destroyAllWindow()