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

 ![sekil](https://github.com/raclab/RACLAB/blob/master/images/ROS/myfirst.png)   
 
 
 Şimdide birden fazla şekil oluşturma ve bu şekiller arası ilişkiyi görelim.
 
    roscd models/urdf
    gedit sekil2.urdf
    
    <?xml version="1.0"?>
    <robot name="multipleshapes">
      <link name="base_link">
        <visual>
          <geometry>
            <cylinder length="0.6" radius="0.2"/>
          </geometry>
        </visual>
      </link>

     <link name="right_leg">
        <visual>
          <geometry>
            <box size="0.6 0.1 0.2"/>
          </geometry>
        </visual>
      </link>

      <joint name="base_to_right_leg" type="fixed">
        <parent link="base_link"/>
        <child link="right_leg"/>
      </joint>

    </robot>
    
joint ile bir biri ile oluşturduğumuz şekillerin birbiri ile bağlantılı olduğunu tanımladık. right_leg nesnesi base_link nesnesinin alt elemanı olarak düşünülebilir.

oluşturduğumuz modeli çalıştıralım.
    
    roslaunch models view_urdf.launch model:=sekil2.urdf

![sekil2](https://github.com/raclab/RACLAB/blob/master/images/ROS/multipleshapes.png)

oluşturduğumuz iki nesneninde merkezleri aynı nokta idi robotumuzu şekillendirmek için oluşturduğumuz nesneleri birbirine bağlantılı olarak konumlandıralım.

    gedit sekil3.urdf
    
    <?xml version="1.0"?>
    <robot name="multipleshapes">
      <link name="base_link">
        <visual>
          <geometry>
            <cylinder length="0.6" radius="0.2"/>
          </geometry>
        </visual>
      </link>

     <link name="right_leg">
        <visual>
          <geometry>
            <box size="0.6 0.1 0.2"/>
          </geometry>
          <origin rpy="0 1.57075 0" xyz="0 0 -0.3" />
        </visual>
      </link>

      <joint name="base_to_right_leg" type="fixed">
        <parent link="base_link"/>
        <child link="right_leg"/>
        <origin xyz="0 -0.22 0.25"/>
      </joint>

    </robot>


oluşturduğumuz modeli çalıştıralım.

    roslaunch models view_urdf.launch model:=sekil3.urdf
    
![sekil3](https://github.com/raclab/RACLAB/blob/master/images/ROS/origins.png)

oluşturduğumuz parçalar aynı renkte oluşmuştu şimdi ise bu parçaları renklendirelim.

    gedit sekil4.urdf
    
    <?xml version="1.0"?>
    <robot name="materials">

     <material name="blue">
        <color rgba="0 0 0.8 1"/>
     </material>

     <material name="white">
        <color rgba="1 1 1 1"/>
     </material>

     <link name="base_link">
        <visual>
          <geometry>
            <cylinder length="0.6" radius="0.2"/>
          </geometry>
          <material name="blue"/>
        </visual>
     </link>

     <link name="right_leg">
        <visual>
          <geometry>
            <box size="0.6 0.1 0.2"/>
          </geometry>
          <origin rpy="0 1.57075 0" xyz="0 0 -0.3" />
          <material name="white"/>
        </visual>
      </link>

      <joint name="base_to_right_leg" type="fixed">
        <parent link="base_link"/>
        <child link="right_leg"/>
        <origin xyz="0 -0.22 0.25"/>
      </joint>

      <link name="left_leg">
        <visual>
          <geometry>
            <box size="0.6 0.1 0.2"/>
          </geometry>
          <origin rpy="0 1.57075 0" xyz="0 0 -0.3" />
          <material name="white"/>
        </visual>
      </link>

      <joint name="base_to_left_leg" type="fixed">
        <parent link="base_link"/>
        <child link="left_leg"/>
        <origin xyz="0 0.22 0.25"/>
      </joint>

    </robot>


oluşturduğumuz modeli çalıştıralım.

    roslaunch models view_urdf.launch model:=sekil4.urdf
    
![sekil4](https://github.com/raclab/RACLAB/blob/master/images/ROS/materials.png)   


oluşturduğumuz modele birkaç ekleme daha yaparak tamamlayalım.

    gedit sekil5.urdf
    
    <?xml version="1.0"?>
    <robot name="visual">

     <!-- Renk meteryallerini tanimladik -->
     <material name="blue">
        <color rgba="0 0 0.8 1"/>
     </material>

     <material name="black">
        <color rgba="0 0 0 1"/>
     </material>

     <material name="white">
        <color rgba="1 1 1 1"/>
     </material>

     <!-- Robotun gonvesini silindirden olusturduk -->
     <link name="base_link">
        <visual>
          <geometry>
            <cylinder length="0.6" radius="0.2"/>
          </geometry>
          <material name="blue"/>
        </visual>
     </link>

     <!-- Robotun sag bacagini olusturduk -->
     <link name="right_leg">
        <visual>
          <geometry>
            <box size="0.6 0.1 0.2"/>
          </geometry>
          <origin rpy="0 1.57075 0" xyz="0 0 -0.3" />
          <material name="white"/>
        </visual>
     </link>

     <!-- Robotun govdesine sag bacagini birlestirdik -->
     <joint name="base_to_right_leg" type="fixed">
        <parent link="base_link"/>
        <child link="right_leg"/>
        <origin xyz="0 -0.22 0.25"/>
     </joint>

     <!-- Robotun sag ayagini olusturduk -->
     <link name="right_base">
        <visual>
          <geometry>
            <box size="0.4 0.1 0.1"/>
          </geometry>
          <material name="white"/>
        </visual>
     </link>

     <!-- Robotun sag bacagina ayagini birlestirdik -->
     <joint name="right_base_joint" type="fixed">
        <parent link="right_leg"/>
        <child link="right_base"/>
        <origin xyz="0 0 -0.6"/>
     </joint>

     <!-- Robotun sag on tekerlerini olusturduk -->
     <link name="right_front_wheel">
        <visual>
          <origin rpy="1.57075 0 0" xyz="0 0 0"/>
          <geometry>
            <cylinder length="0.1" radius="0.035"/>
          </geometry>
          <material name="black"/>
          <origin rpy="0 0 0" xyz="0 0 0"/>
        </visual>
     </link>

     <!-- Robotun sag ayagina on tekerlerini birlestirdik -->
     <joint name="right_front_wheel_joint" type="fixed">
        <parent link="right_base"/>
        <child link="right_front_wheel"/>
        <origin rpy="0 0 0" xyz="0.133333333333 0 -0.085"/>
     </joint>

     <!-- Robotun sag arka tekerlerini olusturduk -->
     <link name="right_back_wheel">
        <visual>
          <origin rpy="1.57075 0 0" xyz="0 0 0"/>
          <geometry>
            <cylinder length="0.1" radius="0.035"/>
          </geometry>
          <material name="black"/>
        </visual>
     </link>

     <!-- Robotun sag ayagina arka tekerlerini birlestirdik -->
     <joint name="right_back_wheel_joint" type="fixed">
        <parent link="right_base"/>
        <child link="right_back_wheel"/>
        <origin rpy="0 0 0" xyz="-0.133333333333 0 -0.085"/>
     </joint>


     <!-- Robotun sol bacagini olusturduk -->
     <link name="left_leg">
        <visual>
          <geometry>
            <box size="0.6 0.1 0.2"/>
          </geometry>
          <origin rpy="0 1.57075 0" xyz="0 0 -0.3"/>
          <material name="white"/>
        </visual>
     </link>

     <!-- Robotun govdesine sol bacagini birlestirdik -->
     <joint name="base_to_left_leg" type="fixed">
        <parent link="base_link"/>
        <child link="left_leg"/>
        <origin xyz="0 0.22 0.25"/>
     </joint>

     <!-- Robotun sol ayagini olusturduk -->
     <link name="left_base">
        <visual>
          <geometry>
            <box size="0.4 0.1 0.1"/>
          </geometry>
          <material name="white"/>
        </visual>
     </link>

     <!-- Robotun sol bacagina ayagini birlestirdik -->
     <joint name="left_base_joint" type="fixed">
        <parent link="left_leg"/>
        <child link="left_base"/>
        <origin xyz="0 0 -0.6"/>
     </joint>

     <!-- Robotun sol on tekerlerini olusturduk -->
     <link name="left_front_wheel">
        <visual>
          <origin rpy="1.57075 0 0" xyz="0 0 0"/>
          <geometry>
            <cylinder length="0.1" radius="0.035"/>
          </geometry>
          <material name="black"/>
        </visual>
     </link>

     <!-- Robotun sol ayagina on tekerlerini birlestirdik -->
     <joint name="left_front_wheel_joint" type="fixed">
        <parent link="left_base"/>
        <child link="left_front_wheel"/>
        <origin rpy="0 0 0" xyz="0.133333333333 0 -0.085"/>
     </joint>

     <!-- Robotun sol arka tekerlerini olusturduk -->
     <link name="left_back_wheel">
        <visual>
          <origin rpy="1.57075 0 0" xyz="0 0 0"/>
          <geometry>
            <cylinder length="0.1" radius="0.035"/>
          </geometry>
          <material name="black"/>
        </visual>
     </link>

     <!-- Robotun sol ayagina arka tekerlerini birlestirdik -->
     <joint name="left_back_wheel_joint" type="fixed">
        <parent link="left_base"/>
        <child link="left_back_wheel"/>
        <origin rpy="0 0 0" xyz="-0.133333333333 0 -0.085"/>
     </joint>

     <!-- Gripper kolu olusturduk -->
     <link name="gripper_pole">
        <visual>
          <geometry>
            <cylinder length="0.2" radius="0.02"/>
          </geometry>
          <material name="white"/>
          <origin rpy="0 1.57075 0 " xyz="0.1 0 0"/>
        </visual>
     </link>

     <!-- Robotun govdesine gripper kolunu birlestirdik -->
     <joint name="gripper_extension" type="fixed">
        <parent link="base_link"/>
        <child link="gripper_pole"/>
        <origin rpy="0 0 0" xyz="0.19 0 0.2"/>
     </joint>

     <!-- Gripperin solidworks cizimlerini yukledik -->
     <link name="left_gripper">
        <visual>
          <origin rpy="0.0 0 0" xyz="0 0 0"/>
          <geometry>
            <mesh filename="package://urdf_tutorial/meshes/l_finger.dae"/>
          </geometry>
        </visual>
     </link>

     <joint name="left_gripper_joint" type="fixed">
        <origin rpy="0 0 0" xyz="0.2 0.01 0"/>
        <parent link="gripper_pole"/>
        <child link="left_gripper"/>
     </joint>

     <link name="left_tip">
        <visual>
          <origin rpy="0.0 0 0" xyz="0.09137 0.00495 0"/>
          <geometry>
            <mesh filename="package://urdf_tutorial/meshes/l_finger_tip.dae"/>
          </geometry>
        </visual>
     </link>

     <joint name="left_tip_joint" type="fixed">
        <parent link="left_gripper"/>
        <child link="left_tip"/>
     </joint>

     <link name="right_gripper">
        <visual>
          <origin rpy="-3.1415 0 0" xyz="0 0 0"/>
          <geometry>
            <mesh filename="package://urdf_tutorial/meshes/l_finger.dae"/>
          </geometry>
        </visual>
     </link>

     <joint name="right_gripper_joint" type="fixed">
        <origin rpy="0 0 0" xyz="0.2 -0.01 0"/>
        <parent link="gripper_pole"/>
        <child link="right_gripper"/>
     </joint>

     <link name="right_tip">
        <visual>
          <origin rpy="-3.1415 0 0" xyz="0.09137 0.00495 0"/>
          <geometry>
            <mesh filename="package://urdf_tutorial/meshes/l_finger_tip.dae"/>
          </geometry>
        </visual>
     </link>

     <joint name="right_tip_joint" type="fixed">
        <parent link="right_gripper"/>
        <child link="right_tip"/>
     </joint>

     <!-- Robotun kafasini olusturduk -->
     <link name="head">
        <visual>
          <geometry>
            <sphere radius="0.2"/>
          </geometry>
          <material name="white"/>
        </visual>
     </link>

     <!-- Robotun govdesine kafasini birlestirdik -->
     <joint name="head_swivel" type="fixed">
        <parent link="base_link"/>
        <child link="head"/>
        <origin xyz="0 0 0.3"/>
     </joint>

     <link name="box">
        <visual>
          <geometry>
            <box size="0.08 0.08 0.08"/>
          </geometry>
          <material name="blue"/>
        </visual>
     </link>

     <joint name="tobox" type="fixed">
        <parent link="head"/>
        <child link="box"/>
        <origin xyz="0.16 0 0.1"/>
     </joint>

    </robot>
    
 
oluşturduğumuz modeli çalıştıralım.

    roslaunch models view_urdf.launch model:=sekil5.urdf
![sekil5](https://github.com/raclab/RACLAB/blob/master/images/ROS/visual.png)    

# Hareketli Model

Sabit ve hareketli olmak üzere fakrlı eklem türleri vardır. ilk yaptığımız örneklerde oluşturduğumuz eklemler sabitti şimdi ise hareketli eklemler oluşturarak modelimizin nasıl hareket ettiğini görelim.

Continuous - Sürekli Eklemler

Herhangi bir eksen üzerinde negatif ve pozitif yönde sınırsız dönenbilen eklemlerdir.

    <joint name="head_swivel" type="continuous">
      <parent link="base_link"/>
      <child link="head"/>
      <axis xyz="0 0 1"/>
      <origin xyz="0 0 0.3"/>
    </joint>


Revolute - Dönen Eklemler

Herhangi bir eksen üzerinde belirli açı değerleri arasında dönenbilen eklemlerdir.

    <joint name="left_gripper_joint" type="revolute">
      <axis xyz="0 0 1"/>
      <limit effort="1000.0" lower="0.0" upper="0.548" velocity="0.5"/>
      <origin rpy="0 0 0" xyz="0.2 0.01 0"/>
      <parent link="gripper_pole"/>
      <child link="left_gripper"/>
    </joint>
    
Prismatic  Eklemler

Tek bir eksen üzerinde düz hareket edebilen eklemlerdir.

    <joint name="gripper_extension" type="prismatic">
      <parent link="base_link"/>
      <child link="gripper_pole"/>
      <limit effort="1000.0" lower="-0.38" upper="0" velocity="0.5"/>
      <origin rpy="0 0 0" xyz="0.19 0 0.2"/>
    </joint>

Son oluşturduğumuz modeli hareket edebilir şekilde düzenleyelim.

    roscd models/urdf
    gedit sekil6.urdf
    
    <?xml version="1.0"?>
    <robot name="visual">

     <!-- Renk meteryallerini tanimladik -->
     <material name="blue">
        <color rgba="0 0 0.8 1"/>
     </material>

     <material name="black">
        <color rgba="0 0 0 1"/>
     </material>

     <material name="white">
        <color rgba="1 1 1 1"/>
     </material>

     <!-- Robotun gonvesini silindirden olusturduk -->
     <link name="base_link">
        <visual>
          <geometry>
            <cylinder length="0.6" radius="0.2"/>
          </geometry>
          <material name="blue"/>
        </visual>
     </link>

     <!-- Robotun sag bacagini olusturduk -->
     <link name="right_leg">
        <visual>
          <geometry>
            <box size="0.6 0.1 0.2"/>
          </geometry>
          <origin rpy="0 1.57075 0" xyz="0 0 -0.3" />
          <material name="white"/>
        </visual>
     </link>

     <!-- Robotun govdesine sag bacagini birlestirdik -->
     <joint name="base_to_right_leg" type="fixed">
        <parent link="base_link"/>
        <child link="right_leg"/>
        <origin xyz="0 -0.22 0.25"/>
     </joint>

     <!-- Robotun sag ayagini olusturduk -->
     <link name="right_base">
        <visual>
          <geometry>
            <box size="0.4 0.1 0.1"/>
          </geometry>
          <material name="white"/>
        </visual>
     </link>

     <!-- Robotun sag bacagina ayagini birlestirdik -->
     <joint name="right_base_joint" type="fixed">
        <parent link="right_leg"/>
        <child link="right_base"/>
        <origin xyz="0 0 -0.6"/>
     </joint>

     <!-- Robotun sag on tekerlerini olusturduk -->
     <link name="right_front_wheel">
        <visual>
          <origin rpy="1.57075 0 0" xyz="0 0 0"/>
          <geometry>
            <cylinder length="0.1" radius="0.035"/>
          </geometry>
          <material name="black"/>
          <origin rpy="0 0 0" xyz="0 0 0"/>
        </visual>
     </link>

     <!-- Robotun sag ayagina on tekerlerini birlestirdik -->
     <joint name="right_front_wheel_joint" type="continuous">
        <parent link="right_base"/>
        <child link="right_front_wheel"/>
        <axis xyz="0 1 0"/>
        <origin rpy="0 0 0" xyz="0.133333333333 0 -0.085"/>
     </joint>

     <!-- Robotun sag arka tekerlerini olusturduk -->
     <link name="right_back_wheel">
        <visual>
          <origin rpy="1.57075 0 0" xyz="0 0 0"/>
          <geometry>
            <cylinder length="0.1" radius="0.035"/>
          </geometry>
          <material name="black"/>
        </visual>
     </link>

     <!-- Robotun sag ayagina arka tekerlerini birlestirdik -->
     <joint name="right_back_wheel_joint" type="continuous">
        <parent link="right_base"/>
        <child link="right_back_wheel"/>
        <axis xyz="0 1 0"/>
        <origin rpy="0 0 0" xyz="-0.133333333333 0 -0.085"/>
     </joint>


     <!-- Robotun sol bacagini olusturduk -->
     <link name="left_leg">
        <visual>
          <geometry>
            <box size="0.6 0.1 0.2"/>
          </geometry>
          <origin rpy="0 1.57075 0" xyz="0 0 -0.3"/>
          <material name="white"/>
        </visual>
     </link>

     <!-- Robotun govdesine sol bacagini birlestirdik -->
     <joint name="base_to_left_leg" type="fixed">
        <parent link="base_link"/>
        <child link="left_leg"/>
        <origin xyz="0 0.22 0.25"/>
     </joint>

     <!-- Robotun sol ayagini olusturduk -->
     <link name="left_base">
        <visual>
          <geometry>
            <box size="0.4 0.1 0.1"/>
          </geometry>
          <material name="white"/>
        </visual>
     </link>

     <!-- Robotun sol bacagina ayagini birlestirdik -->
     <joint name="left_base_joint" type="fixed">
        <parent link="left_leg"/>
        <child link="left_base"/>
        <origin xyz="0 0 -0.6"/>
     </joint>

     <!-- Robotun sol on tekerlerini olusturduk -->
     <link name="left_front_wheel">
        <visual>
          <origin rpy="1.57075 0 0" xyz="0 0 0"/>
          <geometry>
            <cylinder length="0.1" radius="0.035"/>
          </geometry>
          <material name="black"/>
        </visual>
     </link>

     <!-- Robotun sol ayagina on tekerlerini birlestirdik -->
     <joint name="left_front_wheel_joint" type="continuous">
        <parent link="left_base"/>
        <child link="left_front_wheel"/>
        <axis xyz="0 1 0"/>
        <origin rpy="0 0 0" xyz="0.133333333333 0 -0.085"/>
     </joint>

     <!-- Robotun sol arka tekerlerini olusturduk -->
     <link name="left_back_wheel">
        <visual>
          <origin rpy="1.57075 0 0" xyz="0 0 0"/>
          <geometry>
            <cylinder length="0.1" radius="0.035"/>
          </geometry>
          <material name="black"/>
        </visual>
     </link>

     <!-- Robotun sol ayagina arka tekerlerini birlestirdik -->
     <joint name="left_back_wheel_joint" type="continuous">
        <parent link="left_base"/>
        <child link="left_back_wheel"/>
        <axis xyz="0 1 0"/>
        <origin rpy="0 0 0" xyz="-0.133333333333 0 -0.085"/>
     </joint>

     <!-- Gripper kolu olusturduk -->
     <link name="gripper_pole">
        <visual>
          <geometry>
            <cylinder length="0.2" radius="0.02"/>
          </geometry>
          <material name="white"/>
          <origin rpy="0 1.57075 0 " xyz="0.1 0 0"/>
        </visual>
     </link>

     <!-- Robotun govdesine gripper kolunu birlestirdik -->
     <joint name="gripper_extension" type="prismatic">
        <parent link="base_link"/>
        <child link="gripper_pole"/>
        <limit effort="1000.0" lower="-0.15" upper="0" velocity="0.5"/>
        <origin rpy="0 0 0" xyz="0.19 0 0.2"/>
     </joint>

     <!-- Gripperin solidworks cizimlerini yukledik -->
     <link name="left_gripper">
        <visual>
          <origin rpy="0.0 0 0" xyz="0 0 0"/>
          <geometry>
            <mesh filename="package://urdf_tutorial/meshes/l_finger.dae"/>
          </geometry>
        </visual>
     </link>

     <joint name="left_gripper_joint" type="revolute">
        <axis xyz="0 0 1"/>
        <limit effort="1000.0" lower="0.0" upper="0.548" velocity="0.5"/>
        <origin rpy="0 0 0" xyz="0.2 0.01 0"/>
        <parent link="gripper_pole"/>
        <child link="left_gripper"/>
     </joint>

     <link name="left_tip">
        <visual>
          <origin rpy="0.0 0 0" xyz="0.09137 0.00495 0"/>
          <geometry>
            <mesh filename="package://urdf_tutorial/meshes/l_finger_tip.dae"/>
          </geometry>
        </visual>
     </link>

     <joint name="left_tip_joint" type="fixed">
        <parent link="left_gripper"/>
        <child link="left_tip"/>
     </joint>

     <link name="right_gripper">
        <visual>
          <origin rpy="-3.1415 0 0" xyz="0 0 0"/>
          <geometry>
            <mesh filename="package://urdf_tutorial/meshes/l_finger.dae"/>
          </geometry>
        </visual>
     </link>

     <joint name="right_gripper_joint" type="revolute">
        <axis xyz="0 0 -1"/>
        <limit effort="1000.0" lower="0.0" upper="0.548" velocity="0.5"/>
        <origin rpy="0 0 0" xyz="0.2 -0.01 0"/>
        <parent link="gripper_pole"/>
        <child link="right_gripper"/>
     </joint>

     <link name="right_tip">
        <visual>
          <origin rpy="-3.1415 0 0" xyz="0.09137 0.00495 0"/>
          <geometry>
            <mesh filename="package://urdf_tutorial/meshes/l_finger_tip.dae"/>
          </geometry>
        </visual>
     </link>

     <joint name="right_tip_joint" type="fixed">
        <parent link="right_gripper"/>
        <child link="right_tip"/>
     </joint>

     <!-- Robotun kafasini olusturduk -->
     <link name="head">
        <visual>
          <geometry>
            <sphere radius="0.2"/>
          </geometry>
          <material name="white"/>
        </visual>
     </link>

     <!-- Robotun govdesine kafasini birlestirdik -->
     <joint name="head_swivel" type="continuous">
        <parent link="base_link"/>
        <child link="head"/>
        <axis xyz="0 0 1"/>
        <origin xyz="0 0 0.3"/>
     </joint>

     <link name="box">
        <visual>
          <geometry>
            <box size="0.08 0.08 0.08"/>
          </geometry>
          <material name="blue"/>
        </visual>
     </link>

     <joint name="tobox" type="fixed">
        <parent link="head"/>
        <child link="box"/>
        <origin xyz="0.16 0 0.1"/>
     </joint>

    </robot>

Modelimizi çalıştırarak hareketlerini inceleyelim.

    roslaunch models view_urdf.launch model:=sekil6.urdf gui:=true

![sekil6](https://github.com/raclab/RACLAB/blob/master/images/ROS/flexible.png)

# Modelin Fiziksel Özeliklerinin Ve Çarpışma Özeliğinin Tanımlanması

**Çarpışma algılamasının çalışabilmesi için bir çarpışma ögesi tanımlanması gereklidir.**

    <link name="base_link">
      <visual>
        <geometry>
          <cylinder length="0.6" radius="0.2"/>
        </geometry>
        <material name="blue">
        <color rgba="0 0 .8 1"/>
        </material>
      </visual>
      <collision>
        <geometry>
          <cylinder length="0.6" radius="0.2"/>
        </geometry>
      </collision>
    </link>
    
Çarpışma ögesi bağlantılı nesnenin bir alt ögesidir. Bağlantılı nesne ile aynı şekilde tanımlanır.
Çarpışma ögesi çoğu durum için bağlantılı nesne ile aynı boyutlarda olurken bazı durumlarda hassas ekipmanları korumak için bir koruma alanı oluşturacak şekilde tanımlanabilir. Çarpma algılamanın daha hızlı çalışabilmesi için bağlantılı nesnelerin karmaşık geometrilerini kullanmak yerine daha basit geometrik şekiller kullanılarak tanımlanabilir.

**Modelin doğru şekilde taklit edilebilmesi için robotun çeşitli fiziksel özelliklerinin tanımlanması gerekir.**

    <link name="base_link">
      <visual>
        <geometry>
          <cylinder length="0.6" radius="0.2"/>
        </geometry>
        <material name="blue">
          <color rgba="0 0 .8 1"/>
        </material>
      </visual>
      <collision>
        <geometry>
          <cylinder length="0.6" radius="0.2"/>
        </geometry>
      </collision>
      <inertial>
        <mass value="10"/>
        <inertia ixx="0.4" ixy="0.0" ixz="0.0" iyy="0.4" iyz="0.0" izz="0.2"/>
      </inertial>
    </link>

Bu ögede bağlantı nesnesinin alt ögesidir. 

**mass(kütle)** kilogram olarak tanımlanır.

**inertial(hareketsizlik)** 3x3'lük atalet matrisi ile belirtilir. Bu bilgi 3 boyutlu modelleme programı ile sağlanabilir yada basit geometriler için [atalet momentleri listesi](http://www.wiki-zero.com/index.php?q=aHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvTGlzdF9vZl9tb21lbnRfb2ZfaW5lcnRpYV90ZW5zb3Jz) kullanılabilir.

Atalet momenti cismin kütlesine ve dağılımına bağlıdır. 

**Temas katsayıları**

bağlantıların birbirleri ile temas halinde nasıl davrandıkları tanımlanabilir. 
Bu tanımlama çarpışma etiketinin alt ögesi olan contact_coefficients ile yapılabilir. 

Temas katsayısı tanımlanırken; 

**mu** - Sürtünme katsayısı

**kp** - Sertlik katsayısı

**kd** - Sönümleme katsayısı

bu üç nitelik belirtilir.

**Ortak dinamikler**

Eklem hareketleri, eklem için dinamik hareketler ile tanımlanır. Burada iki nitelik vardır.

**sürtünme** - Fiziksel statik sürtünme. Prizmatik derzlerde birimler Newton'dur. Dönen eklemler için birimler Newton metredir.

**sönüm** - Fiziksel sönümleme değeri. Prizmatik derzlerde birimler metre başına Newton saniyedir. Dönen eklemler için, radyan başına Newton metre saniyedir.

**Enson oluşturduğumuz modele çarpışma ve fiziksel özellikleri [burada](https://github.com/ros/urdf_tutorial/blob/master/urdf/07-physics.urdf) olduğu gibi ekleyebiliriz.**

# URDF Dosyasını XACRO İle Kısaltma

ilk olarak xacro ile yaptığımız modeli çalıştırabileceğimiz launch dosyamızı oluşturalım.
    
    roscd models/launch
    gedit view_xacro.lauch
    
    <?xml version="1.0"?>
    <launch>
        <arg name="model" />
        <arg name="gui" default="false" />
        <arg name="rvizconfig" default="$(find models)/rviz/urdf.rviz" />

        <param name="robot_description" command="$(find xacro)/xacro $(find models)/urdf/$(arg model)" />
        <param name="use_gui" value="$(arg gui)"/>

        <node name="joint_state_publisher" pkg="joint_state_publisher" type="joint_state_publisher" />
        <node name="robot_state_publisher" pkg="robot_state_publisher" type="state_publisher" />

        <node name="rviz" pkg="rviz" type="rviz" args="-d $(arg rvizconfig)" required="true" />
    </launch>

Xacro ile değişken oluşturarak modelimizi değiştirilmesi daha kolay ve daha kısa hale getirebiliriz.

    <?xml version="1.0"?>
    <robot name="myfirst" xmlns:xacro="http://ros.org/wiki/xacro">

      <xacro:property name="width" value="0.2" />
      <xacro:property name="bodylen" value="0.6" />
      <link name="base_link">
          <visual>
              <geometry>
                  <cylinder radius="${width}" length="${bodylen}"/>
              </geometry>
          </visual>
          <collision>
              <geometry>
                  <cylinder radius="${width}" length="${bodylen}"/>
              </geometry>
          </collision>
      </link>
    </robot>

sadece urdf olarak yazdığımız dosyada silindirin boyunu ve yarıçapını değiştirmek isteseydik iki yerde de aynı değişiklikleri yapmak zorunda kalacaktır. xacro ile değişken olarak tanımlamamız değişiklik yapmak istediğimiz durumlarda işimizi kolaylaştırır.

ayrıca değişkenler sonradan değiştirilmeye ve ekleme yapılmasına olanak tanır.

    <xacro:property name=”robotname” value=”marvin” />
    <link name=”${robotname}s_leg” />
    
    Çıktı aşağıdaki gibi olacaktır.
    <link name=”marvins_leg” />

farklı matematiksel işlemler yapmamızada olanak tanır.

    <cylinder radius="${wheeldiam/2}" length="0.1"/>
    <origin xyz="${reflect*(width+.02)} 0 0.25" />

    <link name="${5/6}"/>
    Çıktı;
    <link name="0.833333333333"/>
    
Makrolar tanımlanarak aynı etiketleri tekrar oluşturmaya gerek kalmayacak şekilde tanımlanarak kullanılabilir.

    <xacro:macro name="default_inertial" params="mass">
        <inertial>
                <mass value="${mass}" />
                <inertia ixx="1.0" ixy="0.0" ixz="0.0"
                     iyy="1.0" iyz="0.0"
                     izz="1.0" />
        </inertial>
    </xacro:macro>    
    
oluşturulan makro aşağıdaki kod ile kullanılabilir.

    <xacro:default_inertial mass="10"/>
   
Tüm bloglarda parmetre olarak kullanılabilir.

    <xacro:macro name="blue_shape" params="name *shape">
        <link name="${name}">
            <visual>
                <geometry>
                    <xacro:insert_block name="shape" />
                </geometry>
                <material name="blue"/>
            </visual>
            <collision>
                <geometry>
                    <xacro:insert_block name="shape" />
                </geometry>
            </collision>
        </link>
    </xacro:macro> 

Bir blok parametresi belirtmek için, parametre adından önce bir yıldız eklenir. 

Bir blok, insert_block komutu kullanılarak eklenebilir

Oluşturduğumuz blogu aşağıdaki gibi kullanabiliriz. 

    <xacro:blue_shape name="base_link">
        <cylinder radius=".42" length=".01" />
    </xacro:blue_shape>   
 
Şimdi ise urdf ile olusturdugumuz modelimizi xacro kullanarak daha kullanışlı hale getirelim.

    roscd models/urdf
    gedit sekil8.urdf.xacro

    <?xml version="1.0"?>
    <robot name="macroed" xmlns:xacro="http://ros.org/wiki/xacro">

      <!-- Kullanacagimiz degiskenleri tanimladik -->
      <xacro:property name="width" value="0.2" />
      <xacro:property name="leglen" value="0.6" />
      <xacro:property name="polelen" value="0.2" />
      <xacro:property name="bodylen" value="0.6" />
      <xacro:property name="baselen" value="0.4" />
      <xacro:property name="wheeldiam" value="0.07" />
      <xacro:property name="pi" value="3.1415" />

      <!-- Renk materyallerini tanimladik -->
      <material name="blue">
        <color rgba="0 0 0.8 1"/>
      </material>

      <material name="black">
        <color rgba="0 0 0 1"/>
      </material>

      <material name="white">
        <color rgba="1 1 1 1"/>
      </material>


      <!-- Fiziksel degerler blogunu makro olarak tanimladik -->
      <xacro:macro name="default_inertial" params="mass">
        <inertial>
          <mass value="${mass}" />
          <inertia ixx="1.0" ixy="0.0" ixz="0.0" iyy="1.0" iyz="0.0" izz="1.0" />
        </inertial>
      </xacro:macro>


     <!-- Robotumuzun govdesini olusturalim -->
      <link name="base_link">
        <visual>
          <geometry>
            <cylinder radius="${width}" length="${bodylen}"/>
          </geometry>
          <material name="blue"/>
        </visual>
        <collision>
          <geometry>
            <cylinder radius="${width}" length="${bodylen}"/>
          </geometry>
        </collision>
        <xacro:default_inertial mass="10"/>
      </link>

      <!-- Tekerler icin makro blogu tanimladik -->
      <xacro:macro name="wheel" params="prefix suffix reflect">
        <link name="${prefix}_${suffix}_wheel">
          <visual>
            <origin xyz="0 0 0" rpy="${pi/2} 0 0" />
            <geometry>
              <cylinder radius="${wheeldiam/2}" length="0.1"/>
            </geometry>
            <material name="black"/>
          </visual>
          <collision>
            <origin xyz="0 0 0" rpy="${pi/2} 0 0" />
            <geometry>
              <cylinder radius="${wheeldiam/2}" length="0.1"/>
            </geometry>
          </collision>
          <xacro:default_inertial mass="1"/>
        </link>
        <joint name="${prefix}_${suffix}_wheel_joint" type="continuous">
          <axis xyz="0 1 0" rpy="0 0 0" />
          <parent link="${prefix}_base"/>
          <child link="${prefix}_${suffix}_wheel"/>
          <origin xyz="${baselen*reflect/3} 0 -${wheeldiam/2+.05}" rpy="0 0 0"/>
        </joint>
      </xacro:macro>

      <!-- bacaklar ve ayaklar icin makro blogu tanimladik -->
      <xacro:macro name="leg" params="prefix reflect">
        <link name="${prefix}_leg">
          <visual>
            <geometry>
              <box size="${leglen} 0.1 0.2"/>
            </geometry>
            <origin xyz="0 0 -${leglen/2}" rpy="0 ${pi/2} 0"/>
            <material name="white"/>
          </visual>
          <collision>
            <geometry>
              <box size="${leglen} 0.1 0.2"/>
            </geometry>
            <origin xyz="0 0 -${leglen/2}" rpy="0 ${pi/2} 0"/>
          </collision>
          <xacro:default_inertial mass="10"/>
        </link>

        <joint name="base_to_${prefix}_leg" type="fixed">
          <parent link="base_link"/>
          <child link="${prefix}_leg"/>
          <origin xyz="0 ${reflect*(width+.02)} 0.25" />
        </joint>

        <link name="${prefix}_base">
          <visual>
            <geometry>
              <box size="${baselen} 0.1 0.1"/>
            </geometry>
            <material name="white"/>
          </visual>
          <collision>
            <geometry>
              <box size="${baselen} 0.1 0.1"/>
            </geometry>
          </collision>
          <xacro:default_inertial mass="10"/>
        </link>

        <joint name="${prefix}_base_joint" type="fixed">
          <parent link="${prefix}_leg"/>
          <child link="${prefix}_base"/>
          <origin xyz="0 0 ${-leglen}" />
        </joint>

        <!-- Tekerleri ekledik -->
        <xacro:wheel prefix="${prefix}" suffix="front" reflect="1"/>
        <xacro:wheel prefix="${prefix}" suffix="back" reflect="-1"/>
      </xacro:macro>

      <!-- bacaklaro ve ayaklari ekledik -->
      <xacro:leg prefix="right" reflect="-1" />
      <xacro:leg prefix="left" reflect="1" />


      <!-- Gripper kolu ekledik -->
      <joint name="gripper_extension" type="prismatic">
        <parent link="base_link"/>
        <child link="gripper_pole"/>
        <limit effort="1000.0" lower="-${width-.05}" upper="0" velocity="0.5"/>
        <origin rpy="0 0 0" xyz="${width-.01} 0 0.2"/>
      </joint>

      <link name="gripper_pole">
        <visual>
          <geometry>
            <cylinder length="${polelen}" radius="0.02"/>
          </geometry>
          <material name="white"/>
          <origin xyz="${polelen/2} 0 0" rpy="0 ${pi/2} 0 "/>
        </visual>
        <collision>
          <geometry>
            <cylinder length="${polelen}" radius="0.01"/>
          </geometry>
          <origin xyz="${polelen/2} 0 0" rpy="0 ${pi/2} 0 "/>
        </collision>
        <xacro:default_inertial mass="0.05"/>
      </link>


      <!-- Gripperi olusturmak icin makro tanimladik -->
      <xacro:macro name="gripper" params="prefix reflect">
        <joint name="${prefix}_gripper_joint" type="revolute">
          <axis xyz="0 0 ${reflect}"/>
          <limit effort="1000.0" lower="0.0" upper="0.548" velocity="0.5"/>
          <origin rpy="0 0 0" xyz="${polelen} ${reflect*0.01} 0"/>
          <parent link="gripper_pole"/>
          <child link="${prefix}_gripper"/>
        </joint>
        <link name="${prefix}_gripper">
          <visual>
            <origin rpy="${(reflect-1)/2*pi} 0 0" xyz="0 0 0"/>
            <geometry>
              <mesh filename="package://urdf_tutorial/meshes/l_finger.dae"/>
            </geometry>
          </visual>
          <collision>
            <geometry>
              <mesh filename="package://urdf_tutorial/meshes/l_finger.dae"/>
            </geometry>
            <origin rpy="${(reflect-1)/2*pi} 0 0" xyz="0 0 0"/>
          </collision>
          <xacro:default_inertial mass="0.05"/>
        </link>

        <joint name="${prefix}_tip_joint" type="fixed">
          <parent link="${prefix}_gripper"/>
          <child link="${prefix}_tip"/>
        </joint>
        <link name="${prefix}_tip">
          <visual>
            <origin rpy="${(reflect-1)/2*pi} 0 0" xyz="0.09137 0.00495 0"/>
            <geometry>
              <mesh filename="package://urdf_tutorial/meshes/l_finger_tip.dae"/>
            </geometry>
          </visual>
          <collision>
            <geometry>
              <mesh filename="package://urdf_tutorial/meshes/l_finger_tip.dae"/>
            </geometry>
            <origin rpy="${(reflect-1)/2*pi} 0 0" xyz="0.09137 0.00495 0"/>
          </collision>
          <xacro:default_inertial mass="0.05"/>
        </link>
      </xacro:macro>

      <!-- gripperin sag ve sol ceneyisini ekledik -->
      <xacro:gripper prefix="left" reflect="1" />
      <xacro:gripper prefix="right" reflect="-1" />


      <!-- Robotun kafasini ekledik -->
      <link name="head">
        <visual>
          <geometry>
            <sphere radius="${width}"/>
          </geometry>
          <material name="white"/>
        </visual>
        <collision>
          <geometry>
            <sphere radius="${width}"/>
          </geometry>
        </collision>
        <xacro:default_inertial mass="2"/>
      </link>

      <joint name="head_swivel" type="continuous">
        <parent link="base_link"/>
        <child link="head"/>
        <axis xyz="0 0 1"/>
        <origin xyz="0 0 ${bodylen/2}"/>
      </joint>

      <link name="box">
        <visual>
          <geometry>
            <box size="0.08 0.08 0.08"/>
          </geometry>
          <material name="blue"/>
          <origin xyz="-0.04 0 0"/>
        </visual>
        <collision>
          <geometry>
            <box size="0.08 0.08 0.08"/>
          </geometry>
        </collision>
        <xacro:default_inertial mass="1"/>
      </link>

      <joint name="tobox" type="fixed">
        <parent link="head"/>
        <child link="box"/>
        <origin xyz="${.707*width+0.04} 0 ${.707*width}"/>
      </joint>

    </robot>

oluşturduğumuz modeli çalıştıralım.

    roslaunch models view_xacro.launch model:=sekil8.urdf.xacro gui:=true

# Gazebo'da URDF Kullanma

ilk olarak oluşturduğumuz modeli çalıştırabileceğimiz bir launch dosyası oluşturmalıyız.

    roscd models/launch
    gedit gazebo.launch
    
    <?xml version="1.0"?>
    <launch>
      <arg name="paused" default="false"/>
      <arg name="use_sim_time" default="true"/>
      <arg name="gui" default="true"/>
      <arg name="headless" default="false"/>
      <arg name="debug" default="false"/>
      <arg name="model" default="$(find models)/urdf/sekil8.urdf.xacro"/>

      <include file="$(find gazebo_ros)/launch/empty_world.launch">
        <arg name="debug" value="$(arg debug)" />
        <arg name="gui" value="$(arg gui)" />
        <arg name="paused" value="$(arg paused)"/>
        <arg name="use_sim_time" value="$(arg use_sim_time)"/>
        <arg name="headless" value="$(arg headless)"/>
      </include>

      <param name="robot_description" command="$(find xacro)/xacro $(arg model)" />

      <node name="urdf_spawner" pkg="gazebo_ros" type="spawn_model"
            args="-z 1.0 -unpause -urdf -model robot -param robot_description" respawn="false" output="screen" />

      <node name="joint_state_publisher" pkg="joint_state_publisher" type="joint_state_publisher" />
      <node pkg="robot_state_publisher" type="robot_state_publisher"  name="robot_state_publisher">
        <param name="publish_frequency" type="double" value="30.0" />
      </node>
    </launch>

gazebo.launch dosyasını çalıştırarak oluşturduğumuz modelin gazebo ortamında hareketsiz bir versiyonunu görürüz.

    roslaunc models gazebo.launch

![gazebo](https://github.com/raclab/RACLAB/blob/master/images/ROS/pr2gazebo.png)

Şimdi de ROS'un Gazebo ile etkileşime girmesi için, Gazebo'ya ne yapılacağını söyleyen ROS kitaplığına dinamik olarak bağlantı kurmalıyız. Gazebo ve ROS'u birbirine bağlamak için oluşturmuş olduğumuz urdf dosyasının sonuna, aşağıdaki satırlar eklenir. [Burada](https://github.com/ros/urdf_sim_tutorial/blob/master/urdf/09-publishjoints.urdf.xacro#L238)

    <gazebo>
      <plugin name="gazebo_ros_control" filename="libgazebo_ros_control.so">
        <robotNamespace>/</robotNamespace>
        </plugin>
    </gazebo>
    
Artık ROS ve Gazebo'yu birbirine bağladık, Gazebo'da çalışmak istediğimiz, denetleyicilerini genel olarak adlandırdığımız bazı ROS kodu belirtmeliyiz.

Bunun için bir yaml dosyası oluştururuz.

    roscd models
    mkdir config
    cd config
    gedit joints.yaml
    
    type: "joint_state_controller/JointStateController"
    publish_rate: 50
    
Bu kontrol cihazı, joint_state_controller paketinde bulunur ve robot eklemlerin durumunu doğrudan Gazebo'dan ROS'a yayınlar.

oluşturduğumuz yaml dosyasını ve gazebo.launch dosyasını çalıştıracak yenibir launch dosyası oluşturalım.

    roscd models/launch
    gedit joints.launch
    
    <?xml version="1.0"?>
    <launch>
      <arg name="model" default="$(find models)/urdf/sekil9.urdf.xacro"/>
      <arg name="rvizconfig" default="$(find models)/rviz/urdf.rviz" />

      <include file="$(find models)/launch/gazebo.launch">
        <arg name="model" value="$(arg model)" />
      </include>

      <node name="rviz" pkg="rviz" type="rviz" args="-d $(arg rvizconfig)" />

      <rosparam command="load"
                file="$(find models)/config/joints.yaml"
                ns="r2d2_joint_state_controller" />

      <node name="r2d2_controller_spawner" pkg="controller_manager" type="spawner"
        args="r2d2_joint_state_controller
              --shutdown-timeout 3"/>
    </launch>

joints.launch dosyasını çalıştırıp joint_states konusunu dinlediğimizde bize robot eklemlerinin durumunu yayınlayacaktır fakat eklemleri halen tanımlamadığımız için çıktı boş olacaktır.

Her sabit olmayan eklem için, Gazebo'ya eklem ile ne yapılacağını bildiren bir iletim belirtmeliyiz. Kafa eklemiyle başlayalım. Son oluşturduğumuz urdf dosyasına aşağıdaki satırları ekleyelim. [Burda](https://github.com/ros/urdf_sim_tutorial/blob/master/urdf/10-firsttransmission.urdf.xacro#L216)

    <transmission name="head_swivel_trans">
      <type>transmission_interface/SimpleTransmission</type>
      <actuator name="$head_swivel_motor">
        <mechanicalReduction>1</mechanicalReduction>
      </actuator>
      <joint name="head_swivel">
        <hardwareInterface>PositionJointInterface</hardwareInterface>
      </joint>
    </transmission>

Oluşturduğumuz bu paketleri çalıştırarak inceleyelim.

    roslaunch models joints.launch
    
    Yeni bir terminalde
    rostopic list
    rostopic echo /joint_states
    
    Çıktı;
    header:
      seq: 220
      stamp:
        secs: 4
        nsecs: 707000000
      frame_id: ''
    name: ['head_swivel']
    position: [-2.9051283156888985e-08]
    velocity: [7.575990694887896e-06]
    effort: [0.0]
    
Şimdide tanımladığımız eklemi çalıştırmak için bir denetleyici yapılandırmalıyız. Kafa eklemini kontrol etmek için position_controllers paketinden bir JointPositionController kullanalım.

    roscd models/config
    gedit head.yaml
    
    type: "position_controllers/JointPositionController"
    joint: head_swivel
    
oluşturduğumuz yeni yaml dosyasını çalıştırabilmek için yeni bir launch dosyası oluşturmalıyız.

    roscd models/launch
    gedit head.launch
    
    <?xml version="1.0"?>
    <launch>
      <arg name="model" default="$(find models)/urdf/sekil8.urdf.xacro"/>
      <arg name="rvizconfig" default="$(find models)/rviz/urdf.rviz" />

      <include file="$(find models)/launch/gazebo.launch">
        <arg name="model" value="$(arg model)" />
      </include>

      <node name="rviz" pkg="rviz" type="rviz" args="-d $(arg rvizconfig)" />

      <rosparam command="load"
                file="$(find models)/config/joints.yaml"
                ns="r2d2_joint_state_controller" />
      <rosparam command="load"
                file="$(find models)/config/head.yaml"
                ns="r2d2_head_controller" />

      <node name="r2d2_controller_spawner" pkg="controller_manager" type="spawner"
        args="r2d2_joint_state_controller
              r2d2_head_controller
              --shutdown-timeout 3"/>
    </launch>

oluşturduğumuz bu launch dosyasını kullanarak artık robotumuzun kafasını hareket ettirebiliriz.

    roslaunch models head.launch

    yeni bir terminalde
    rostopic pub /r2d2_head_controller/command std_msgs/Float64 "data: -0.707"

Kafanın hareketini sağlamış olduk. Fakat kafa eklemini oluştururken herkangi bir fiziksel limit koymadığımzdan dolayı hareket komutunun gönderilmesiyle hemen belirtilen konuma hareket etti. Kademeli hareket için kafa eklemini limitlendirelim.

son oluşturduğumuz urdf dosyasındaki head_swivel'i aşağıdaki gibi düzenleyelim.

    <joint name="head_swivel" type="continuous">
      <parent link="base_link"/>
      <child link="head"/>
      <axis xyz="0 0 1"/>
      <origin xyz="0 0 ${bodylen/2}"/>
      <limit effort="30" velocity="1.0"/>
    </joint>

Yukarıda kullanımını gösterdiğimiz kodlar ile robotun kafasının kademeli olarak hareket ettiğini görebilirsiniz.

Şimdi ise gripper hareketlerini için urdf dosyamızı [burada](https://github.com/ros/urdf_sim_tutorial/blob/master/urdf/12-gripper.urdf.xacro) olduğu gibi düzenleyelim.

Her eklenti için ayrı bir ros konusu oluşturmak yerine onları bir araya getirebiliriz.

    roscd models/config
    gedit gripper.yaml
    
    type: "position_controllers/JointGroupPositionController"
    joints:
     - gripper_extension
     - left_gripper_joint
     - right_gripper_joint

oluşturduğumuz yaml dosyasını çalıştırmak için yeni bir launch dosyası oluşturalım.

    roscd models/launch
    gedit gripper.launch
    
    <?xml version="1.0"?>
    <launch>
      <arg name="model" default="$(find models)/urdf/sekil8.urdf.xacro"/>
      <arg name="rvizconfig" default="$(find models)/rviz/urdf.rviz" />

      <include file="$(find models)/launch/gazebo.launch">
        <arg name="model" value="$(arg model)" />
      </include>

      <node name="rviz" pkg="rviz" type="rviz" args="-d $(arg rvizconfig)" />

      <rosparam command="load"
                file="$(find models)/config/joints.yaml"
                ns="r2d2_joint_state_controller" />
      <rosparam command="load"
                file="$(find models)/config/head.yaml"
                ns="r2d2_head_controller" />
      <rosparam command="load"
                file="$(find models)/config/gripper.yaml"
                ns="r2d2_gripper_controller" />

      <node name="r2d2_controller_spawner" pkg="controller_manager" type="spawner"
        args="r2d2_joint_state_controller
              r2d2_head_controller
              r2d2_gripper_controller
              --shutdown-timeout 3"/>
    </launch>

oluşturduğumuz launch dosyasını çalıştırarak gripper'ın hareketlerini gözlemleyelim.

    roslaunch models gripper.launch
    
Gripperı açmak ve kolu dışarı itmek için

    rostopic pub  /r2d2_gripper_controller/command std_msgs/Float64MultiArray "layout:
      dim:
      - label: ''
        size: 3
        stride: 1
      data_offset: 0
    data: [0, 0.5, 0.5]"

Gripperı kapatmak ve kolu içeri çekmek için
    
    rostopic pub  /r2d2_gripper_controller/command std_msgs/Float64MultiArray "layout:
      dim:
      - label: ''
        size: 3
        stride: 1
      data_offset: 0
    data: [-0.4, 0, 0]"

Son olarak robotun tekerlerine harket eklentilerini yaparak modelimizi tamamlayalım.

urdf dosyamıza tekerlerin hareketi için actuator ekleyelim.

    <transmission name="${prefix}_${suffix}_wheel_trans">
      <type>transmission_interface/SimpleTransmission</type>
      <actuator name="${prefix}_${suffix}_wheel_motor">
        <mechanicalReduction>1</mechanicalReduction>
      </actuator>
      <joint name="${prefix}_${suffix}_wheel_joint">
        <hardwareInterface>VelocityJointInterface</hardwareInterface>
      </joint>
    </transmission>

Yer ile tekerler arasındaki sürtünmeyi tanımlayalım.

    <gazebo reference="${prefix}_${suffix}_wheel">
      <mu1 value="200.0"/>
      <mu2 value="100.0"/>
      <kp value="10000000.0" />
      <kd value="1.0" />
      <material>Gazebo/Grey</material>
    </gazebo>

urdf dosyamızın son hali [burdaki](https://github.com/ros/urdf_sim_tutorial/blob/master/urdf/13-diffdrive.urdf.xacro) gibi olmalıdır.

Tekerlerimizin hareketi için DiffDriveController kullanarak yaml dosyamızı oluşturalım.

    roscd models/config
    gedit diffdrive.yaml
    
    type: "diff_drive_controller/DiffDriveController"
    publish_rate: 50

    left_wheel: ['left_front_wheel_joint', 'left_back_wheel_joint']
    right_wheel: ['right_front_wheel_joint', 'right_back_wheel_joint']

    wheel_separation: 0.44

    # Odometry covariances for the encoder output of the robot. These values should
    # be tuned to your robot's sample odometry data, but these values are a good place
    # to start
    pose_covariance_diagonal: [0.001, 0.001, 0.001, 0.001, 0.001, 0.03]
    twist_covariance_diagonal: [0.001, 0.001, 0.001, 0.001, 0.001, 0.03]

    # Top level frame (link) of the robot description
    base_frame_id: base_link

    # Velocity and acceleration limits for the robot
    linear:
      x:
        has_velocity_limits    : true
        max_velocity           : 0.2   # m/s
        has_acceleration_limits: true
        max_acceleration       : 0.6   # m/s^2
    angular:
      z:
        has_velocity_limits    : true
        max_velocity           : 2.0   # rad/s
        has_acceleration_limits: true
        max_acceleration       : 6.0   # rad/s^2

oluşturduğumuz dosyaları çalıştırmak için yeni bir launch dosyası oluşturalım.

    roscd models/launch
    gedit diffdrive.launch
    
    <?xml version="1.0"?>
    <launch>
      <arg name="model" default="$(find models)/urdf/sekil8.urdf.xacro"/>
      <arg name="rvizconfig" default="$(find models)/rviz/urdf.rviz" />

      <include file="$(find models)/launch/gazebo.launch">
        <arg name="model" value="$(arg model)" />
      </include>

      <node name="rviz" pkg="rviz" type="rviz" args="-d $(arg rvizconfig)" />

      <rosparam command="load"
                file="$(find models)/config/joints.yaml"
                ns="r2d2_joint_state_controller" />
      <rosparam command="load"
                file="$(find models)/config/head.yaml"
                ns="r2d2_head_controller" />
      <rosparam command="load"
                file="$(find models)/config/gripper.yaml"
                ns="r2d2_gripper_controller" />
      <rosparam command="load"
                file="$(find models)/config/diffdrive.yaml"
                ns="r2d2_diff_drive_controller" />

      <node name="r2d2_controller_spawner" pkg="controller_manager" type="spawner"
        args="r2d2_joint_state_controller
              r2d2_head_controller
              r2d2_gripper_controller
              r2d2_diff_drive_controller
              --shutdown-timeout 3"/>

      <node name="rqt_robot_steering" pkg="rqt_robot_steering" type="rqt_robot_steering">
        <param name="default_topic" value="/r2d2_diff_drive_controller/cmd_vel"/>
      </node>
    </launch>

robotumuzu oluşturduğumuz launch dosyasını çalıştıralım.

    roslaunch models diffdrive.launch

![gazebo2](https://github.com/raclab/RACLAB/blob/master/images/ROS/pr2gazebo2.png)

# PR2 Modelinin İncelenmesi

yukarıda anlatılanların tamamı pr2 modelini oluşturmaya yönelikti, pr2 modelinde urdf kullanımın kalkması ve gazebo bağımlılıklarının değişmesiyle değişiklik yapıldı. Son modelin tamamını [buradan](http://wiki.ros.org/urdf/Tutorials/UnderstandingPR2URDF) inceleyebilir ve pr2 paketinin tamamına [burdan](https://github.com/PR2/pr2_common/tree/kinetic-devel/pr2_description) ulaşabilirsiniz.

# URDF dosyasının doğruluğunu kontrol etme

    roscd models/urdf
    check_urdf sekil7.urdf

urdf dosyamızın bağlantı grafiğini çıkaralım.

    urdf_to_graphiz sekil7.urdf
    evince physics.pdf 
    
![robot_tree](https://github.com/raclab/RACLAB/blob/master/images/ROS/pr2physics.png)
