# -*- coding:utf-8 -*-
#
# 현재시간날짜
# 날씨
# 기온
# 습도
# 선풍기파워
from http.client import HTTPConnection
from json import loads
from datetime import datetime
from cx_Oracle import connect

# 분석용 csv 파일제작, 분석용 db 생성

f = open("D:\\BYUN\\getWeatermapList.csv", 'a', encoding="utf-8")
con = HTTPConnection("api.openweathermap.org")
con.request("GET", "/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
cnn = connect("sdedu03/sdedu03@192.168.0.75:1521/xe")

des = None
temp = 0
hm = 0
resBody = con.getresponse().read()
weatherList = loads(resBody)

now = datetime.today()
des = weatherList["weather"][0]["description"]
temp = weatherList["main"]["temp"]
hm = weatherList["main"]["humidity"]

power = '약'
if int(temp) >= 30:
    power = '강'
elif int(temp) >= 20:
    power = '중'

sql = "insert into ow_weather_lory values(sysdate,'%s','%.2f','%s','%s')" % (des, temp, hm, power)
rs = cnn.cursor()
rs.execute(sql)

f.write("%s," % now)
f.write("%s," % des)
f.write("%.2f," % temp)
f.write("%s," % hm)
f.write("%s\n" % power)

if rs.rowcount >= 1:
    print("success")
    cnn.commit()

f.close()
con.close()
cnn.close()
