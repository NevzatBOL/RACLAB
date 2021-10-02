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
