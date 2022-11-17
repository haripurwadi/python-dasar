#baca video youtube
import cv2 # menyertakan library cv2 dari opencv
import pafy

url ='https://www.youtube.com/watch?v=iXkDUVk961U'
vpafy = pafy.new(url)
play = vpafy.getbest(preftype="mp4")
cap = cv2.VideoCapture(play.url)

while True:
    ret, image =cap.read()
    height, width, layers = image.shape
    new_h = int(height/1)
    new_w =int(width/1)
    resize = cv2.resize(image, (new_w, new_h))
    

    cv2.imshow("display", resize)
    if cv2.waitKey(5) == 27:
        break
cv2.destroyAllWindows()
cap.release()






