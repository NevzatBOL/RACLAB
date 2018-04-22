Armadillo Kurulumu için aşağıdaki tanimatları izleyiniz. Ubuntu 14 için uyumlu ROS INDIGO sürümü içindir.

    sudo apt-get update
    cd ~/catkin_ws/src
    git clone https://github.com/robotican/robotican.git
    cd ~/catkin_ws/src/robotican/robotican/setup
    chmod +x setup.sh
    ./setup.sh

Armadillo2 Kurulumu için aşağıdaki tanimatları izleyiniz. Ubuntu 16 için uyumlu ROS KINETIC sürümü içindir.

    sudo apt-get update
    cd ~/catkin_ws/src
    git clone https://github.com/robotican/armadillo2.git
    cd ~/catkin_ws/src/armadillo2/armadillo2
    ./setup.sh

Bu Tutorials'ta Armadillo2 üzerinden anlatım yapılacaktır.

Robotumuzu Gazebo simülasyon ortamında çalıştırmak için;
 
    roslaunch armadillo2 armadillo2.launch gazebo :=true
    
Robotun Gazebo ortamında açıldığı world'ü değiştirmek için;
  
    roscd armadillo2/launch
    gedit armadillo2.launch 

Launch dosyası içirisinde world_name satırı aşağıdaki gibi istenilen world dosyasının konumu ile değiştirilir.

    <arg name="world_name" default="$(find armadillo2_gazebo)/worlds/home.world"/> 

Robotumuzun kontrolünü cmd_vel'e yayın yaparak sağlayabiliriz. Robotun kontrolü için Twist tipinde ileri geri hareketi için linear.x ve dönme hareketi için anguler.z değerlerini kullanacağız. Bunun için;

    rostopic pub /cmd_vel geometry_msgs/Twist -r 10 -- '[0.3, 0.0, 0.0]' '[0.0, 0.0, -0.9]'
    
Robotun kontrolünü rqt üzerinden de görsel arayüzü kullanarak sağlayabiliriz. Bunun için;

    rqt
    Plugins->Robot Tools->Robot Steering  seçilir.
    Topic cmd_vel girilmelidir.
    
![rtq_robot_steering](https://github.com/raclab/RACLAB/blob/master/images/ROS/robot_steering.png)    




  
    

