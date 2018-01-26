import os

line = 0
ls = os.popen('ls ./box/*.box').readlines()

for i in open('tmp5'):
    if i.split('\t')[0] == i.split('\t')[1][:-1]:
        print (ls[line][:-1]+'\t'+i[:-1]+'\tright')
    elif i.split('\t')[0] == '0':
        print (ls[line][:-1]+'\t'+i[:-1]+'\tunused')
    else:
        print (ls[line][:-1]+'\t'+i[:-1])
    line += 1
