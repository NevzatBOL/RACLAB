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

 ![sekil](https://raw.githubusercontent.com/ros/urdf_tutorial/master/urdf_tutorial/images/myfirst.png)   
 
 
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

![sekil2](https://raw.githubusercontent.com/ros/urdf_tutorial/master/urdf_tutorial/images/multipleshapes.png)

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
    
![sekil3](https://raw.githubusercontent.com/ros/urdf_tutorial/master/urdf_tutorial/images/origins.png)

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
    
![sekil4](https://raw.githubusercontent.com/ros/urdf_tutorial/master/urdf_tutorial/images/materials.png)   


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
![sekil5](https://raw.githubusercontent.com/ros/urdf_tutorial/master/urdf_tutorial/images/visual.png)    

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

![sekil6](https://raw.githubusercontent.com/ros/urdf_tutorial/master/urdf_tutorial/images/flexible.png)

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

**Enson oluşturduğumuz modele çarpışma ve fiziksel özellikleri [burada](https://raw.githubusercontent.com/ros/urdf_tutorial/master/urdf_tutorial/urdf/07-physics.urdf) olduğu gibi ekleyebiliriz.**


check_urdf my_robot.urdf

urdf_to_graphiz my_robot.urdf
