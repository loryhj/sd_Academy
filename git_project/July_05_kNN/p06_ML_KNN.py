# -*- coding:utf-8 -*-


# scikit-learn : python machineleaning library
# pip install sklearn
# pip install numpy==1.16.4 #numpy version 낮추기



# AI
#     MachineLearning : 어떤 문제를 해결을 하는데 필요한 알고리즘을 사람이 지정해주면
#            여태 해왔던것들
#            좀더 ai스러운 알고리즘 몇 개 봅시다
#     DeepLearning : 어떤 문제를 해결을 하는데 필요한 알고리즘도 직접 찾아서 문제 해결
#            tensorflow로 인공신경망....

# 지도학습
#        영화A-액션
#        영화B-조폭
#        ...기존 사람들이 판정해놓은거를 알려주고, 미지의 데이터를 예측
# 비지도학습
#        영화A
#        영화B
#        ...그 학습데이터의 특징을 찾는(비슷한거끼리 묶기, ...)

# kNN(k-Nearest Neightbor)알고리즘 : 학습데이터랑 비슷한걸로 최종 결론 내주는
#    사람들이 많이 봐 왔던, 사람 비슷한 거를 사람이라고 판정
#     지도학습
#     학습데이터를 그래프상의 점으로 표현
#     예측해야하는 데이터도 점으로 표현
#     예측데이터와 가장 가까운(피타고라스 정리 학습데이터를 k개 찾아서)
#     다수결로 최종 결론

import numpy as np
from sklearn.neighbors._classification import KNeighborsClassifier

data = np.array([[80, 20], [95, 5], [10, 90], [90, 10], [5, 95]])
label = np.array(['액션', '액션', '조폭', '조폭', '액션'])

knc = KNeighborsClassifier(3) # 가장 가까운 3개 뽑아서 결론...
knc.fit(data, label) #학습시키기

x = float(input("격투 : "))
y = float(input("욕 : "))
what = np.array([[x, y]])
result = knc.predict(what) #결론내기
print(result)
print(result[0])