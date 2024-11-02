import cv2

#cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(0)

while 1:
    #_,img1=cap1.read()
    _,img2=cap2.read()
    #cv2.imshow('img1',img1)
    cv2.imshow('img2',img2)
    
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()