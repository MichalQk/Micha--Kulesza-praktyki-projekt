import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#warunek ogarnąłem. + wyjątki mieliśmy juz omawiane
img = cv2.imread("face.jpg")
if img is None:
    raise Exception("Nie znaleziono obrazka")


faces = face_cascade.detectMultiScale(img, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

#wyświetlenie i załadowanie obrazka w oknie.
cv2.imshow("face", img)


#zapmiętąłem na pamięć. w skrócie klikasz ESC i wychodzisz. przydatne.
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()


#spraswdzam poprawnosc zaladowania i dzialania programu. -> False

print(face_cascade.empty())


print(cv2.__version__)
