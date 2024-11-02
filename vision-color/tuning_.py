
#靶心识别代码

import cv2
import numpy as np
import matplotlib.pyplot as plt
import serial

xm = 167
ym = 184


# 红色阈值
redh13 = 0
reds13 = 29
redv13 = 0
redH13 = 55
redS13 = 255
redV13 = 255
# redh23 = 225
# reds23 = 225
# redv23 = 225
# redH23 = 255
# redS23 = 255
# redV23 = 255
# 蓝色阈值
blueh3 = 100
blues3 = 18
bluev3 = 0
blueH3 = 255
blueS3 = 255
blueV3 = 171
# 绿色阈值
greenh3 = 40
greens3 = 0
greenv3 = 32
greenH3 = 80
greenS3 = 255
greenV3 = 136


# 红色阈值
redh14 = 0
reds14 = 0
redv14 = 0
redH14 = 63
redS14 = 255
redV14 = 255
redh24 = 225
reds24 = 225
redv24 = 225
redH24 = 255
redS24 = 255
redV24 = 255
# 蓝色阈值
blueh4 = 100
blues4 = 18
bluev4 = 0
blueH4 = 255
blueS4 = 255
blueV4 = 171
# 绿色阈值
greenh4 = 37
greens4 = 0
greenv4 = 32
greenH4 = 96
greenS4 = 255
greenV4 = 225

def nothing(x):
    pass

#cv2.namedWindow("Thresh")
#cv2.createTrackbar("thresh","Thresh",0,255,nothing)

