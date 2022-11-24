#dnn untuk blob citra

import cv2
import numpy as np

net = cv2.dnn.readNetFromCaffe("deploy.prototxt","res10_300x300_ssd_iter_140000.caffemodel") #model dari using a reduced ResNet-10 model

image= cv2.imread("foto1.jpg")
(h,w) = image.shape[ :2] #mengambil image array 0 da array 1
#h = image.shape[0]
#w = image.shape[1]

blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (103.93, 116.77, 123.68))
net.setInput(blob)
detections = net.forward()

for i in range(0, detections.shape[2]):
    confidence = detections[0,0,i,2]
    if confidence > 0.5:
        box = detections [0,0,i,3:7]*np.array([w,h,w,h]) #lokasi kotak pada image 300x300
        (startX, startY, endX, endY) = box.astype("int")
        cv2.rectangle(image, (startX, startY), (endX, endY), (0,255,0), 3) #membuat kotak
        
cv2.imshow("display", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
        
                              

                             
 