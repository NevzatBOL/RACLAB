# ROS PAKETLERİ KULLANIMLARI VE KURULUMLARI

## ZED KAMERA
https://github.com/stereolabs/zed-ros-wrapper

Adresinden zed kamera paketi indirilir.

İlk olarak çalışma dizini oluşturalım.

    mkdir -p zed/src
    cd zed
    catkin_make
    source devel/setup.bach
    gedit ~/.bachrc
      source /home/nevzat/zed/devel/setup.bach
 
ROS için zed paketini githubdan çekelim.

    cd src
    git clone https://github.com/stereolabs/zed-ros-wrapper.git
    
    cd ..
    catkin_make
 
 zed kamerayı çalıştıralım.
 
     roslaunch zed_wrapper zed.launch
    
 zed kameradan gelen verileri rvizde çalıştıralım.
 
     roslaunch zed_wrapper display.launch

    
