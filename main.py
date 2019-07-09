import cv2
import os
import numpy as np


def nothing(x):
    pass
# 读取
img = cv2.imread("./config/test.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# OTUS 设置阈值后canny，更为精准
ret,gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# 方便调试，缩小一倍
# gray = cv2.resize(gray,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
# img = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
cv2.namedWindow("circle")
cv2.createTrackbar('param_canny1','circle',0,200,nothing)
cv2.createTrackbar('param_canny2','circle',0,200,nothing)
cv2.createTrackbar('param_Hough1','circle',15,200,nothing)
cv2.createTrackbar('param_Hough2','circle',15,100,nothing)


while (True):
    gray_ = np.copy(gray)
    img_ = np.copy(img)
    param_canny1 = cv2.getTrackbarPos("param_canny1",'circle')
    param_canny2 = cv2.getTrackbarPos("param_canny2",'circle')
    param_Hough1 = cv2.getTrackbarPos("param_Hough1",'circle')
    param_Hough2 = cv2.getTrackbarPos("param_Hough2",'circle')

    print(param_canny1,param_canny2,param_Hough1,param_Hough2)
    edges = cv2.Canny(gray_,param_canny1,param_canny2)
    circle = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,5,param1=param_Hough1,param2=param_Hough2,minRadius=20,maxRadius=25)
    # 缩小一倍
    # circle = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,5,param1=param_Hough1,param2=param_Hough2,minRadius=20//2,maxRadius=25//2)
    num_circle = 0
    if circle is not None:
        circle = np.uint16(np.around(circle[0,:,:]))
        for i in circle[:]:
            # Draw outer circle
            cv2.circle(img_, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw inner circle
            cv2.circle(img_, (i[0], i[1]), 2, (0, 0, 255), 3)
            num_circle = num_circle + 1
        print(img.shape[0]//5)
        cv2.putText(img_,str(num_circle),(img_.shape[1]//3,img_.shape[0]//7),6,4,(0,0,0))
    # img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
    edges_ = cv2.merge((edges,edges,edges))
    dst = np.hstack((edges_,img_))
    # cv2.imshow("circle", edges)
    cv2.imshow("circle", dst)
    if cv2.waitKey(1) == 27:
        cv2.imwrite("./debug/dst.png",dst)
        break
    # cv2.imwrite("./debug/result3.png",img)