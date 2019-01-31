#!/usr/bin/env python
# Jia 2018.12.22


######
# input
bank = 'bank1.csv'
sample = 'sample2.csv'
######


def plot4(a1, a2, b1, b2, scale):
    scale2 = max(a1, a2, b1, b2) - min(a1, a2, b1, b2)
    if range == 0:
        return 0
    m1 = int((a1 - min(a1, a2, b1, b2)) * scale / scale2)
    m2 = int((a2 - min(a1, a2, b1, b2)) * scale / scale2)
    t1 = int((b1 - min(a1, a2, b1, b2)) * scale / scale2)
    t2 = int((b2 - min(a1, a2, b1, b2)) * scale / scale2)
    visual = ("%12s%s%s%s%s\n%11s%s%s%s%s\n" % (
        idt, ' ' * (m1 + 10 - len(str(startt))), startt, '-' * (m2 - m1 + 1), endt,
        idm, ' ' * (t1 + 10 - len(str(startm))), startm, '-' * (t2 - t1 + 1), endm))
    return visual


b = open(bank, 'r')
out = open('%s_in_%s' % (sample.split('.')[0], bank.split('.')[0]), 'w')
for i in b.readlines():
    idt = i.split(',')[0]
    chrt = int(i.split(',')[1])
    startt = int(i.split(',')[2])
    endt = int(i.split(',')[3].split('\n')[0])
    s = open(sample, 'r')
    for j in s.readlines():
        idm = j.split(',')[0]
        chrm = int(j.split(',')[1])
        startm = int(j.split(',')[2])
        endm = int(j.split(',')[3].split('\n')[0])
#        print(idm + " " + chrm + " " + startm + " " + endm)
        if chrt == chrm:
            if startt <= startm <= endt:
                print(plot4(startt, endt, startm, endm, 80))
                out.writelines(plot4(startt, endt, startm, endm, 80))
                out.writelines('\n')
            elif startm <= startt <= endm:
                print(plot4(startt, endt, startm, endm, 80))
                out.writelines(plot4(startt, endt, startm, endm, 80))
                out.writelines('\n')

