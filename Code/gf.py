# --coding:utf-8--
#暴力模拟计算，如果要集齐12星座，需要多少人斩。
import random
total = 0
round = 0
n=100000
for i in range(0,n):
    xingzuolist = []
    k=1
    while True:
        xingzuo = random.randint(1,12)
        if xingzuo in xingzuolist:
            "do nothing"
        else:
            xingzuolist.append(xingzuo)
        if len(xingzuolist) == 12:
            total += k
            break
#            print round
#            print total / round
#            print j
        k=k+1
#print total/round
print total
print total/(n + 0.0)
#for k in range(1,100):
#    print random.randint(1,12)
