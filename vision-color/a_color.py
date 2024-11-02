#本代码将实现识别指定颜色物体并对其框选，从而确定其是否到达指定位置（物料颜色识别）
import time
import cv2
import numpy as np
import serial

cut_x=322
cut_y=191
cut_xw=332
cut_yw=201

# 红色阈值
redh1 = 0
reds1 = 0
redv1 = 0

redH1 = 25
redS1 = 255
redV1 = 255

# redh2 = 224
# reds2 = 46
# redv2 = 151
#
# redH2 = 81
# redS2 = 255
# redV2 = 255
# 蓝色阈值
blueh = 100
blues = 74
bluev = 46
blueH = 132
blueS = 255
blueV = 255
# 绿色阈值
greenh = 50
greens = 50
greenv = 50
greenH = 101
greenS = 255
greenV = 255

def recognise_color(get,img):#提取指定颜色区域的图片
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#bgr转为hsv
    blur_img = cv2.blur(hsv_img,(5,5))
    #print(hsv_img)
    #print(get)

    #使用if语句，如果传来1，表示应识别红色，将掩膜设置为红色阈值
    #if get==b'21':
    if get == '1':
        mask = cv2.inRange(blur_img, (redh1,reds1,redv1), (redH1,redS1,redV1))#提取红色区域的掩膜
        # mask2 = cv2.inRange(blur_img, (redh2,reds2,redv2), (redH2,redS2, redV2))
        # mask = cv2.bitwise_or(mask1,mask2)

    #elif get==b'22':
    elif get == '2':
        mask = cv2.inRange(blur_img, (greenh,greens,greenv), (greenH, greenS,greenV))  # 提取绿色区域的掩膜
    #elif get==b'23':
    elif get == '3':
        mask = cv2.inRange(blur_img, (blueh,blues,bluev), (blueH, blueS,blueV))  # 提取蓝色区域的掩膜
    mask = cv2.erode(mask,(5,5),iterations=1)
    #print(mask)
    cv2.imshow('mask',mask)
    #mask_erode=cv2.erode(mask,(5,5),iterations=3)
    #cv2.imshow('mask1', mask_erode)
    #mask_dilate=cv2.dilate(mask,(5,5),iterations=3)
    #mask=mask_dilate
    #cv2.imshow('mask2',mask_dilate)
    recognise_img=cv2.bitwise_and(img,img,mask=mask)#与计算
    if mask is not None:
        return recognise_img,mask

def stop(get,img):
    #print(get)
    recognise_img,mask = recognise_color(get,img)
    reccut = img[cut_y:cut_yw,cut_x:cut_xw]
    imgcut = mask[cut_y:cut_yw,cut_x:cut_xw]
    cv2.imshow('imgcut',imgcut)
    cv2.imshow('reccut',reccut)
    if np.all(imgcut==255):
        return 's'

#画边框
def outline(get,img,data):
    #print(img)
    recognise_img,mask=recognise_color(get, img)
    #print(recognise_img)
    imgContour=img.copy()#用于画图
    gray_img = cv2.cvtColor(recognise_img, cv2.COLOR_BGR2GRAY)  # 灰度图
    blur_img = cv2.GaussianBlur(gray_img, (9, 9), 1)  # 高斯滤波
    canny_img = cv2.Canny(blur_img, 100, 150)  # 边缘检测
    dilate_img = cv2.dilate(canny_img, (5,5), 2)  # 膨胀操作

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 寻找轮廓点

    s_x=190
    s_y=170
    e_x=400
    e_y=380
    #cv2.rectangle(imgContour, (s_x, s_y), (e_x, e_y), (255, 0, 225), 5)#绘制一个基准框，进入基准框返回succ

    for cnt in contours:
        area = cv2.contourArea(cnt)#计算面积
        if area>900:
            cv2.drawContours(imgContour,cnt,-1,(0,225,225),1)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 0, 0), 5)#画矩形边框
            #print(x,y,x+w,y+h)
            print(data[0],x)
            cv2.imshow('img', imgContour)
            x_r=200
            y_r=200
            if abs(int(data[0])-x)<10 and abs(int(data[1])-(x+w))<10:
                print('s')
                return 's'
            else:
                data[0]=x
                data[1]=x+w
                time.sleep(0.1)#

#二次夹取识别首颜色并校准
def catch(get,img):


            return result


if __name__=='__main__':
    cap = cv2.VideoCapture(0)
    i=0
    datacode = ['1','2','3','3','2','1']

    while True:
        _,img=cap.read()
        # img = img[50:400,180:520]

        cv2.imshow('img',img)
        #outline(get,img,data)
        result = stop(datacode[i],img)
        if result is not None:
            print(i,result)
            i+=1
        cv2.waitKey(1)

    cap.release()
    cv2.destroyWindow()





# if __name__=='__main__':
#     ser = serial.Serial('COM8', 115200)  # 打开串口设备
#     if ser.isOpen == False:
#         ser.open()  # 打开串口
#     a = ser.write(b'\x05')
#     print(a)
#     res = ['0']
#     while 1:
#         size = ser.inWaiting()
#         cap = cv2.VideoCapture(0)
#         if size!=0:
#             res[0]=ser.read(size)
#             print(res[0])
#             if res[0]==b'1':
#                 data=['0','0']
#                 while True:
#                     ret,img=cap.read()
#
#                     cv2.imshow('img', img)
#                     result=outline(res[0],img,data)
#                     if result is not None:
#                         if result=='s':
#                             print(result)
#                             ser.write(result.encode())
#                             break
#
#
#
#                     key = cv2.waitKey(1)
#
#     cap.release()
#     cv2.destroyAllWindows()