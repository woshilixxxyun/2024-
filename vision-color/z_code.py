import cv2
from pyzbar.pyzbar import decode

#img = cv2.imread("test QR code/123+321.png")
cap = cv2.VideoCapture(0)

data = ["0"]

while True:
    success,img = cap.read()
    QR_code = decode(img)


    for QR in QR_code:
        QR_data = QR.data.decode("utf-8")

        if (QR_data!=data[-1]):
            data[-1] = QR_data
            print(data)

        point = QR.rect

        cv2.rectangle(img,(point[0],point[1]),(point[0]+point[2],point[1]+point[3]),(0,200,255),5)
        #cv2.putText(img,QR_data,(point[0],point[1]),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),1)


    cv2.imshow("img",img)
    key = cv2.waitKey(1)
    if key == 27:
        break
