import cv2
import numpy as np

cap = cv2.VideoCapture(0)
def nothing(x):
    pass

cv2.namedWindow("frame")
cv2.createTrackbar("H1","frame",0,255,nothing)
cv2.createTrackbar("S1","frame",0,225,nothing)
cv2.createTrackbar("V1","frame",0,225,nothing)

cv2.createTrackbar("H2","frame",255,255,nothing)
cv2.createTrackbar("S2","frame",255,255,nothing)
cv2.createTrackbar("V2","frame",255,255,nothing)

img_hsv = np.zeros((250,500,3),np.uint8)

while True:
    h1 = cv2.getTrackbarPos("H1","frame")
    s1 = cv2.getTrackbarPos("S1", "frame")
    v1 = cv2.getTrackbarPos("V1","frame")

    h2 = cv2.getTrackbarPos("H2", "frame")
    s2 = cv2.getTrackbarPos("S2", "frame")
    v2 = cv2.getTrackbarPos("V2", "frame")

    _,img=cap.read()
    #img = img[50:400, 180:520]
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # bgr转为hsv
    mask = cv2.inRange(hsv_img, (h1, s1, v1), (h2, s2, v2))  # 提取绿色区域的掩膜
    recognise_img = cv2.bitwise_and(img, img, mask=mask)  # 与计算
    cv2.imshow('img',mask)
    cv2.imshow("frame",recognise_img)
    key = cv2.waitKey(1)
    if key ==27:
        break

cv2.destroyWindow()


