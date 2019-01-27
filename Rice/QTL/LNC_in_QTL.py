#!/usr/bin/env python
# Jia 2018.12.22
# mod 2019.01.27 update if statement, add calc percentage


######
# input
bank = 'bank1.csv'
sample = 'sample2.csv'
######


def plot4(a1, a2, b1, b2, scale):
    global hit
    hit += 1
    sort_4 = sorted([a1, a2, b1, b2])
    scale2 = sort_4[3] - sort_4[0]
    if range == 0:
        return 0
    m1 = int((a1 - sort_4[0]) * scale / scale2)
    m2 = int((a2 - sort_4[0]) * scale / scale2)
    t1 = int((b1 - sort_4[0]) * scale / scale2)
    t2 = int((b2 - sort_4[0]) * scale / scale2)
    visual = ("hit%s\t%sbp\t%.3f%%\t%.3f%%\n%12s%s%s%s%s\n%12s%s%s%s%s\n\n" % (
        hit, sort_4[2]-sort_4[1], (sort_4[2]-sort_4[1])*100.0/(b2-b1), (sort_4[2]-sort_4[1] + 0.1 - 0.1)*100.0/(a2-a1),
        idt, ' ' * (m1 + 10 - len(str(startt))), startt, '-' * (m2 - m1 + 1), endt,
        idm, ' ' * (t1 + 10 - len(str(startm))), startm, '-' * (t2 - t1 + 1), endm
        ))
    return visual


b = open(bank, 'r')
out = open('%s_in_%s' % (sample.split('.')[0], bank.split('.')[0]), 'w')
hit = 0
# t - bank, m - sample
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
            if startt <= startm <= endt or startt <= endm <= endt:
#                print(plot4(startt, endt, startm, endm, 80))
                out.writelines(plot4(startt, endt, startm, endm, 80))
