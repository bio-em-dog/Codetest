# --coding:utf-8--
#Jia
#2017.5.20 把两个文件拼接在一起，每一行续在对应行后面

from sys import argv
filename,in1,in2,out = argv

#in1=raw_input('input file 1:')
#in2=raw_input('input file 2:')
#out = raw_input('out put file name:')

file1=open(in1,'r')
file2=open(in2,'r')
file3=open(out,'w')

lines = 3749528
#lines = raw_input("""how many lines?
#Use ${cat <filename> | wc -l} in shell
#3749528???
#:""")

for i in range(0,int(lines)):
    file3.write(str(file1.readline())[0:-1]+","+str(file2.readline())[0:-2]+"\n")

#不同编码格式的，最后的那一位不同
