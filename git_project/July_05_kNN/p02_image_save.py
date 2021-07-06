# -*- coding:utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import numpy as np

# 크기변경
# data = cv2.imread("D:/BYUN/chung.jpg", cv2.IMREAD_GRAYSCALE)
# data = cv2.resize(data, dsize=(100, 200))
# data = cv2.resize(data, dsize=(0,0), fx=0.5, fy=0.3) #비율
# data = cv2.resize(data, dsize=(0,0), fx=0.5, fy=0.3, interpolation=cv2.INTER_LINEAR) #보간
# plt.imshow(data, cmap='gray')
# plt.show()

# 자르기
# data = cv2.imread("D:/BYUN/chung.jpg", cv2.IMREAD_GRAYSCALE)
# data = data[1:100, 100:500]
# plt.imshow(data, cmap="gray")
# plt.show()

#불러
# data = cv2.imread("D:/BYUN/chung.jpg", cv2.IMREAD_GRAYSCALE)
# data = cv2.blur(data,(20,50)) # 주위 20*50의 평균값으로
# plt.imshow(data, cmap="gray")
# plt.show()

# 쨍하게
# data = cv2.imread("D:/BYUN/chung.jpg", cv2.IMREAD_GRAYSCALE)
# k = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) #커널
# data = cv2.filter2D(data, -1, k) # -1 : 원본하고 같은 포맷으로(jpg)
# plt.imshow(data, cmap="gray")
# plt.show()



