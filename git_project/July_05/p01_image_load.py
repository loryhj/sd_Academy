# -*- coding:utf-8 -*-
# pip install opencv-python
# 그림, 음성, 영상, .....-인코딩 -> 숫자

import cv2
import matplotlib.pyplot as plt

data = cv2.imread("D:/BYUN/chung.jpg", cv2.IMREAD_GRAYSCALE)
print(data)
plt.imshow(data, cmap='gray')
plt.show()

# color
data = cv2.imread("D:/BYUN/chung.jpg", cv2.IMREAD_COLOR) # BGR
print(data)
data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB) # BGR -> RGB
plt.imshow(data)
plt.show()