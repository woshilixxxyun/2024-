import cv2
import numpy as np


cap = cv2.VideoCapture(0)

# 鼠标回调函数
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print("鼠标位置：", x, y)


# 创建一个窗口并设置鼠标回调函数
cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_callback)

while True:
    # 显示图像
    _,img = cap.read()
    #img = img[50:400,180:520]
    cv2.imshow('img', img)

    # 按下ESC键退出
    if cv2.waitKey(20) & 0xFF == 27:
        break

# 销毁所有窗口
cv2.destroyAllWindows()
