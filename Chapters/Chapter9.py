import cv2

faceCascade= cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread('Resources/lena.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray, 1.1, 4)

font = cv2.FONT_HERSHEY_SIMPLEX

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 150, 255), 2)

cv2.imshow('img', img)

cv2.waitKey()

print("completed")
