import cv2
from pyzbar.pyzbar import decode
import serial


def code(data,img):
    #imgCopy=img.copy()
    QR_code = decode(img)

    for QR in QR_code:
        QR_data = QR.data.decode("utf-8")

        if (QR_data!=data[-1]):
            data[-1] = QR_data
            result = ''.join(data)
            #print(result)
            #ser.write(result.encode())
            return result


        

# if __name__=='__main__':
#     cap = cv2.VideoCapture(0)
#     ser = serial.Serial('COM8', 115200)  # 打开串口设备
#     if ser.isOpen == False:
#         ser.open()  # 打开串口
#     a = ser.write(b'\x05')
#     print(a)
#     while True:
#         size = ser.inWaiting()
#         cap = cv2.VideoCapture(0)
#         if size!=0:
#             res=ser.read(size)
#             print(res)
#             if res==b'1':
#                 form=ser.inWaiting()
#                 if form!=0:
#                     ret=ser.read(form)
#                     print(ret)
#                     while True:
#                         data=[0]
#                         success, img = cap.read()
#                         result = code(data,img)
#                         if result is not None:
#                             ser.write(result.encode())
#                             result=None
#
#                             break
#                         #cv2.imshow('img',img)
#
#                         #ser.write(b'\x01')
#
#
#                         key=cv2.waitKey(1)
#                         if key==27:
#                             break
#         print('1')
#     cap.release()
#     cv2.destroyAllWindows()

if __name__=='__main__':
    cap = cv2.VideoCapture(0)
    data = ['0']
    datacode = []

    while True:
        _,img = cap.read()
        result = code(data,img)
        if result is not None:
            datacode = list(result)
            del datacode[3]
            print(datacode)
            break
        key=cv2.waitKey(1)

    cap.release()
    cv2.destroyWindow()
