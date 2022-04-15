#!/bin/bash


sudo apt update -y
sudo apt install vim -y
sudo apt install wget -y
sudo apt install curl -y
sudo apt install remmina -y
sudo apt install git -y
sudo apt install vagrant -y
sudo apt install openssh-server -y




echo deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main >> /etc/apt/sources.list
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
apt update -y
apt install ansible -y

if [ ! -d ~/Downloads/pacotes ]
then
	mkdir ~/Downloads/pacotes
else
	echo "Diretorio já esta criado"
fi

cd ~/Downloads/pacotes

wget http://ftp.de.debian.org/debian/pool/main/q/qtbase-opensource-src/libqt5core5a_5.15.2+dfsg-9_amd64.deb > testes.txt
wget http://ftp.de.debian.org/debian/pool/main/q/qtbase-opensource-src/libqt5gui5_5.15.2+dfsg-9_amd64.deb > /dev/null
wget http://ftp.de.debian.org/debian/pool/main/q/qtbase-opensource-src-gles/libqt5gui5-gles_5.15.2+dfsg-4_amd64.deb
wget http://ftp.de.debian.org/debian/pool/main/q/qtbase-opensource-src/libqt5opengl5_5.15.2+dfsg-9_amd64.deb > /dev/null
wget http://ftp.de.debian.org/debian/pool/main/q/qtbase-opensource-src/libqt5printsupport5_5.15.2+dfsg-9_amd64.deb > /dev/null
wget http://ftp.de.debian.org/debian/pool/main/q/qtbase-opensource-src/libqt5widgets5_5.15.2+dfsg-9_amd64.deb > /dev/null
wget http://ftp.de.debian.org/debian/pool/main/q/qtx11extras-opensource-src/libqt5x11extras5_5.15.2-2_amd64.deb > /dev/null
wget http://ftp.de.debian.org/debian/pool/main/libs/libsdl1.2/libsdl1.2debian_1.2.15+dfsg2-6_amd64.deb > /dev/null
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb > /dev/null
wget https://download.virtualbox.org/virtualbox/6.1.32/virtualbox-6.1_6.1.32-149290~Debian~bullseye_amd64.deb > /dev/null

sudo dpkg -i libqt5core5a_5.15.2+dfsg-9_amd64.deb
sudo dpkg -i libqt5gui5_5.15.2+dfsg-9_amd64.deb
sudo dpkg -i libqt5gui5-gles_5.15.2+dfsg-4_amd64.deb
sudo dpkg -i libqt5opengl5_5.15.2+dfsg-9_amd64.deb
sudo dpkg -i libqt5printsupport5_5.15.2+dfsg-9_amd64.deb
sudo dpkg -i libqt5widgets5_5.15.2+dfsg-9_amd64.deb
sudo dpkg -i libqt5x11extras5_5.15.2-2_amd64.deb
sudo dpkg -i libsdl1.2debian_1.2.15+dfsg2-6_amd64.deb
sudo dpkg -i virtualbox-6.1_6.1.32-149290~Debian~bullseye_amd64.deb
sudo dpkg -i  google-chrome-stable_current_amd64.deb

sudo rm -rf ~/Downloads/pacotes

if [ ! -d ~/Repositorio ]
then
	mkdir ~/Repositorio
else
	echo "Diretorio já esta criado"
fi



