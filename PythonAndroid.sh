docker pull registry.docker-cn.com/library/ubuntu:16.04
#国内官方镜像
docker run -itd -v /home/em/data1/jia/JiaUbuntu:/JiaUbuntu --name JiaUbuntu registry.docker-cn.com/library/ubuntu:16.04 /bin/bash
docker exec -it JiaUbuntu /bin/bash

apt-get install vim

#更新apt源
#cp /etc/apt/source.list /etc/apt/source.list.bak
#找几个阿里云
#apt-get update

#安装python2.7
apt-get install python2.7
apt-get install python-pip
pip install --upgrade pip

#p4a
#https://github.com/cycleuser/Kivy-CN/blob/master/01-Kivy-Installation.md 
apt-get install software-properties-common python-software-properties
add-apt-repository ppa:kivy-team/kivy
apt-get update
apt-get install python-kivy
apt-get install python-kivy --fix-missing

#windows写代码环境部署
#https://blog.csdn.net/ghking1/article/details/79609363


#linux部署环境
#p4a
#https://blog.csdn.net/ghking1/article/details/79609363
dpkg --add-architecture i386
apt-get update
apt-get install libssl-dev libffi-dev
apt-get install cython==0.21
apt-get install virtualenv
apt-get install -y build-essential ccache git zlib1g-dev python2.7 python2.7-dev libncurses5:i386 libstdc++6:i386 zlib1g:i386 openjdk-8-jdk unzip ant ccache autoconf libtool



#buildozer
#https://blog.csdn.net/fangxuejiang/article/details/49405277
pip install buildozer




#docker图形界面 
xhost +
#docker run -itd -v /etc/localtime:/etc/localtime:ro -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY -e GDK_SCALE -e GDK_DPI_SCALE --name test registry.docker-cn.com/library/ubuntu:16.04
docker run -itd -v /home/em/data1/jia/JiaUbuntu:/JiaUbuntu --name Ubuntu -v /etc/localtime:/etc/localtime:ro -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY -e GDK_SCALE -e GDK_DPI_SCALE registry.docker-cn.com/library/ubuntu:16.04

