
#码垛代码

import cv2
import numpy as np
import serial

# 靶心相对坐标
xm = 170
ym = 163
# 红色阈值
redh1 = 0
reds1 = 41
redv1 = 0
redH1 = 21
redS1 = 255
redV1 = 255
redh2 = 156
reds2 = 10
redv2 = 145
redH2 = 255
redS2 = 255
redV2 = 255
# 蓝色阈值
blueh = 100
blues = 18
bluev = 0
blueH = 255
blueS = 255
blueV = 171
# 绿色阈值
greenh = 29
greens = 0
greenv = 8
greenH = 82
greenS = 128
greenV = 159


def nothing(x):
    pass

def imgmask(get,img):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # bgr转为hsv
    blur_img = cv2.blur(hsv_img, (7, 7))
    # print(hsv_img)
    # print(get)

    if get == '1':
        mask_red1 = cv2.inRange(hsv_img, (redh1,reds1,redv1), (redH1,redS1,redV1))  # 提取红色区域的掩膜
        mask_red2 = cv2.inRange(hsv_img, (redh2,reds2,redv2), (redH2,redS2, redV2))
        mask = cv2.bitwise_or(mask_red1, mask_red2)
    # cv2.imshow('red', mask_red)
    if get == '2':
        mask = cv2.inRange(hsv_img, (greenh,greens,greenv), (greenH, greenS,greenV))  # 提取绿色区域的掩膜
    # cv2.imshow('green', mask_green)
    if get == '3':
        mask = cv2.inRange(hsv_img, (blueh,blues,bluev), (blueH, blueS,blueV))  # 提取蓝色区域的掩膜
    # cv2.imshow('blue', mask_blue)
    #cv2.imshow('mask', mask)
    mask = cv2.erode(mask,(5,5),iterations=1)
    mask = cv2.dilate(mask,(5,5),iterations=1)
    #cv2.imshow('mask1',mask1)

    recognise_img = cv2.bitwise_and(img, img, mask=mask)  # 与计算，识别出物块的位置（三色
    cv2.imshow('recognise_img',recognise_img)
    return recognise_img

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

    data[1] = '%02d' % x_real
    data[3] = '%02d' % y_real
    #print(data)
    result = ''.join(data)
    return result



def gray(get, img):
    imgcopy = img.copy()
    mask_img = imgmask(get, imgcopy)
    # cv2.imshow('mask_img',mask_img)

    gray_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.blur(gray_img, (3, 3))
    # cv2.imshow('blur_img', blur_img)
    # dilate_img = cv2.dilate(canny_img, (5, 5), 5)  # 膨胀操作
    # cv2.imshow('dilate_img',dilate_img)

    # k=cv2.getTrackbarPos("thresh", "th_img")
    _, th_img = cv2.threshold(blur_img, 119, 255, cv2.THRESH_BINARY)  # 二值化
    # cv2.imshow('th_img', th_img)

    circles = cv2.HoughCircles(blur_img, cv2.HOUGH_GRADIENT, 1, 200, param1=100, param2=50, minRadius=50,
                               maxRadius=100)
    if circles is not None:
        circles = circles[0]
        # 圆心坐标为（i[0],i[1])，此处可能需要强制转换为整数
        for i in circles:
            x = int(i[0])
            y = int(i[1])
            # cv2.circle(imgcopy, (int(i[0]), int(i[1])), 2, (255, 255, 255), -1)
        print(x, y)
        # cv2.imshow('img', imgcopy)
        xtest2 = xtest1 = x
        ytest1 = ytest2 = y
        # print(th_img[y,x])
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
        ytrue = int((ytest1 + ytest2) / 2)
        cv2.circle(imgcopy, (xtrue, ytrue), 2, (220, 225, 0), -1)
        cv2.imshow('img', imgcopy)
        result = distan(xtrue, ytrue)
        return result




if __name__ == '__main__':
    cap=cv2.VideoCapture(0)
    # cv2.namedWindow("th_img")
    # cv2.createTrackbar("thresh", "th_img", 0, 255, nothing)
    datacode = ['1', '2', '3', '3', '2', '1']
    k = 0


    while True:
        _,img=cap.read()
        img = img[50:400,180:520]
        result=gray(datacode[k],img)
        #cv2.imshow('img',img)
        if result is not None:
            print(result)
            # input()
            # k+=1
        cv2.waitKey(1)

    cap.release()
    cv2.destroyWindow()

# if __name__=='__main__':
#     ser = serial.Serial('/dev/ttyAMA0', 115200)  # 打开串口设备
#     cap=cv2.VideoCapture(0)
#     i=1
#     while i:
#         _,img=cap.read()
#         result = gray(img)
#         cv2.imshow('img',img)
#         if result is not None:
#             ser.write(result.encode())
#             i=0
#         cv2.waitKey(1)
#     cap.release()
#     #cv2.destroyWindow()