# -*- coding:utf-8 -*-

import cv2
import matplotlib.pyplot as plt
# 대비 늘리기(밝은거 더 밝게, 어두운거 더 어둡게)
data = cv2.imread("D:/BYUN/chung.jpg", cv2.IMREAD_GRAYSCALE)
data = cv2.equalizeHist(data)
plt.imshow(data, cmap='gray')
plt.show()


# 경계선
# data = cv2.imread("D:/BYUN/chung.jpg", cv2.IMREAD_GRAYSCALE)
# data = cv2.Canny(data, 50, 100) # 50보다 작으면 무시, 100보다 크면 무조건 경계선
# plt.imshow(data, cmap='gray')
# plt.show()

# 이진화(값보다 크면 흰색, 작으면 검정으로)
data = cv2.imread("D:/BYUN/chung.jpg", cv2.IMREAD_GRAYSCALE)
_, data = cv2.threshold(data, 
                 100, # 기준값  
                 255, # 바꿀값
                 # cv2.THRESH_BINARY) # 100보다 크면 255로, 아니면 0
                 cv2.THRESH_BINARY_INV) # 반대로
plt.imshow(data, cmap='gray')
plt.show()