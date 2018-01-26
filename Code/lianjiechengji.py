# --coding:utf-8--
a = 9000
b = 9999
maxnum = 0


for i in range(9000,9999+1):
    list = []
    raw = (str(i * 1) + str(i * 2))
    for j in range(0,9):
        list.append(raw[j])
    list.sort()
    if list != ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
#        print 'ffffff'
        'do nothing'
    else:
        if int(raw) > maxnum:
            maxnum = int(raw)
        print maxnum