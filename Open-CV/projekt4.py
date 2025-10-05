#skanowanie kodu QR
#Projekt nr 4.
#polecam odpalić kamerkę z kodem qr aby program załapał



import cv2
import numpy as np
import time


#ustawienia kamerki
cam = cv2.VideoCapture(2)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

detector = cv2.QRCodeDetector()

while cam.isOpened():
    succes,img = cam.read()
    start = time.perf_counter() #zlicza jak dlugo nam to zajmie.
    value,points,qrcode = detector.detectAndDecode(img)

    if value !="":
        x1 = points[0][0][0]
        y1 = points[0][0][1]
        x2 = points[0][2][0]
        y2 = points[0][2][1]


        cv2.rectangle(img, (int(x1),(int(y1)),(int(x2)), int(y2)) , (0,255,0),3)
        cv2.putText(img, str(value),(30,120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    end = time.perf_counter()
    totalTime = end-start
    # fps = 1/totalTime

    # cv2.putText(img, f'FPS: {int(fps)}', (30,70),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    cv2.imshow("face", img)

    if cv2.waitKey(1) & 0xFF == 27: #ESC
        break

    cam.release()
    cv2.destroyAllWindows()


#mozna by bylo zrobić tez, x_center , y_center ale poczytałem ze przy jednej kamerze nie ma to sensu. (nie jes to potrzebne)
#Wtedy wywywałbym funkcję cv2.circle()