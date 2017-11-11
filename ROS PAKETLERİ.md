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
    
Rviz'de /depth/depth_registered derinlik değeri metre cinsinden 8bit'dir, bu değer `launch/zed_camera.launch` dosyasın da 
openni_depth_mode value=1 yapılarak milimetre cinsinden 16bit yapılabilir.

    <param name="openni_depth_mode" value="1"/>
  
Derinlik ve noktasal bulut değeri varsayılan olarak 100 tanımlanmıştır. Bu değerde tüm derinlik değerleri, derinlik ve noktasal bulut'a yazılır. Belirli bir değerin altındaki değerleri filtrelemek için aşağıdaki komut kullanıla bilir. (80 varsayılan filtre değeridir.)
  
    rosrun dynamic_reconfigure dynparam set /zed/zed_wrapper_node confidence 80    

Birden fazla zed kullanma

    roslaunch zed_wrapper zed_multi_cam.launch
