# -*- coding:utf-8 -*-

# age = int(input("나이: "))
age =15
# insa ="ㅎㅇ"
# if age > 20:
    # age ="안녕하세요"
# elif age >= 10:
    # age = "안녕"

# insa라는 변수에 20살 이상이면 안녕하세요, 아니면 안녕
insa = "안녕"
if age > 20:
    insa = "안녕하세요"
print(insa)
print("=======================================")



# list
list2 = [123, 456, 76, 123, 111, 546]
print(list2[0])

# numpy
import numpy as np
ll = np.array([324, 342, 12, 2, 234])
print(ll[0])
print("-----")

# set
s = {123, 456, 76, 123, 111, 546} # 중복제거, 순서?
print(len(s))
print(s)


# dict : 순서x, key-Value(찾는 기준도 설정)
d = {"마우스":10000, "키보드":13000}
print(d['마우스'])

# range
e = range(3, 10, 2)
e = list(e)
# e = list(e)
print(e)

# tuple
f, g, h = (10, 123, 10)
print(f)

# pandas
import pandas as pd
df = pd.read_csv("D:/BYUN/subway.csv", names=['y', 'm', 'd', 'no', 'sta', 'r', 'a'])
