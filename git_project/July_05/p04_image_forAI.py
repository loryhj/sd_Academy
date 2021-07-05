# -*- coding:utf-8 -*-

import cv2
# 그림, 음성, 영상, ... -인코딩 -> 숫자
# 인공신경망에 넣으려면 -> 1차원으로

data = cv2.imread("D:/BYUN/chung.jpg", cv2.IMREAD_COLOR)
data = data.flatten()
print(data)