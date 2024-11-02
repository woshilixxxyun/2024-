import time
import cv2
import numpy as np
import serial

def set(img):#提取三色颜色区域的图片
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#bgr转为hsv
    blur_img = cv2.blur(hsv_img,(3,3))
    #print(hsv_img)
    #print(get)
    #使用if语句，如果传来1，表示应识别红色，将掩膜设置为红色阈值

    mask_red1 = cv2.inRange(hsv_img, (156, 43, 46), (180, 225, 225))#提取红色区域的掩膜
    mask_red2 = cv2.inRange(hsv_img,(0, 43, 46),(10, 225, 225))
    mask_red = cv2.bitwise_or(mask_red1,mask_red2)
    cv2.imshow('red',mask_red)
    mask_green = cv2.inRange(hsv_img, (35, 43, 46), (77, 225, 225))  # 提取绿色区域的掩膜
    cv2.imshow('green',mask_green)
    mask_rg=cv2.bitwise_or(mask_red,mask_green)
    mask_blue = cv2.inRange(hsv_img, (100, 43, 46), (124, 255, 255))  # 提取蓝色区域的掩膜
    cv2.imshow('blue',mask_blue)
    mask=cv2.bitwise_or(mask_rg,mask_blue)
    mask = cv2.erode(mask,(5,5),iterations=1)
    #cv2.imshow('mask',mask)

    recognise_img = cv2.bitwise_and(img, img, mask=mask)  # 与计算，识别出物块的位置（三色
    #cv2.imshow('recognise_img',recognise_img)

    imgContour = img.copy()  # 用于画图
    gray_img = cv2.cvtColor(recognise_img, cv2.COLOR_BGR2GRAY)  # 灰度图
    blur_img = cv2.GaussianBlur(gray_img, (9, 9), 1)  # 高斯滤波
    canny_img = cv2.Canny(blur_img, 100, 150)  # 边缘检测
    #cv2.imshow('canny',canny_img)

    dilate_img = cv2.dilate(canny_img, (5, 5), 2)  # 膨胀操作
    #cv2.imshow('dilate',dilate_img)

    contours, hierarchy = cv2.findContours(dilate_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 寻找轮廓点

    s_x = 190
    s_y = 170
    e_x = 400
    e_y = 380
    #cv2.rectangle(imgContour, (s_x, s_y), (e_x, e_y), (255, 0, 225), 5)  # 绘制一个基准框，进入基准框返回succ

    for cnt in contours:
        area = cv2.contourArea(cnt)  # 计算面积
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (0, 225, 225), 1)
            x, y, w, h = cv2.boundingRect(cnt)#定位
            print(w,h)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 0, 0), 5)#绘制矩形框
            cv2.imshow('img',imgContour)
    #以下代码放在这里保存一下


if __name__=='__main__':
    cap=cv2.VideoCapture(1)


    while True:
        _,img=cap.read()
        cv2.imshow('img', img)
        set(img)


        key=cv2.waitKey(1)
        if key==27:
            break
    cap.release()
    cv2.destroyWindow()