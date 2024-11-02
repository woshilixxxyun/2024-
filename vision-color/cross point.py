import cv2
import numpy as np

def point(img):
    imgCopy=img.copy()
    blur_img=cv2.blur(imgCopy,(3,3))
    gray_img=cv2.cvtColor(blur_img,cv2.COLOR_BGR2GRAY)

    lines = cv2.HoughLines(gray_img,1,np.pi/180,1010)
    print(lines)
    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(imgCopy, (x1, y1), (x2, y2), (0, 0, 255), 2)
            #cv2.line(imgCopy,(1,1),(640,480),(0,0,255),2)
            cv2.imshow('imgCopy1',imgCopy)



if __name__=='__main__':
    #cap=cv2.VideoCapture(0)
    img = cv2.imread('photo/form.png')

    #_,img=cap.read()
    cv2.imshow('img',img)
    point(img)
    cv2.waitKey(0)



    #cap.release()
    #cv2.destroyWindow()