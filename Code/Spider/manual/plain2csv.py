#!/usr/bin/python
# -*- coding: utf-8 -*-

plain=open("raw.txt",'r').readlines()
cycle_data=open("cycling_data.csv",'w')

while '\n' in plain:
    plain.remove('\n')
#print len(plain)
for i in range(0,len(plain)):
    if plain[i][:-1] == "  *" and plain[i+6][0:13] == "    <#/track/":
#        print plain[i][:-1]
#        print plain[i+6][0:13] #track ID

        date = plain[i+3][4:-1]
        name = plain[i+4][4:-1]
        dis      = (plain[i+5][4:-1].split(' '))[1][:-8]
        duration = (plain[i+5][4:-1].split(' '))[2][:-6]
        avs      = (plain[i+5][4:-1].split(' '))[3][:-10]
        climb    = (plain[i+5][4:-1].split(' '))[4][:-1]
#        print plain[i+5][4:-1].split(' ')
#        print "%s,%s,%s,%s,%s,%s,%s,%s" % (date.split('-')[0], date.split('-')[1], date.split('-')[2], name, dis, duration, avs, climb)
        cycle_data.write("%s,%s,%s,%s,%s,%s,%s,%s\n" % (date.split('-')[0], date.split('-')[1], date.split('-')[2], name, dis, duration, avs, climb))
