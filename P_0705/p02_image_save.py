# -*- coding:utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import numpy as np

#저장하기
# data = cv2.imread("D:/sunny/sad.png", cv2.IMREAD_GRAYSCALE) 
# cv2.imwrite("D:/sunny/sad_1.png", data) #위에 그레이스케일 된 data 저장하기

#사이즈 조정
# # data = cv2.resize(data, dsize=(200,250)) #절대값, 숫자 넣어서 사이즈 조정
# data = cv2.resize(data, dsize = (0,0), fx=0.5, fy=0.3, interpolation=cv2.INTER_LINEAR) 
# #                                                x축 y축 비율로 사이즈조정,   보간
# plt.imshow(data, cmap='gray')
# plt.show()


#자르기
data = cv2.imread("D:/sunny/sad.png", cv2.IMREAD_GRAYSCALE) 
data = data[1:100, 100:500]
plt.imshow(data, cmap='gray')
plt.show()


#블러처리
data = cv2.imread("D:/sunny/sad.png", cv2.IMREAD_GRAYSCALE) 
data = cv2.blur(data, (20, 50))
plt.imshow(data, cmap='gray')
plt.show()

#블러처리
data = cv2.imread("D:/sunny/sad.png", cv2.IMREAD_GRAYSCALE) 
data = cv2.blur(data, (20, 50)) #주위 20*50의 평균값으로
plt.imshow(data, cmap='gray')
plt.show()


#쨍하게
data = cv2.imread("D:/sunny/sad.png", cv2.IMREAD_GRAYSCALE) 
k = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]) #커널
data = cv2.filter2D(data, -1, k) #-1: 원본하고 같은 포맷으로(jpg)
plt.imshow(data, cmap='gray')
plt.show()


#대비 (밝은거 더 밝게, 어두운거 더 어둡게)
data = cv2.imread("D:/sunny/sad.png", cv2.IMREAD_GRAYSCALE) 
data = cv2.equalizeHist(data)
plt.imshow(data, cmap='gray')
plt.show()


#경계선 검정화
data = cv2.imread("D:/sunny/sad.png", cv2.IMREAD_GRAYSCALE) 
data = cv2.Canny(data, 50, 100) #50보다 작으면 무시 100보다 크면 무조건 경계선
plt.imshow(data, cmap='gray')
plt.show()


#이진화 (값보다 크면 흰색 작으면 검정으로)
data = cv2.imread("D:/sunny/sad.png", cv2.IMREAD_GRAYSCALE) 
_, data = cv2.threshold(data, 100, 255, cv2.THRESH_BINARY)
#                                    기준값, 바꿀값, (100보타크면255,아니면0) cv2.THRESH_INV
plt.imshow(data, cmap='gray')
plt.show()















