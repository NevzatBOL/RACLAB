# ROS PAKETLERİ KULLANIMLARI VE KURULUMLARI

## ZED KAMERA
https://github.com/stereolabs/zed-ros-wrapper

Adresinden zed kamera paketi indirilir.

    mkdir -p zed/src
    cd zed
    catkin_make
    source devel/setup.bach
    gedit ~/.bachrc
      source /home/nevzat/zed/devel/setup.bach
 
    cd src
    git clone https://github.com/stereolabs/zed-ros-wrapper.git
 
    cd ..
    catkin_make
 
    roslaunch zed_wrapper zed.launch
    roslaunch zed_wrapper display.launch
