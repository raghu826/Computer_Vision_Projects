import cv2

img = cv2.imread("Resources/lambo.png")
print("original image shape", img.shape)

imgResize = cv2.resize(img, (300, 200))
print("resized shape", imgResize.shape)

imgCropped = img[85:400, 60:510]


cv2.imshow("original Image", img)
# cv2.imshow("resized image", imgResize)
cv2.imshow("cropped image", imgCropped)
cv2.waitKey(0)
