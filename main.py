import cv2
import os
import numpy as np

# 读取
img = cv2.imread("./config/test.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,200,30)

circle = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,5,param1=200,param2=30
                          ,minRadius=20,maxRadius=25)


num_circle = 0
if circle is not None:
    circle = np.uint16(np.around(circle[0,:,:]))
    for i in circle[:]:
        # Draw outer circle
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Draw inner circle
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
        num_circle = num_circle + 1
    print(img.shape[0]//5)
    # cv2.putText(img,str(num_circle),(200,200),3,3,(0,0,0))
    cv2.putText(img,str(num_circle),(img.shape[1]//3,img.shape[0]//7),6,4,(0,0,0))
    # cv2.putText(img,)
# cv2.imshow("result",img)
# cv2.waitKey(0)
cv2.imwrite("./debug/edge3.png",edges)
cv2.imwrite("./debug/result1.png",img)