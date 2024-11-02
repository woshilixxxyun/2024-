import cv2
import numpy as np
import a_color as cl

# 读取图像
cap = cv2.VideoCapture(2)


get=b'22'
data=['0','0']
while 1:
    _,img=cap.read()
    img=img[80:350,180:500]
    cv2.imshow('img',img)
    cl.outline(get,img,data)

    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()