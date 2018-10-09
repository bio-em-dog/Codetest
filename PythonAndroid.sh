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
apt install python-pip
pip install --upgrade pip
