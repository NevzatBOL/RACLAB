# Turtlebot  Tutorials

İlk olarak Turtlebotu kuralım.

    sudo apt-get install ros-kinetic-turtlebot*
    
Turtlebot üzerinde kullacağımız kinect kamera sensörünün sürücüsünü kuralım.

    sudo apt-get install ros-kinetic-openni-*    
    
Turtlebot'u gazebo ortamında çalıştıralım.

    roslaunch turtlebot_gazebo turtlebot_world.launch

Modelimizi rviz ortamında çalıştırarak kameradan alınan görüntüyü inceleyelim.
    
    roslaunch turtlebot_rviz_launchers view_robot.launch

DepthCloud seçeneğini aktif hale gerirerek kamera görüntüsü incelenebilir.

Klavye kullanılarak robotrumuzu simülasyon ortamında hareket ettirebiliriz.

    roslaunch turtlebot_teleop keyboard_teleop.launch
    
Rviz ortamında robotumuzu görsel hareket ettirebileceğimiz Interactive Markers özelliğimizi çalıştırmak için yeni bir terminalde aşağıdaki kodu çalıştıralım.

    roslaunch turtlebot_interactive_markers interactive_markers.launch
    
rviz üzerinde Interactive Markers seçeneğini aktif edilir ve Interact seçilerek rviz üzerindeki ok tuşları kullanılarak robot yönlendirilebilir.

