import cv2
import numpy as np

cap=cv2.VideoCapture(0)
def circle(blur_img):
        circle = cv2.HoughCircles(blur_img, cv2.HOUGH_GRADIENT, 1, 200, param1=100, param2=50, minRadius=100,
                                  maxRadius=200)
        for i in circle:
            cv2.circle(img, (i[0], i[1]), 5, (255, 0, 0), 1)

def ShapeDetection(img,imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 寻找轮廓点

    for cnt in contours:
        area = cv2.contourArea(cnt)#计算面积
        peri = cv2.arcLength(cnt, True)  # 计算轮廓长度
        if area>1000 and peri<2000:
            cv2.drawContours(imgContour, cnt, -1, (0, 255, 255), 1)  # 绘制轮廓线
            approx = cv2.approxPolyDP(cnt,0.2*peri,True)
            n=len(approx)
            print(n)
            print(peri)

            #如果是圆形
            if 1:
                x ,y ,w , h = cv2.boundingRect(cnt)
                cv2.rectangle(imgContour,(x,y),(x+w,y+h),(255,0,0),5)


                if x >= 200 and y >= 140 and x + w <= 370 and y + h <= 300:
                    print("Success")
                   #若识别的物体进入框内，输出success
                    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 用cv2.cvtColor()将图像从RGB转为HSV
                    cv2.imshow("img",hsv_img)
                    pixel_center = hsv_frame[285,220]  # 获取中心点的颜色信息
                    hue_value = pixel_center[0]  # 读取第一个值，即H的值
                    s_value = pixel_center[1]
                    v_value = pixel_center[2]

                    color = "Undefined"
                    if 35 < hue_value <= 77 and 43 < s_value <= 255 and 46 < v_value <= 255:
                        color = "GREEN"
                    elif 100 < hue_value <= 124 and 43 < s_value <= 255 and 46 < v_value <= 255:
                        color = "BLUE"
                    elif 156 < hue_value <= 180 and 43 < s_value <= 255 and 46 < v_value <= 255:
                        color = "RED"


while True:
    ret,img=cap.read()#读取图像
    imgContour=img.copy()#copy图像
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度图
    #HSV_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #cv2.imshow("hsv",HSV_img)
    blur_img=cv2.GaussianBlur(gray_img,(7,7),1)#高斯滤波
    #cv2.imshow("blur",blur_img)
    canny_img=cv2.Canny(blur_img,100,150)#边缘检测
    kernal=np.ones((5,5))#卷积
    dial_img=cv2.dilate(canny_img,kernal,2)#膨胀操作
    #cv2.imshow("dial_img",dial_img)
    cv2.rectangle(imgContour, (200, 140), (370, 300), (255, 0, 0), 5)#绘制中心框



    ShapeDetection(dial_img,imgContour)


    if not ret:
        break


    cv2.imshow("img1",imgContour)
    key=cv2.waitKey(1)
    if key ==27:
        break

cap.release()
cv2.destroyAllWindows()
