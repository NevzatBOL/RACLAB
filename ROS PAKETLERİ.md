# ROS PAKETLERİ KULLANIMLARI VE KURULUMLARI

## ZED KAMERA
https://github.com/stereolabs/zed-ros-wrapper

Adresinden zed kamera paketi indirilir.

İlk olarak çalışma dizini oluşturalım.

    mkdir -p zed/src
    cd zed
    catkin_make
    source devel/setup.bash
    gedit ~/.bashrc
      source /home/nevzat/zed/devel/setup.bash
 
ROS için zed paketini githubdan çekelim.

    cd src
    git clone https://github.com/stereolabs/zed-ros-wrapper.git
    
    cd ..
    catkin_make

Zed kamerayı çalıştıralım.
 
    roslaunch zed_wrapper zed.launch

Kameradan gelen görüntüleri rqt de inceleyelim.

    rqt_image_view

Kameradan gelen görüntüleri incelemenin başka bir yolu;
   
    roscore
    rostopic list
    rosrun image_view image_view image:=/zed/rgb/image_raw_color
    
Zed kamerayı rviz de çalıştırabiliriz.
 
    roslaunch zed_wrapper display.launch
    
Rviz'de /depth/depth_registered derinlik değeri 8bit'dir bu değer `launch/zed_camera.launch` dosyasın da 
openni_depth_mode value=1 yapılarak 16bit yapılabilir.

    <param name="openni_depth_mode" value="1"/>
   
    

Birden fazla zed kullanma

    roslaunch zed_wrapper zed_multi_cam.launch
