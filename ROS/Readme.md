# UDEMY EĞİTİMLERİM

## Udemy Üzerinde yayınlamakta olduğum eğitimlerime aşadağıdaki indirim kuponlarını kullanarak ulaşabilirsiniz.

## Tüm Kurslarda Geçerli İndirim Kuponu: ROSINDIRIM2019

## Temel ROS Eğitimi

### [Udemy - Temel ROS Eğitimi İndirim Kuponu](https://www.udemy.com/temel-ros-egitimi/?couponCode=ROSINDIRIM2019)

### [Kursun Tanıtım Videosu](https://youtu.be/K92_CLqbFT4)

## ROS - Urdf ve Xacro ile Robot Modelleme

### [Udemy - ROS - Urdf ve Xacro ile Robot Modelleme Eğitimi İndirim Kuponu](https://www.udemy.com/ros-ile-robot-modelleme/?couponCode=ROSINDIRIM2019)

## Uygulamalar ile ROS Eğitimi

### [Uygulamalar ile ROS Eğitimi İndirim Kuponu](https://www.udemy.com/uygulamalar-ile-ros-egitimi/?couponCode=ROSINDIRIM2019)

# ROS KİNETİC KURULUMU

	sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

	sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

	sudo apt-get update


	sudo apt-get install ros-kinetic-desktop-full


	sudo rosdep init
	rosdep update


	echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
	source ~/.bashrc
	source /opt/ros/kinetic/setup.bash

	sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential

Referans Link:
http://wiki.ros.org/kinetic/Installation/Ubuntu
