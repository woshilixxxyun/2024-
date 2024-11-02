import cv2
import cv2 as cv
import numpy as np

#img2
# def line_detection(image):
#     h,w,_ = image.shape
#     w_new = int(w/5)
#     h_new = int(h/5)
#     image = cv2.resize(image,(w_new,h_new))
#     gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     blur = cv2.blur(gray,(3,3))
#     # cv2.imshow('img_blur',blur)
#     edges = cv.Canny(blur, 50, 150, apertureSize=3)#apertureSize,Canny边缘检测梯度那一步，窗口大小是3   apertureSize是sobel算子大小，只能为1,3,5，7
#     cv2.imshow('img',edges)
#     lines = cv.HoughLines(edges, 1, np.pi/180, 200) #函数将通过步长为1的半径和步长为π/180的角来搜索所有可能的直线
#     if lines is not None:
#         for line in lines:
#             print(type(lines))
#             rho, theta = line[0] #获取极值ρ长度和θ角度
#             a = np.cos(theta) #获取角度cos值
#             b = np.sin(theta)#获取角度sin值
#             x0 = a * rho #获取x轴值
#             y0 = b * rho #获取y轴值　　x0和y0是直线的中点
#             x1 = int(x0 + 1000 * (-b)) #获取这条直线最大值点x1
#             y1 = int(y0 + 1000 * (a)) #获取这条直线最大值点y1
#             x2 = int(x0 - 1000 * (-b)) #获取这条直线最小值点x2
#             y2 = int(y0 - 1000 * (a)) #获取这条直线最小值点y2　　其中*1000是内部规则
#             cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2) #开始划线
#     cv.imshow("image_lines", image)

# img1
def line_detection(image):
    h,w,_ = image.shape
    w_new = int(w/5)
    h_new = int(h/5)
    image = cv2.resize(image,(w_new,h_new))
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv2.blur(gray,(3,3))
    # cv2.imshow('img_blur',blur)
    _,th = cv2.threshold(blur,156,255,cv2.THRESH_TOZERO)
    print(th)
    cv2.imshow("th",th)
    edges = cv.Canny(th, 140,200, apertureSize=3)#apertureSize,Canny边缘检测梯度那一步，窗口大小是3   apertureSize是sobel算子大小，只能为1,3,5，7
    cv2.imshow('img',edges)
    lines = cv.HoughLines(edges, 1, np.pi/180, 100) #函数将通过步长为1的半径和步长为π/180的角来搜索所有可能的直线
    if lines is not None:
        for line in lines:
            # print(type(lines))
            rho, theta = line[0] #获取极值ρ长度和θ角度
            a = np.cos(theta) #获取角度cos值
            b = np.sin(theta)#获取角度sin值
            x0 = a * rho #获取x轴值
            y0 = b * rho #获取y轴值　　x0和y0是直线的中点
            x1 = int(x0 + 1000 * (-b)) #获取这条直线最大值点x1
            y1 = int(y0 + 1000 * (a)) #获取这条直线最大值点y1
            x2 = int(x0 - 1000 * (-b)) #获取这条直线最小值点x2
            y2 = int(y0 - 1000 * (a)) #获取这条直线最小值点y2　　其中*1000是内部规则
            cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2) #开始划线
    cv.imshow("image_lines", image)

src = cv.imread("D:/python 3.11.7/vision-color/photo/line.png")  #读取图片位置
img1 = cv2.imread('D:/python 3.11.7/vision-color/photo/line1.jpg')
img2 = cv2.imread('D:/python 3.11.7/vision-color/photo/line2.jpg')
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
# line_detection(src)
line_detection(img1)
cv.waitKey(0)
cv.destroyAllWindows()

