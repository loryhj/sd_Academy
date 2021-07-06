# -*- coding:utf-8 -*-
# test9 머신러닝 기반 데이터 분석 : kNN
import pandas as pd
from sklearn.neighbors._classification import KNeighborsClassifier
from http.client import HTTPSConnection
from json import loads

# DB에서 값을 가져올때
# ow_temp, ow_humidity, ow_power
from cx_Oracle import connect
con = connect("sdedu03/sdedu03@192.168.0.75:1521/xe")
sql = "select * from ow_weather_lory order by ow_when"
airconDB = pd.read_sql(sql, con)
con.close()
print(airconDB)
# trainData2 = airconDB[[ow_temp,ow_humidity]].to_numpy()
# label2 = airconDB['ow_power']
# knc = KNeighborsClassifier(5)
# # knc.fit(trainData, label)
# knc.fit(trainData2, label2)
# t = float(input("기온: "))
# h = float(input("습도: "))
# what = [[t, h]]
# result = knc.predict(what)
# print(result[0])


# 파일에서 가져올때
airconDF = pd.read_csv("D:/BYUN/owmWeather.csv", names=['년', '월', '일', '시', '분', '구분', '기온', '습도', '에어콘'])
trainData = airconDF[['기온', '습도']].to_numpy()
label = airconDF['에어콘']
# print(trainData)
knc = KNeighborsClassifier(5)
knc.fit(trainData, label)

##############################################################
con = HTTPSConnection("api.openweathermap.org")
con.request("GET", "/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
resBody = con.getresponse().read()
con.close()

weatherDate = loads(resBody) 

t= weatherDate['main']['temp']
h= weatherDate['main']['humidity']
##############################################################
# t = float(input("기온: "))
# h = float(input("습도: "))
what = [[t, h]]
result = knc.predict(what)
print(result[0])

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
fontFile = "c:/windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
plt.rc("font", family=fontName)

sns.scatterplot(x='기온', y='습도', hue='에어콘', data=airconDF)
plt.show()