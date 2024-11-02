import cv2
#靶心识别切片img = img[50:400,180:520]

cap = cv2.VideoCapture(0)

while 1:
    _,img = cap.read()
    imgcut = img[240:400,200:400]
    cv2.imshow('img',img)
    cv2.waitKey(1)

cap.release()