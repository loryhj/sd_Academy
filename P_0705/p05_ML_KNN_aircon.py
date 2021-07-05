# -*- coding:utf-8 -*-

# from cx_Oracle import connect
# con = connect("sunny/123123123@192.168.0.90:1521/xe")
# sql = "select when, description, temp, humidity, power from realtime_weather" 
# airconDF = pd.read_sql(sql,con)
# con.close()

import pandas as pd
import numpy as np
from sklearn.neighbors._classification import KNeighborsClassifier
from http.client import HTTPSConnection
from json import loads

airconDF = pd.read_csv("D:/Sunny/owmWeather.csv", names=["년", "월", "일", "시", "분", "기온", "날씨", "습도", "에어컨"])

trainData = airconDF[["기온", "습도"]].to_numpy()
# print(trainData)
label = airconDF["에어컨"]
# print(label)

knc = KNeighborsClassifier(5)
# print(knc)
knc.fit(trainData, label) #????????????????

con = HTTPSConnection("api.openweathermap.org") 
con.request("GET", "/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr") 
res = con.getresponse() 
resBody = res.read()
con.close()

weatherData = loads(resBody) 
t = weatherData["main"]["temp"]
h = weatherData["main"]["humidity"]
print(t)
print(h)
what = [[t, h]]

result = knc.predict(what)
print(t)
print(h)
print(result[0])

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

fontFile = ("c:/windows/Fonts/malgun.ttf")
fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
plt.rc("font", family=fontName)

sns.scatterplot(x="기온", y="습도", hue="에어컨", data=airconDF)
plt.show()

