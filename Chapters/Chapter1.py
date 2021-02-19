import cv2

# To read a IMAGE
img = cv2.imread("images/lena.png")
cv2.imshow("output", img)
# 0 means infinite amount of time n 1 means one millisecond
cv2.waitKey(0)


# To READ A VIDEO
video = cv2.VideoCapture("Resources/test_video.mp4")
frameWidth = 640  # video width
frameHeight = 480
while True:
    success, img = video.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("output", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break


#  Web Cam
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)  # default value for web cam
cap.set(3, frameWidth)     # 3 represents width
cap.set(4, frameHeight)    # 4 represents Height
cap.set(10, 50)            # 10 gives brightness

while True:
    success, img = cap.read()   # success is a boolean value
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

