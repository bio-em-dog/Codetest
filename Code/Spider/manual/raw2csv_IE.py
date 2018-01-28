#!/usr/bin/python
# -*- coding: utf-8 -*-

plain=open("QQ.txt",'r').readlines()
cycle_data=open("cycling_data.csv",'w')

while '\n' in plain:
    plain.remove('\n')
while ' \n' in plain:
    plain.remove(' \n')
for i in range(len(plain)):  
    plain[i] = plain[i].lstrip()

print len(plain)

for i in range(len(plain)):
    try:
        if plain[i][4] == "-":
#            print plain[i]
            date = plain[i][:-1]
            name = plain[i+1][:-1]
            if ',' in name:
                name = name.replace(',',';')
            dis      = (plain[i+2][:-1].split(' '))[1][:-8]
            duration = (plain[i+2][:-1].split(' '))[2][:-6]
            avs      = (plain[i+2][:-1].split(' '))[3][:-10]
            climb    = (plain[i+2][:-1].split(' '))[4][:-1]
#            print plain[i+5][4:-1].split(' ')
#            print "%s,%s,%s,%s,%s,%s,%s,%s" % (date.split('-')[0], date.split('-')[1], date.split('-')[2], name, dis, duration, avs, climb)
            cycle_data.write("%s,%s,%s,%s,%s,%s,%s,%s\n" % (date.split('-')[0], date.split('-')[1], date.split('-')[2], name, dis, duration, avs, climb))
    except:
        "do nothing"