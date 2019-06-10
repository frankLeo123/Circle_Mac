import cv2
import os
import numpy as np

# 读取
img = cv2.imread("./config/test.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,200,30)

circle = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,5,param1=200,param2=30
                          ,minRadius=20,maxRadius=25)
if circle is not None:
    circle = np.uint16(np.around(circle[0,:,:]))
    for i in circle[:]:
        # Draw outer circle
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Draw inner circle
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

# cv2.imshow("result",img)
# cv2.waitKey(0)
cv2.imwrite("./debug/edge3.png",edges)
cv2.imwrite("./debug/result.png",img)