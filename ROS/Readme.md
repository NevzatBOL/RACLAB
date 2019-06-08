# UDEMY EĞİTİMLERİM

**TÜM DERSLERE HER ZAMAN İNDİRİMLİ OLARAK ULAŞABİLİRSİNİZ**

**ALMAK İSTEDİĞİNİZ DERSİN ÜZERİNE TIKLAMANIZ YETERLİ**

**TÜM KURSLARDA GEÇERLİ İNDİRİM KUPONU: ROSINDIRIM2019**
 
[![beginner](https://github.com/NevzatBOL/Udemy_Discount/blob/master/image/ROS_Beginner.jpg?raw=true)](https://www.udemy.com/temel-ros-egitimi/?couponCode=ROSINDIRIM2019)
[![ModelOlusturma](https://github.com/NevzatBOL/Udemy_Discount/blob/master/image/ROS_Model_Olusturma.jpg?raw=true)](https://www.udemy.com/ros-ile-robot-modelleme/?couponCode=ROSINDIRIM2019)
[![Intermediate](https://github.com/NevzatBOL/Udemy_Discount/blob/master/image/ROS_Intermediate.png?raw=true)](https://www.udemy.com/uygulamalar-ile-ros-egitimi/?couponCode=ROSINDIRIM2019)

**Kursların tanıtım videoları**

**Temel ROS Eğitimi**

[![beginner](https://github.com/NevzatBOL/Udemy_Discount/blob/master/image/ROS_Beginner2.jpg?raw=true)](https://www.youtube.com/watch?v=K92_CLqbFT4)


**ROS - Urdf ve Xacro ile Robot Modelleme**

[![ModelOlusturma](https://github.com/NevzatBOL/Udemy_Discount/blob/master/image/ROS_Model_Olusturma2.jpg?raw=true)](https://www.youtube.com/watch?v=RHi-WnTi7lI)


**Uygulamalar ile ROS Eğitimi**

[![Intermediate](https://github.com/NevzatBOL/Udemy_Discount/blob/master/image/ROS_Intermediate2.jpg?raw=true)](https://www.youtube.com/watch?v=liDSuwpU2QE)


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