def outline(get,img):
    recognise_img = imgmask(get, img)
    # print(recognise_img)
    height,width,_=img.shape
    img_draw = np.zeros((height, width, 3), dtype=np.uint8)
    gray_img = cv2.cvtColor(recognise_img, cv2.COLOR_BGR2GRAY)  # 灰度图
    blur_img = cv2.GaussianBlur(gray_img, (7, 7), 1)  # 高斯滤波
    canny_img = cv2.Canny(blur_img, 100, 150)  # 边缘检测
    dilate_img = cv2.dilate(canny_img, (5, 5), 1)  # 膨胀操作

    contours, hierarchy = cv2.findContours(dilate_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 寻找轮廓点


    for cnt in contours:
        area = cv2.contourArea(cnt)  # 计算面积
        if area > 900:
            cv2.drawContours(img_draw, cnt, -1, (255, 225, 225), 5)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.imshow('img_draw',img_draw)

def distan(xtrue,ytrue):
    data=[None]*4
    #计算相差的像素(相对原点 - 测出的圆心）
    x_pixel = xm - xtrue
    y_pixel = ym - ytrue
    # 转换为现实中的距离
    x_real = int(x_pixel / 2)
    y_real = int(y_pixel / 2)
    # 判断走的方向
    if x_real > 2:
        data[0] = 'L'  # 左
    else:
        data[0] = 'R'  # 右
        x_real = abs(x_real)
    if y_real > 2:
        data[2] = 'U'  # 前
    else:
        data[2] = 'D'  # 后
        y_real = abs(y_real)

    if x_real < 2:
        x_real = 0
    if y_real < 2:
        y_real = 0

    data[1] = '%03d' % x_real
    data[3] = '%03d' % y_real
    #print(data)
    result = ''.join(data)
    return result

def imgmask3(get,img):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # bgr转为hsv
    blur_img = cv2.blur(hsv_img, (7, 7))
    # print(hsv_img)
    # print(get)

    if get == '1':
        mask = cv2.inRange(hsv_img, (redh13, reds13, redv13), (redH13, redS13, redV13))  # 提取红色区域的掩膜
        # mask_red1 = cv2.inRange(hsv_img, (redh13,reds13,redv13), (redH13,redS13,redV13))  # 提取红色区域的掩膜
        # mask_red2 = cv2.inRange(hsv_img, (redh23,reds23,redv23), (redH23,redS23, redV23))
        # mask = cv2.bitwise_or(mask_red1, mask_red2)
    # cv2.imshow('red', mask_red)
    if get == '2':
        mask = cv2.inRange(hsv_img, (greenh3,greens3,greenv3), (greenH3, greenS3,greenV3))  # 提取绿色区域的掩膜
    # cv2.imshow('green', mask_green)
    if get == '3':
        mask = cv2.inRange(hsv_img, (blueh3,blues3,bluev3), (blueH3, blueS3,blueV3))  # 提取蓝色区域的掩膜
    # cv2.imshow('blue', mask_blue)
    #cv2.imshow('mask', mask)
    #mask = cv2.erode(mask,(5,5),iterations=2)
    mask = cv2.dilate(mask,(5,5),iterations=2)
    #cv2.imshow('mask1',mask1)

    recognise_img = cv2.bitwise_and(img, img, mask=mask)  # 与计算，识别出物块的位置（三色
    cv2.imshow('recognise_img',recognise_img)
    return recognise_img

def imgmask4(get,img):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # bgr转为hsv
    blur_img = cv2.blur(hsv_img, (7, 7))
    # print(hsv_img)
    # print(get)

    if get == '1':
        mask_red1 = cv2.inRange(hsv_img, (redh14,reds14,redv14), (redH14,redS14,redV14))  # 提取红色区域的掩膜
        mask_red2 = cv2.inRange(hsv_img, (redh24,reds24,redv24), (redH24,redS24, redV24))
        mask = cv2.bitwise_or(mask_red1, mask_red2)
    # cv2.imshow('red', mask_red)
    if get == '2':
        mask = cv2.inRange(hsv_img, (greenh4,greens4,greenv4), (greenH4, greenS4,greenV4))  # 提取绿色区域的掩膜
    # cv2.imshow('green', mask_green)
    if get == '3':
        mask = cv2.inRange(hsv_img, (blueh4,blues4,bluev4), (blueH4, blueS4,blueV4))  # 提取蓝色区域的掩膜
    # cv2.imshow('blue', mask_blue)
    #cv2.imshow('mask', mask)
    #mask = cv2.erode(mask,(5,5),iterations=2)
    mask = cv2.dilate(mask,(5,5),iterations=2)
    #cv2.imshow('mask1',mask1)

    recognise_img = cv2.bitwise_and(img, img, mask=mask)  # 与计算，识别出物块的位置（三色
    cv2.imshow('recognise_img',recognise_img)
    return recognise_img

#靶心微调
def process_bull(get,img):
    imgcopy = img.copy()
    mask_img = imgmask3(get,imgcopy)
    # cv2.imshow('mask_img',mask_img)

    gray_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.blur(gray_img, (3, 3))
    #cv2.imshow('blur_img', blur_img)
    # dilate_img = cv2.dilate(canny_img, (5, 5), 5)  # 膨胀操作
    # cv2.imshow('dilate_img',dilate_img)

    # k=cv2.getTrackbarPos("thresh", "th_img")
    _, th_img = cv2.threshold(blur_img, 119, 255, cv2.THRESH_BINARY)  # 二值化
    #cv2.imshow('th_img', th_img)

    circles = cv2.HoughCircles(blur_img, cv2.HOUGH_GRADIENT, 1, 200, param1=200, param2=50, minRadius=50, maxRadius=200)
    if circles is not None:
        circles = circles[0]
        # 圆心坐标为（i[0],i[1])，此处可能需要强制转换为整数
        for i in circles:
            x = int(i[0])
            y = int(i[1])
            cv2.circle(imgcopy, (int(i[0]), int(i[1])), 2, (255, 255, 255), -1)
        # print(x, y)
        cv2.imshow('img', imgcopy)
        xtest2 = xtest1 = x
        ytest1 = ytest2 = y
        print(th_img[y,x])
        height, width = imgcopy.shape[:2]
        while True:  # 筛选x
            if th_img[y, xtest1] == 0 and th_img[y, xtest2] == 0:
                xtest1 += 1
                xtest2 -= 1
            elif th_img[y, xtest1] == 0 and th_img[y, xtest2] != 0:
                xtest1 += 1
            elif th_img[y, xtest1] != 0 and th_img[y, xtest2] == 0:
                xtest2 -= 1
            else:
                break
            if xtest2>=width or xtest1>=width:
                xtest2 = xtest1 = x
                break
        xtrue = int((xtest1 + xtest2) / 2)
        # print(xtrue)
        while True:  # 筛选y
            if th_img[ytest1, xtrue] == 0 and th_img[ytest2, xtrue] == 0:
                ytest1 += 1
                ytest2 -= 1
            elif th_img[ytest1, xtrue] == 0 and th_img[ytest2, xtrue] != 0:
                ytest1 += 1
            elif th_img[ytest1, xtrue] != 0 and th_img[ytest2, xtrue] == 0:
                ytest2 -= 1
            else:
                break
            if ytest2 >= height or ytest1 >= height:
                ytest2 = ytest1 = y
                break
        ytrue = int((ytest1 + ytest2) / 2)
        cv2.circle(imgcopy, (xtrue, ytrue), 10, (220, 225, 0), -1)
        print(xtrue,ytrue)
        cv2.imshow('img', imgcopy)
        result = distan(x, y)
        return result

#码垛微调
def process_tu(get,img):
    imgcopy = img.copy()
    mask_img = imgmask(get,imgcopy)
    # cv2.imshow('mask_img',mask_img)

    gray_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.blur(gray_img, (3, 3))
    #cv2.imshow('blur_img', blur_img)
    # dilate_img = cv2.dilate(canny_img, (5, 5), 5)  # 膨胀操作
    # cv2.imshow('dilate_img',dilate_img)

    # k=cv2.getTrackbarPos("thresh", "th_img")
    _, th_img = cv2.threshold(blur_img, 119, 255, cv2.THRESH_BINARY)  # 二值化
    #cv2.imshow('th_img', th_img)

    circles = cv2.HoughCircles(blur_img, cv2.HOUGH_GRADIENT, 1, 200, param1=200, param2=50, minRadius=50, maxRadius=200)
    if circles is not None:
        circles = circles[0]
        # 圆心坐标为（i[0],i[1])，此处可能需要强制转换为整数
        for i in circles:
            x = int(i[0])
            y = int(i[1])
            cv2.circle(imgcopy, (int(i[0]), int(i[1])), 2, (255, 255, 255), -1)
        # print(x, y)
        cv2.imshow('img', imgcopy)
        xtest2 = xtest1 = x
        ytest1 = ytest2 = y
        # print(th_img[y,x])
        while True:  # 筛选x
            if th_img[y, xtest1] != 0 and th_img[y, xtest2] != 0:
                xtest1 += 1
                xtest2 -= 1
            elif th_img[y, xtest1] != 0 and th_img[y, xtest2] == 0:
                xtest1 += 1
            elif th_img[y, xtest1] == 0 and th_img[y, xtest2] != 0:
                xtest2 -= 1
            else:
                break
        xtrue = int((xtest1 + xtest2) / 2)
        # print(xtrue)
        while True:  # 筛选y
            if th_img[ytest1, xtrue] != 0 and th_img[ytest2, xtrue] != 0:
                ytest1 += 1
                ytest2 -= 1
            elif th_img[ytest1, xtrue] != 0 and th_img[ytest2, xtrue] == 0:
                ytest1 += 1
            elif th_img[ytest1, xtrue] == 0 and th_img[ytest2, xtrue] != 0:
                ytest2 -= 1
            else:
                break
        ytrue = int((ytest1 + ytest2) / 2)
        cv2.circle(imgcopy, (xtrue, ytrue), 2, (220, 225, 0), -1)
        print(xtrue,ytrue)
        cv2.imshow('img', imgcopy)
        result = distan(xtrue, ytrue)
        return result


if __name__=='__main__':
    #cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    # img = cv2.imread("photo/bull2.png")
    #ser = serial.Serial('/dev/ttyAMA0', 115200)  # 打开串口设备
    cap = cv2.VideoCapture(0)
    #cv2.namedWindow("img",cv2.WINDOW_NORMAL)
    #img = cv2.imread("photo/bull2.png")

    # cv2.namedWindow("th_img")
    # cv2.createTrackbar("thresh", "th_img", 0, 255, nothing)
    datacode = ['1','2','3','3','2','1']
    j=0

    while 1:
        ret,img=cap.read()
        img = img[50:400,180:520]
        cv2.imshow('img',img)
        #result=bull(img)
        result = process_bull(datacode[j],img)
        if result is not None :
            print(j,result)
            # input()
            # j+=1




        cv2.waitKey(1)


# if __name__=='__main__':
#     cap = cv2.VideoCapture(0)
#     ser = serial.Serial('/dev/ttyAMA0', 115200)  # 打开串口设备
#
#     datacode = ['1', '2', '3', '3', '2', '1']
#     j=0
#     res = ['0']
#     while True:
#         size = ser.inWaiting()
#         if size != 0:
#             res[0] = ser.read(size)
#             print(res[0])
#             if res[0]==b'3':
#                 while 1:
#                     _,img = cap.read()
#                     cv2.imshow('img',img)
#                     result = process(datacode[j],img)
#                     if result is not None:
#                         ser.write(result.encode())
#                         j+=1
#                         res[0]='0'
#                     cv2.waitKey(1)
#
#     cv2.destroyWindow()