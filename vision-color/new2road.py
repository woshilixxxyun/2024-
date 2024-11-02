import cv2

img1 = cv2.imread("D:/python 3.11.7/vision-color/photo/line1.jpg")
img2 = cv2.imread("D:/python 3.11.7/vision-color/photo/line2.jpg")

# 鼠标回调函数
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print("鼠标移动到位置：", x, y)
        # image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # print(image_gray)
        cv2.imshow('img',image)
        print(image[y,x])
        return x,y

# 创建一个窗口并设置鼠标回调函数
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

h1,w1,_ = img1.shape
h1_new = int(h1/5)
w1_new = int(w1/5)
# image = cv2.resize(img1,(w1_new,h1_new))
image = cv2.imread("D:/python 3.11.7/vision-color/photo/image1.png")
cv2.imshow('image',image)
cv2.waitKey(0)
# while True:
#     # 显示图像
#     _,image = cap.read()
#     cv2.imshow('image', image)
#
#     # 按下ESC键退出
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
#     cv2.waitKey(1)

# 销毁所有窗口
# cv2.destroyAllWindows()
