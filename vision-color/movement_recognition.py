import cv2
import numpy as np

cap = cv2.VideoCapture(0)#摄像头的捕获
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

mog = cv2.createBackgroundSubtractorMOG2()

while True:
    ret,img = cap.read()
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度图像
    thresh,img_threshold=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)#图像二值化
    #去噪
    blur = cv2.GaussianBlur(img_gray,(3,3),5)
    fgmask = mog.apply(blur)

    #去除背景
    #fgmask =mog.apply(img)


    cv2.imshow("img1",img)
    cv2.imshow("img",blur)
    if cv2.waitKey(1) & 0xFF==27:
        break


cv2.destroyAllWindows()