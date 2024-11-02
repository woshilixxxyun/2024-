# -*- coding: utf-8 -*-
import serial
import time
ser = serial.Serial('/dev/ttyAMA0', 115200) #打开串口设备
if ser.isOpen == False:
    ser.open()          # 打开串口
a=ser.write(b"x09")
print(a)
try:
    while True:
        size = ser.inWaiting()  	# 获得缓冲区字符
        if size != 0:
            res = ser.read(size)   	# 读取内容并显示
            print(res)
            print(ser.bytesize) #字节大小
            if res == b'\x01\r\n':
                ser.write(b'\x05')
                print(ser.baudrate) #波特率
            elif res == b'\x02':
                ser.write(b'\x06')
                print(ser.baudrate) #波特率
            elif res == b'\x03':
                ser.write(b'\x07')
                print(ser.baudrate) #波特率
            elif res == b'\x04':
                ser.write(b'\x08')
                print(ser.baudrate) #波特率
            ser.flushInput()		# 情况接收缓存区
            time.sleep(0.5)			# 软件延时
except KeyboardInterrupt:
    ser.close()
