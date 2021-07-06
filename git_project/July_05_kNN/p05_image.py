# -*- coding:utf-8 -*-
import cv2
import matplotlib.pyplot as plt
data = cv2.imread("D:/BYUN/chung.jpg", cv2.IMREAD_COLOR)
avgColor = cv2.mean(data) #  인공지능할때 이걸로 사용하자
print(avgColor)

r = avgColor[2]
g = avgColor[1]
b = avgColor[0]

r = int(r)
g = int(g)
b = int(b)
print(r, g, b)

r = "%02X" % (r) # 2자리 16진수
g = "%02X" % (g)
b = "%02X" % (b)
print(r, g, b)

c = "#"+r+g+b
print(c)

plt.bar(10, 10, color=c)
plt.show()