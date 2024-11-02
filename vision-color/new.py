import cv2

cap = cv2.VideoCapture(0)
# 鼠标回调函数
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print("鼠标移动到位置：", x, y)





# 创建一个窗口并设置鼠标回调函数
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    # 显示图像
    _,image = cap.read()
    cv2.imshow('image', image)

    # 按下ESC键退出
    if cv2.waitKey(20) & 0xFF == 27:
        break
    cv2.waitKey(1)

# 销毁所有窗口
cv2.destroyAllWindows()
