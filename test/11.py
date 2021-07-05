# -*- coding:utf-8 -*-

#pip install opencv-python 설치

import cv2
import matplotlib.pyplot as plt


#grayscale : 픽셀단위로 색상 표기해주는 기능 (흰색은 255, 검은색은 0)
# data = cv2.imread("D:/sunny/sad.png", cv2.IMREAD_GRAYSCALE) 
# print(data)
# plt.imshow(data, cmap='gray') # 좌표, 컬러맵
# plt.show()

#BGR
data = cv2.imread("D:/sunny/sad.png", cv2.IMREAD_COLOR) #BGR
print(data)

data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB) #BGR -> RGB로
plt.imshow(data)
plt.show()















=======
# 생활코딩 : https://opentutorials.org/course/1
print("11")
>>>>>>> branch 'main' of https://github.com/loryhj/sd_Academy.git
