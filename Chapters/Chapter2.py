import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)   # to blur the image
imgEdge = cv2.Canny(img, 150, 100)          # to detect edges
imgDilation = cv2.dilate(imgEdge, kernel, iterations= 1)   # to increase thickness of edge
imgErosion = cv2.erode(imgDilation, kernel, iterations= 1)  # to reduce thickness of edge

# cv2.imshow("image", img)
# cv2.imshow("gray image", imgGray)
# cv2.imshow("Blur image", imgBlur)
cv2.imshow("Edge detector", imgEdge)
cv2.imshow("Dilated image", imgDilation)
cv2.imshow("Eroded image", imgErosion)

cv2.waitKey(0)

