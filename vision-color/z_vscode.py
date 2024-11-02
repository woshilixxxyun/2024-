import cv2
from pyzbar.pyzbar import decode
import serial

def code(data,img):
    imgCopy=img.copy()
    QR_code = decode(imgCopy)

    for QR in QR_code:
        QR_data = QR.data.decode("utf-8")

        if (QR_data!=data[-1]):
            data[-1] = QR_data


        point = QR.rect

        cv2.rectangle(imgCopy,(point[0],point[1]),(point[0]+point[2],point[1]+point[3]),(0,200,255),5)
        cv2.imshow('img', imgCopy)

if __name__=='__main__':
    ser = serial.Serial('/dev/ttyAMA0', 9600)  # 打开串口设备
    if ser.isOpen == False:
        ser.open()  # 打开串口
    a = ser.write(b'\x05')
    cap = cv2.VideoCapture(0)
    data = ["0"]
    while 1:
        success, img = cap.read()
        code(data,img)
        #cv2.imshow('img',img)
        if data[0]!=0:
            ser.write(data)

        key=cv2.waitKey(1)
        if key==27:
            break
    cap.release()
    cv2.destroyAllWindows()

