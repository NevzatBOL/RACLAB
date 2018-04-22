# Robotican - Armadillo

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

Farklı bir world üzerinde robotun açılması için;

    roslaunch armadillo2 armadillo2.launch gazebo:=true world_name:="`rospack find armadillo2_gazebo`/worlds/home.world"

Robotumuzun kontrolünü cmd_vel'e yayın yaparak sağlayabiliriz. Robotun kontrolü için Twist tipinde ileri geri hareketi için linear.x ve dönme hareketi için anguler.z değerlerini kullanacağız. Bunun için;

    rostopic pub /cmd_vel geometry_msgs/Twist -r 10 -- '[0.3, 0.0, 0.0]' '[0.0, 0.0, -0.9]'
    
Robotun kontrolünü rqt üzerinden de görsel arayüzü kullanarak sağlayabiliriz. Bunun için;

    rqt
    Plugins->Robot Tools->Robot Steering  seçilir.
    Topic cmd_vel girilmelidir.
    
![rtq_robot_steering](https://github.com/raclab/RACLAB/blob/master/images/ROS/robot_steering.png)    

Robotu joystic ile sürmek için;

    roslaunch armadillo2_teleop armadillo2_teleop.launch 

Robotun kontrolünü klavye üzerinden sağlamak için ilk olarak armedillo2_teleop/launch dizininde teleop.launch dosyası oluşturulur. oluşturulan bu dosyaya turtlebot için yazılmış klavye kontrol paketi çalıştırılır hale getirilir. Oluşturulan launch dosyası çalıştırılarak robotun klavye ile kontrolü sağlanabilir. *Bunun için turtlebot paketilerinin kurulu olması gerektiğini unutmayınız.*

    roscd armadillo2_teleop/launch
    gedit teleop.launch
    
    <?xml version="1.0"?>
    <launch>
      <!-- turtlebot_teleop_key already has its own built in velocity smoother -->
      <node pkg="turtlebot_teleop" type="turtlebot_teleop_key" name="turtlebot_teleop_keyboard"  output="screen">
        <param name="scale_linear" value="0.5" type="double"/>
        <param name="scale_angular" value="0.5" type="double"/>
        <remap from="turtlebot_teleop_keyboard/cmd_vel" to="cmd_vel"/>
      </node>
    </launch>
    
    roslaunch armadillo2_teleop teleop.launch 
    
Robotun başını hareket ettirmek için;

    rosservice call /services/pan_tilt_mover "pan: 0.0
    tilt: 0.0" 
    
    pan, kafanın sağa ve sola, titl ise kafanın yukarı ve aşağı kontrolünü sağlar.

Robotun gövdesinin aşağı veya yukarı hareketini sağlamak için;

    rostopic pub /torso_position_controller/command std_msgs/Float64 "data: 0.2" 
    
Robotun navigation yapması için;

    roslaunch armadillo2 armadillo2.launch gazebo:=true lidar:=true amcl:=true have_map:=true map:="`rospack find armadillo2_navigation`/maps/home.yaml" world_name:="`rospack find armadillo2_gazebo`/worlds/home.world" move_base:=true
    
     rosrun rviz rviz -d `rospack find armadillo2_navigation`/rviz/amcl.rviz

map:="`rospack find armadillo2_navigation`/maps/home.yaml" yerine başka bir harita çıkarılan map.yaml dosyası kullanılabilir.
world_name:="`rospack find armadillo2_gazebo`/worlds/home.world" çalıştırılmak istenilen dünya değiştirilebilir.

Navigation için 2D Nav Goal seçilerek harita üzerinde robotun yönlendirilmesi istenilen nokta ve yönü seçilerek robota navigation yaptırılabilir.

Robot Kol hareketini sağlamak için;
    
    roslaunch armadillo2 armadillo2.launch gazebo:=true moveit:=true
    rviz
    rviz -> Add -> MotionPlanning şeçilir.
    
![motionplanning](https://github.com/raclab/RACLAB/blob/master/images/ROS/motionplanning.png)    

Robot kolun rviz üzerinden kırmızı, yeşil ve mavi yön okları kullanılarak yönlendirilir. 

![arm](https://github.com/raclab/RACLAB/blob/master/images/ROS/robotic_arm_manipulation1.png)

![arm](https://github.com/raclab/RACLAB/blob/master/images/ROS/robotic_arm_manipulation2.png)

Yönlendirilen robot kol Motion Planning -> Planning sekmesi üzerinden Plan(1) ile simüle edilebilir veya execute(2) ile yönlendirilen konuma getirilebilir.

![Planning](https://github.com/raclab/RACLAB/blob/master/images/ROS/motionplanning_planning.png)

Robot Kol manipulasyonu, Joint trajectory contoller kullanılarak da gerçekleştirilebilir.
    
    roslaunch armadillo2 armadillo2.launch gazebo:=true
    rqt
    rqt -> Plugins -> Robot Tools -> Joint trajectory contoller 

![Joint contoller](https://github.com/raclab/RACLAB/blob/master/images/ROS/Joint_trajectory%20contoller.png)


Referans Link: http://wiki.ros.org/armadillo2
