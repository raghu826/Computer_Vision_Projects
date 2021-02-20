import cv2
import numpy as np

img = np.zeros((400, 400, 3), np.uint8)

cv2.line(img, (0, 0), (150, 100), (0, 255, 0), 2)
cv2.line(img, (150, 100), (150, 400), (0, 255, 255), 2)
cv2.rectangle(img, (0, 100), (200, 300), (100, 200, 300), 1)
cv2.circle(img, (300,200), 30, (150, 50, 250), 2)
cv2.putText(img, "Raghu", (250, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (140, 240, 40), 3)

cv2.imshow("Image", img)
cv2.waitKey(0)
