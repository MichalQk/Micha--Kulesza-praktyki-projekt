

#notatka -> zmienic zdjecie monet, bo moje jest dosc średnie.


import cv2
import numpy as np

#wczytje z pliku + przeksztalca obraz na szary zeby lepiej sie i szybciej szczytywalo
img = cv2.imread("coins.png")

#na szarosc przesztalca
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(7,7),0)
canny = cv2.Canny(blur, 90, 255)

#funkcje programu

countours,hierarchy = cv2.findContours(canny.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, countours, -1, (0,255,0), 2)

sortenCon = sorted(countours, key=cv2.contourArea)

#zliczanie tych zakreslen

for i,cont in enumerate(sortenCon):
    x,y,w,h = cv2.boundingRect(cont)
    print(i)
    print(x,y,w,h)

    X = x + int(w/2)
    Y = y + int(h/2)

    img = cv2.circle(img,(x,y),int(w/2),(255,0,0),2)
    img = cv2.putText(img = img, text=str(i), org=(X,Y), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(255,255,255), thickness=1)


#otwiera plik szczyta info, czeka na dowolny klawisz i usuwa
cv2.imshow("original image",img)
# cv2.imshow("canny image",canny)

cv2.imshow("gray",blur)
cv2.waitKey(0)
print("Zamknieto program")
cv2.destroyAllWindows()


