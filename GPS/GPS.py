# -*- coding:utf-8 -*-  
from math import*
from datetime import datetime

def Distance(Lat_A,Lng_A,Lat_B,Lng_B): #第一种计算方法
    ra=6378.140 #赤道半径
    rb=6356.755 #极半径 （km）
    flatten=(ra-rb)/ra  #地球偏率
    rad_lat_A=radians(Lat_A)
    rad_lng_A=radians(Lng_A)
    rad_lat_B=radians(Lat_B)
    rad_lng_B=radians(Lng_B)
    pA=atan(rb/ra*tan(rad_lat_A))
    pB=atan(rb/ra*tan(rad_lat_B))
    xx=acos(sin(pA)*sin(pB)+cos(pA)*cos(pB)*cos(rad_lng_A-rad_lng_B))
    c1=(sin(xx)-xx)*(sin(pA)+sin(pB))**2/cos(xx/2)**2
    c2=(sin(xx)+xx)*(sin(pA)-sin(pB))**2/sin(xx/2)**2
    dr=flatten/8*(c1-c2)
    distance=ra*(xx+dr)
    return distance

def DeltaTime(time1,time2):
    a=datetime.strptime(time1,"%Y-%m-%dT%H:%M:%SZ")
    b=datetime.strptime(time2,"%Y-%m-%dT%H:%M:%SZ")
    return b-a

def ele(ele1,ele2):
    return ele2-ele1

gpx = open('baoji.gpx')

for i in open('baoji.gpx'):
    line = gpx.readline()
    print (line[:-1] + '  head')
    if line == '    <trkseg>\n':
        break

line1 = gpx.readline()
line2 = gpx.readline()
line3 = gpx.readline()
line4 = gpx.readline()
print (line1+line2+line3+line4[:-1])

for i in open('baoji.gpx'):
    line5 = gpx.readline()
    line6 = gpx.readline()
    line7 = gpx.readline()
    line8 = gpx.readline()
    if line5 == '    </trkseg>\n':
        break
#eval 字符串到数字
    lat1 = eval(line1[18:29])
    lon1 = eval(line1[36:47])
    lat2 = eval(line5[18:29])
    lon2 = eval(line5[36:47])
    ele1 = eval(line2[13:22])
    ele2 = eval(line6[13:22])
    time1 = line3[14:34]
    time2 = line7[14:34]
    '两个点相距太远'
    if Distance(lat1,lon1,lat2,lon2) > 100*0.001:
        print ('too far')

    print (line5[:-1]+'11111 '+line5[18:29]+' '+line5[36:47])
 #   print ('      <trkpt lat="%d" lon="%d">'%(,))
    print (line6[:-1]+'22222 '+line6[13:22])
 #   print ('        <ele>%d</ele>')
    print (line7[:-1]+'33333 '+line7[14:34])
#    print ('        <time>2017-07-23T14:52:05Z</time>')
    print (line8[:-1]+'44444 ')

    line1 = line5
    line2 = line6
    line3 = line7
    line4 = line8


print (line5+line6+line7+line8[:-1])

