# -*- coding:utf-8 -*-

#AI
#MachineLearning : 어떤 문제 해결하는데 필요한 알고리즘을 사람이 지정해주는 것, 여태 해왔던것들을 좀 더  AI스러운 알고리즘으로
#DeepLearning : 어떤 문제 해결하는데 필요한 알고리즘도 직접 찾아서 문제 해결, tensorflow로 인공신경망


# KNN (K-Nearest Neighbor) 알고리즘
#지도학습, 학습데이터 그래프상의 점으로 표현, 예측데이터와 가장 가까운(피타고라스정리) 학습데이터 몇개 찾아서 다수결로 최종 결론


# 지도학습 : 기존 사람들이 판정해둔거 알려주고, 이후의 데이터 예측
# 비지도학습 : 학습한 데이터의 특징을 찾는다 (비슷한거끼리 묶기)


# pip install sklearn 설치
# python 머신러닝 library

import numpy as np
from sklearn.neighbors._classification import KNeighborsClassifier


data = np.array([[80,20],[95,5],[10,90],[90,10],[5,95]])
label = np.array(["액션", "액션", "조폭", "조폭", "액션"])


knc = KNeighborsClassifier(3) #가장 가까운 3개 뽑아서 결론
knc.fit(data, label) #학습시키기

x = float(input("격투 : "))
y = float(input("욕 : "))
what = np.array([[x,y]]) #[[80,20],[95,5],[10,90],[90,10],[5,95]]
result = knc.predict(what) #결론내기
print(result)
print(result[0])




