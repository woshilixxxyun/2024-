import cv2

cap = cv2.VideoCapture(1)#默认摄像头的捕获
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1200)#捕获的帧宽为1200像素
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)#捕获的帧高为720像素
#frame = cv2.imread("photo/red pen.jpg")

#从摄像头连续获取和处理摄像头的每一帧图像
while True:
    _, frame = cap.read()#“_"表示布尔值表示读取是否成功（通常在错误处理时使用）
                         #"frame"表示这一帧的图像数据，类型为numpy数组
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#用cv2.cvtColor()将图像从RGB转为HSV
    height,width ,_ = frame.shape#获取当前帧图像的高、宽以及通道数（通常是BGR三通道，所以这里用下划线 _ 忽略了第三个值）

    #计算图像中心点的横纵坐标
    cx = int(width/2)
    cy = int(height/2)

    pixel_center = hsv_frame[cy,cx]#获取中心点的颜色信息
    hue_value = pixel_center[0]#读取第一个值，即H的值
    s_value = pixel_center[1]
    v_value = pixel_center[2]

    #判断是什么颜色
    color = "Undefined"
    if 35 < hue_value <=77 and 43<s_value<=255 and 46<v_value<=255:
        color = "GREEN"
    elif 100 < hue_value <=124 and 43<s_value<=255 and 46<v_value<=255:
        color = "BLUE"
    elif 156<hue_value<=180 and 43<s_value<=255 and 46<v_value<=255:
        color = "RED"
    else:
        color = "Undefined"

    print(pixel_center)#打印颜色值
    pixel_center_bgr = frame[cy,cx]#获取BGR的值
    b,g,r = int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])
    cv2.putText(frame,color,(10,50),0,1,(b,g,r),2)
    cv2.circle(frame,(cx,cy),5,(b,g,r),3)#绘制圆，作为中心的参考

    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)#等待用户按键，参数1表示延迟时间（毫秒），在此期间如果用户按下键盘任意键，函数会返回该键的ASCII码值；如果没有按键则返回1。
    if key ==27:#按下esc键
        break

cap.release()
cv2.destroyWindow()