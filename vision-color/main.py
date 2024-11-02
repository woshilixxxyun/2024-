import cv2
import numpy as np
import serial
import time
from pyzbar.pyzbar import decode
import a_color as cl
import vscode2 as code
import tuning_ as tu #靶心识别
#import bull_eye_ as tu #物块对准、码垛


ser = serial.Serial('/dev/ttyAMA0', 115200)#打开串口设备

data = ["0"]#储存二维码字符串
datacode = []#储存二维码字符串（无加号）

i=0#颜色识别位码
j=0#粗加工区位码
k=0#精加工区位码

res=['0']

while 1:
    size = ser.inWaiting()#读取缓冲区字符


    if size!=0:
        res[0]=ser.read(size)
        print(res[0])
        #识别颜色,如果识别到且停止，夹取 a_color.py
        #if res[0]==b'21' or res[0]==b'22' or res[0]==b'23':#识别颜色并检测发送
        if res[0]==b'2':
            cap = cv2.VideoCapture(2)
            while True:
                _, img = cap.read()
                #cv2.imshow('img',img)
                result = cl.stop(datacode[i],img)
                #print(result)
                if result is not None:
                    ser.write(result.encode())
                    print(result)
                    i+=1
                    res=['0']
                    cap.release()
                    break

                cv2.waitKey(1)

        #识别二维码（已完善完成）vscode2.py
        elif res[0]==b'1':
            cap = cv2.VideoCapture(0)

            while True:
                _, img = cap.read()
                #cv2.imshow('img', img)
                result=code.code(data,img)
                
                if result is not None:
                    datacode = list(result)
                    del datacode[3]
                    ser.write(result.encode())
                    print(result)
                    res=['0']
                    cap.release()
                    #cv2.destroyAllWindows()

                    break


                cv2.waitKey(1)
        #识别靶心粗加工 tuning_.py
        elif res[0]==b'3':
            cap = cv2.VideoCapture(2)
            while True:
                _, img = cap.read()
                #cv2.imshow('img',img)
                result = tu.process_bull(datacode[j],img)

                if result is not None:
                    ser.write(result.encode())
                    j+=1
                    res=['0']
                    cap.release()
                    break
                cv2.waitKey(1)

        #精加工 tuning_.py
        elif res[0]==b'4':
            cap = cv2.VideoCapture(2)
            while True:
                _,img = cap.read()
                result = tu.process_tu(datacode[k],img)
                if result is not None:
                    ser.write(result.encode())
                    k+=1
                    res = ['0']
                    cap.release()
                    break
                cv2.waitKey(1)

        #二轮夹取校准

    key = cv2.waitKey(1)

