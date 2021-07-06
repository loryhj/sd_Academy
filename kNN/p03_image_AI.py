# -*- coding:utf-8 -*-

import cv2

#그림,영상,음성 -> 인코딩 과정 -> 숫자
#인공신경망에 넣으려면 1차원으로 변환해야 한다

# data = cv2.imread("D:/sunny/sad.png", cv2.IMREAD_GRAYSCALE) 
# data = data.flatten() #1차원(숫자)으로 바꾸기 : 한 줄의 숫자로 펼쳐놓기 (세팅)
# print(data)


data = cv2.imread("D:/sunny/sad.png", cv2.IMREAD_COLOR) 
avgColor = cv2.mean(data)
b = avgColor[0]
g = avgColor[1]
r = avgColor[2]

print(r) #소수점까지 나와있어서

r = int(r) #소수점 제거
g = int(g)
b = int(b)

print(r,g,b)









