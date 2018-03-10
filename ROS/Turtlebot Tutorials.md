# Turtlebot  Tutorials

## Kurulum

İlk olarak Turtlebotu kuralım.

    sudo apt-get install ros-kinetic-turtlebot*
    
Turtlebot üzerinde kullacağımız kinect kamera sensörünün sürücüsünü kuralım.

    sudo apt-get install ros-kinetic-openni-*    
  
## Simülasyon

Turtlebot'u gazebo ortamında çalıştıralım.

    roslaunch turtlebot_gazebo turtlebot_world.launch
![turtlebot_wold](https://github.com/raclab/RACLAB/blob/master/images/ROS/sim_first_gazebo_launching.png)

Modelimizi rviz ortamında çalıştırarak kameradan alınan görüntüyü inceleyelim.
    
    roslaunch turtlebot_rviz_launchers view_robot.launch

DepthCloud seçeneğini aktif hale gerirerek kamera görüntüsü incelenebilir.
![Kinect depth](https://github.com/raclab/RACLAB/blob/master/images/ROS/simulated-kinect.png)

Klavye kullanılarak robotrumuzu simülasyon ortamında hareket ettirebiliriz.

    roslaunch turtlebot_teleop keyboard_teleop.launch
![Teleop Keyboard](https://github.com/raclab/RACLAB/blob/master/images/ROS/sim_teleop_keyboard.png)

Rviz ortamında robotumuzu görsel hareket ettirebileceğimiz Interactive Markers özelliğimizi çalıştırmak için yeni bir terminalde aşağıdaki kodu çalıştıralım.

    roslaunch turtlebot_interactive_markers interactive_markers.launch
    
rviz üzerinde Interactive Markers seçeneğini aktif edilir ve Interact seçilerek rviz üzerindeki ok tuşları kullanılarak robot yönlendirilebilir.
![inter makers](https://github.com/raclab/RACLAB/blob/master/images/ROS/sim_teleop_inter_markers.png)

Turtlebot ile haritalandırma yapalım.

ilk olarak gazebo dünyasını başlatalım.

    roslaunch turtlebot_gazebo turtlebot_world.launch 
Harita oluşturmak için gerekli paketimizi çalıştıralım.    

    roslaunch turtlebot_gazebo gmapping_demo.launch  
oluşturmaya başladığımız haritayı rviz ortamında görselleştirelim.

    roslaunch turtlebot_rviz_launchers view_navigation.launch
    
**Local map-> Costmap-> Topic 'i /map olarak ayarlayalım.**
![map](https://github.com/raclab/RACLAB/blob/master/images/ROS/sim_local_map_topic.png)

Robotun kontrolünü sağlamak için klavye kontrolünü açalım.

    roslaunch turtlebot_teleop keyboard_teleop.launch

![map](https://github.com/raclab/RACLAB/blob/master/images/ROS/sim_map.png)
oluşturduğumuz haritayı kaydedelim. tüm terminalleri durduralım.

    rosrun map_server map_saver -f test_map

Oluşturduğumuz harita üzerinde navigation yapalım.

ilk olarak gazebo dünyamızı tekrar açalım.

    roslaunch turtlebot_gazebo turtlebot_world.launch 
Navigation ı başlatalım.

    roslaunch turtlebot_gazebo amcl_demo.launch map_file:=~/test_map.yaml
Rviz'i başlatalım.

    roslaunch turtlebot_rviz_launchers view_navigation.launch


![default map](https://github.com/raclab/RACLAB/blob/master/images/ROS/sim_default_map.png)

**2D Nav Goal** seçeneğine tıklayın ve harita üzerinde robotun gideceği hedef noktayı seçin, turtlrbot bu noktaya otomatik olarak güzergah oluşturup kendisi gidecektir.



    
