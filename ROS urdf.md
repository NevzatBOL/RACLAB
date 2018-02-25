# URDF OLUŞTURMA

Çalışma alanı oluşturalım.

    mkdir -p model/src
    cd model

Çalışma alanını yapılandırıp ros ile bağlayalım.

    catkin_make
    source devel/setup.bash
    
    gedit ~/.bashrc 
      source /home/nevzat/model/devel/setup.bash
  
urdf, launch ve rviz için çalışma alanımızda dosyalar oluşturalım.

    cd ~model/src/
    catkin_create_pkg models
    cd models
    mkdir urdf
    mkdir launch
    mkdir rviz

urdf dosyamız ile model oluşturalım.

    roscd models/urdf
    gedit sekil.urdf
    
    <?xml version="1.0"?>
    <robot name="myfirst">
      <link name="base_link">
        <visual>
          <geometry>
            <cylinder length="0.6" radius="0.2"/>
          </geometry>
        </visual>
      </link>
    </robot>    
  
urdf dosyamızı rviz'e aktarmak için launch dosyamızı oluşturalım.

    roscd models/launch
    gedit view_urdf.launch
    
    <?xml version="1.0"?>
    <launch>
      <arg name="model" />
      <arg name="gui" default="false" />
      <!--arg name="rvizconfig" default="$(find models)/rviz/urdf.rviz" /-->

      <param name="robot_description" command="$(find xacro)/xacro.py $(find models)/urdf/$(arg model)" />
      <param name="use_gui" value="$(arg gui)"/>

      <node name="joint_state_publisher" pkg="joint_state_publisher" type="joint_state_publisher" />
        <node name="robot_state_publisher" pkg="robot_state_publisher" type="state_publisher" />

      <!--node name="rviz" pkg="rviz" type="rviz" args="-d $(arg rvizconfig)" required="true" /-->

    </launch>
    
yeni terminallerde launch dosyamızı ve rviz 'i çalıştıralım.
    
    roslaunch models view_urdf.launch model:=sekil.urdf
   
    rviz
    
    Fixed Frame base_link   olarak değiştirelim.
    Add seçeneği ile RobotModel ve TF 'yi ekleyelim.
    
    File -> save config as ile rvizi çalışma dizinimiz içerisindeki rviz klasörüne urdf.rviz ismi ile kaydedelim.
    
oluşturduğumuz launch dosyası içerisine girerek aşağıdaki sayırları yorum satırı olmaktan çıkaralım.

    <arg name="rvizconfig" default="$(find models)/rviz/urdf.rviz" />
    <node name="rviz" pkg="rviz" type="rviz" args="-d $(arg rvizconfig)" required="true" /> 
    
oluşturduğumuz dosyaları çalıştırmak artık daha kolay. 

    roslaunch models view_urdf.launch model:=sekil.urdf

    
    
    
check_urdf my_robot.urdf

urdf_to_graphiz my_robot.urdf
