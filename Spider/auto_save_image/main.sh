for i in {001..200};do
echo $i
done > list

for k in {1..6};do
python get.py http://yikeyz.com/topic/tt/aiss/page/$k | grep "<h2><a" | cut -d '"' -f 2,8 | sed 's/ //g' | sed 's/&#//g'
done > groupname

count=1
for i in `cat groupname`;do
url=`echo $i | cut -d '"' -f 1`
name=`echo $i | cut -d '"' -f 2`
no=`head -n $count list | tail -n 1`
count=`echo "$count+1" | bc`

[ -e ${no}_${name} ]&&continue
mkdir ${no}_${name}

page=`python get.py $url | grep "<span>1</span>" | grep -o ">.[0-9]*</" | tail -n 1 | sed 's/>//g' | sed 's/<\///g'`
echo -e "mark\t$page\t$name"

for ((j=1;j<=${page};j++));do
python get.py $url/$j | grep 'aligncenter' | grep jpg | grep -Po "http://.*?jpg" 
done > ${no}_${name}/list

cd ${no}_${name}
for p in `cat list`;do
wget $p
sleep 0.5
done
cd ..
done
