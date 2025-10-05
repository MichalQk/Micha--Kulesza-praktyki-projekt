import cv2
import numpy as np

img = cv2.imread('postac nr (7).png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def nothing(v): pass
cv2.namedWindow("podglad", cv2.WINDOW_NORMAL)
cv2.createTrackbar("blur", "podglad", 9, 31, nothing)
cv2.createTrackbar("t1", "podglad", 90, 255, nothing)
cv2.createTrackbar("t2", "podglad", 255, 255, nothing)

while True:
    b = cv2.getTrackbarPos("blur","podglad");  b = b if b%2==1 else b+1
    t1 = cv2.getTrackbarPos("t1","podglad")
    t2 = cv2.getTrackbarPos("t2","podglad")

    blur = cv2.GaussianBlur(gray, (max(3,b), max(3,b)), 0)
    edges = cv2.Canny(blur, t1, t2)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    vis = img.copy()
    cv2.drawContours(vis, contours, -1, (0,255,0), 2)

    cv2.imshow("podglad", vis)
    if cv2.waitKey(30) & 0xFF == 27: break

cv2.destroyAllWindows()
