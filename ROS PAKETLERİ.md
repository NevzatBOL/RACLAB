# ROS PAKETLERİ KULLANIMLARI VE KURULUMLARI

## mybot_ws

mybot_ws paketi githubdan klonlanarak çalışma dizini oluşturulur.

    cd ~
    git clone https://github.com/richardw05/mybot_ws.git
    gedit ~/.bashrc 
        source /home/nevzat/mybot_ws/devel/setup.bash
    cd mybot_ws/
    catkin_make
    source devel/setup.bash 

Robotun Gazebo ve Rviz üzerinde çalıştırılması

    roslaunch mybot_gazebo mybot_world.launch       -robotun gazebo paketi çalıştırılır.
    roslaunch mybot_description mybot_rviz.launch   -robotun rviz paketi çalıştırılır.
        Fixed Frame = odom  
        Add -> RobotModel                           -rviz'e robotun modeli eklenir.
    rostopic pub /cmd_vel geometry_msgs/Twist '[0.2, 0.0, 0.0]' '[0.0, 0.0, 0.1]'   -robotu hareket ettirmek için komut girilir.

     rosrun tf view_frames                          -sistemin ağacını pdf olarak kaydedir. 
     evince frames.pdf 

Robot üzerindeki kameradan simulasyon ortamında görüntü alınması
 
    roslaunch mybot_gazebo mybot_world.launch
    roslaunch mybot_description mybot_rviz.launch 
        Fixed Frame = odom  
        Add -> RobotModel
        Add -> Camera                               -rviz'e kamera'yı ekledik.
        Camera
            Image Topic /mybot/camera1/image_raw    -rviz üzerinden kameradan alınan görüntüye bakılabilir.
            
    rosrun image_view image_view image:=/mybot/camera1/image_raw    -kameradan alınan görüntüye image_view ile bakabiliriz.

Haritalandırma ve Konumlandırma (SLAM)
   
    roscd mybot_navigation  
    mkdir maps      -haritanın kaydedileceği klasörü oluşturduk.
    
    roslaunch mybot_gazebo mybot_world.launch
    roslaunch mybot_navigation gmapping_demo.launch         -haritalandırma için gerekli paketleri çalıştırdık.
    roslaunch mybot_description mybot_rviz_gmapping.launch
    roslaunch mybot_navigation mybot_teleop.launch          -robotun klavyeden kontolü için gerekli paketi çalıştırdık.
    rosrun map_server map_saver -f ~/mybot_ws/src/mybot_navigation/maps/test_map    -harita oluşturduktan sonra haritayı kaydettik.

    roslaunch mybot_gazebo mybot_world.launch   
    roslaunch mybot_navigation amcl_demo.launch             -oluşturduğumuz haritayı yükledik.
    roslaunch mybot_description mybot_rviz_amcl.launch      -rviz üzerinden artık robotumuzu otomatik yönlendire biliriz.
                                                            -2D Nav Goal kullanılarak robotu istenilen noktaya otomatik götürtebiliriz. (hedef nokta ve yönü belirler.)
                                                            
*Eğer lidar ile haritalama yapmıyorsa mybot.gazebo paketi içerisindeki  libgazebo_ros_gpu_laser.so yerine libgazebo_ros_laser.so bu yazılarak sorun çözülebilir.*

*Haritalama için Turtlebot paketleri kurulu olması gerekir kurulu değilse öncelikle Turtlebot paketini kurmalısınız.

Referans Link:

http://moorerobots.com/blog

## Turtlebot

Turtlebot Kurma
    
    sudo apt-get install ros-kinetic-turtlebot*

Turtlebot ile haritalama
    
    roslaunch turtlebot_gazebo turtlebot_world.launch 
    roslaunch turtlebot_gazebo gmapping_demo.launch  
    roslaunch turtlebot_rviz_launchers view_navigation.launch
    roslaunch turtlebot_teleop keyboard_teleop.launch
    rosrun map_server map_saver -f test_map
    
    roslaunch turtlebot_gazebo turtlebot_world.launch 
    roslaunch turtlebot_gazebo amcl_demo.launch map_file:=~/test_map.yaml
    roslaunch turtlebot_rviz_launchers view_navigation.launch

Referans Link:

http://learn.turtlebot.com/2015/02/03/8/


## rplidar

    mkdir -p rplidar/src
    cd rplidar
    catkin_make
    source devel/setup.bash
    gedit ~/.bashrc
      source /home/nevzat/rplidar/devel/setup.bash

    cd ~/rplidar/src/
    git clone -b slam https://github.com/robopeak/rplidar_ros.git   -paketin slam kolunu indirdik.
    

    sudo chmod 666 /dev/ttyUSB0                 -rplidarı çalıştırabilmek için usb portu yapılandırdık.

    roslaunch rplidar_ros rplidar.launch        -rplidar çalıştırmak için kullanılabilir.
    roslaunch rplidar_ros view_rplidar.launch   -rvizde rplidar'ı çalıştırmak için kullanılabilir.
    rosrun rplidar_ros rplidarNodeClient        -rplidar'dan gelen verileri yazdırır.

Rplidar ile Haritalandırma

    roslaunch rplidar_ros view_slam.launch      -rplidar ve hector mapping ile haritalandırma yapılabilir.

    rosrun map_server map_saver -f test_map     -oluşturduğumuz haritayı kaydederiz.

Referans Link:

https://github.com/robopeak/rplidar_ros

https://hollyqood.wordpress.com/2015/12/01/ros-slam-2-hector-slam-2d%E5%9C%B0%E5%9C%96%E5%BB%BA%E7%BD%AE/

## ZED KAMERA

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

Birden fazla zed kullanma

    roslaunch zed_wrapper zed_multi_cam.launch

Birden fazla zed ve gpu kullanma

    roslaunch zed_wrapper zed_multi_gpu.launch
    
Rviz'de /depth/depth_registered derinlik değeri metre cinsinden 32bit'dir, bu değer `launch/zed_camera.launch` dosyasın da 
openni_depth_mode value=1 yapılarak milimetre cinsinden 16bit yapılabilir.

    <param name="openni_depth_mode" value="1"/>
  
Derinlik ve noktasal bulut değeri varsayılan olarak 100 tanımlanmıştır. Bu değerde tüm derinlik değerleri, derinlik ve noktasal bulut'a yazılır. Belirli bir değerin altındaki değerleri filtrelemek için aşağıdaki komut kullanıla bilir. (80 varsayılan filtre değeridir.)
  
    rosrun dynamic_reconfigure dynparam set /zed/zed_wrapper_node confidence 80    
   
Yayınlanan Konular;

    image_rect_color                : Renk düzeltilmiş görüntü
    image_raw_color                 : Renk düzeltilmemiş görüntü
    /depth/depth_registered         : Sol resimde kayıtlı derinlik harita görüntüsü
    /point_cloud/cloud_registered   : Kayıtlı renk noktası bulutu
    /camera/odom                    : zed_initial_frame'e göre mutlak 3D konum ve yön bilgisi
    /camera_info                    : Kamera kalibrasyon verileri

Launch Dosyası Parametreleri;

    Parameter	        Description	                                        Value
    svo_file	        Specify SVO filename	                                Path to an SVO file
    resolution	        Select ZED camera resolution	                        ‘0’: HD2K, ‘1’: HD1080, ‘2’: HD720, ‘3’: VGA
    frame_rate	        Set ZED camera video framerate	                        int
    sensing_mode	        Select depth sensing mode	                        ‘0’: STANDARD, ‘1’: FILL
    quality	                Select depth map quality	                        ‘0’: NONE, ‘1’: PERFORMANCE, ‘2’: MEDIUM, ‘3’: QUALITY
    openni_depth_mode	Convert 32bit depth in meters to 16bit in millimeters	‘0’: 32bit float meters, ‘1’: 16bit uchar millimeters
    zed_id	                Select a ZED camera by its ID. ID are assigned by Ubuntu. 
                            Useful when multiple cameras are connected. 
                            ID is ignored if an SVO path is specified.	        int, default ‘0’
    gpu_id	                Select a GPU device for depth computation	        int, default ‘-1’ (best device found)
    publish_tf	        Enable/Disable publish odometry TF	                true, false
    odometry_frame	        Odometry frame name	string,                         default=‘odometry_frame’
    base_frame	        Base link frame name	                                string, default=‘base_frame’
    camera_frame	        Camera frame name	                                string, default=‘camera_frame’
    depth_frame	        Depth frame name	                                string, default=‘depth_frame’






Referans Linkler;

https://www.stereolabs.com/documentation/integrations/ros/getting-started.html

http://wiki.ros.org/zed-ros-wrapper

## ZED KAMERA RTABMAP İLE HARİTALANDIRMA

Haritalandırma için rtabmap paketi indirilir.

     sudo apt-get install ros-kinetic-rtabmap-ros 

ZED Kamera Odemetrisi kullanarak haritalandırma

    export ROS_NAMESPACE=camera
    roslaunch zed_wrapper zed_camera.launch

    roslaunch rtabmap_ros rtabmap.launch rtabmap_args:="--delete_db_on_start" depth_topic:=/camera/depth/depth_registered frame_id:=zed_center approx_sync:=false visual_odometry:=false odom_topic:=/camera/odom
    
Rtabmap Odemetrisi kullanarak haritalandırma

    export ROS_NAMESPACE=camera
    roslaunch zed_wrapper zed_camera.launch publish_tf:=false

    roslaunch rtabmap_ros rtabmap.launch rtabmap_args:="--delete_db_on_start" depth_topic:=/camera/depth/depth_registered frame_id:=zed_center approx_sync:=false

*Egeer haritala maparken, haritanın arka planı kırmızıya dönerse odemetri kaybolur. Bu durumda Kamerayı kırmızı belirmeden önce ki  konumuna getirin ve odometriyi yeniden hesaplansın yada haritayı sıfırlayın.*

Haritayı sıfırlamak için

    rosservice call /rtabmap/reset

*Harita oluştulmaya başlandığında otomaktik olarak ~/.ros/ konumuna kaydedilir.*

*Haritayı üç boyutlu olarak kaydetmek için File -> Export 3D Clouds seçeneği kullanılabilir.*

*PLY formatına kaydedildiğinde bulut, MeshLab* 

*PCD formatında kaydedildiğinde nokta bulutlarını pcl_viewer ile açabilirsiniz.*

Haritayı incelemek için

    rtabmap-databaseViewer ~/.ros/rtabmap.db

Referans Linkler;

http://wiki.ros.org/rtabmap_ros/Tutorials/HandHeldMapping

https://github.com/introlab/rtabmap/wiki/Kinect-mapping
    

## SCANSE SWEEP LİDAR

git clone https://github.com/jetsonhacks/installSweep

Adresinden dosyalar indirilir

    cd installSweep/
    ./installSweepSDK.sh
Yukarıdaki adımlarda home dizinine sweep-sdk yi indirdik. Paketi kurmadan önce lidarin usb serial number'ı öğrenmemiz gerekli. Lidar usb ile bilgisayara bağladıktan sonra terminalden "dmesg --follow"  komutu çalıştırılır ve serial number 
"~/installSweep" dizinindeki "99-usb-serial-rules" isimli dosyanın içindeki ATTRS(serial)=="xxxxxxxx" isimli satırdaki xxxxxxx kısmına kopyalanır ve kaydedilir.

    cd installSweep/
    sudo cp 99-usb-serial.rules /etc/udev/rules.d/
SWEEP-SDK ÜZERİNDEN VERİ ALMA

    cd ~/sweep-sdk/libsweep/build
    sudo ./sweep-ctl /dev/sweep get motor_speed
Lidarın çalışma frekansını verir

    sudo ./sweep-ctl /dev/sweep get sample_rate
Lidarın dakikadaki örnek sayısını verir

    sudo ./sweep-ctl /dev/sweep set motor_speed 5
Lidarın çalışma frekansını değiştirir 1-10 arasındaki frekanslara ayarlanabilir

    sudo ./sweep-ctl /dev/sweep set sample_rate 1000
Lidarın dakikadaki örnek sayısını değiştirir, maximum 1000

    cd ~/sweep-sdk/libsweep/examples/build
    sudo ./example-c /dev/sweep
Lidarın 10 tur dönmesi sonuçunda aldığı verileri terminal ekranına yazdırır.

    sudo ./example-viewer /dev/sweep
Lidar verilerini viewer ekranında gösterir.

SWEEP LİDAR PAKETİ WORKSPACE ÜZERİNE KURULUMU

İlk önce lidar için bir workspace oluşturalım 

    mkdir -p lidar/src
    cd ~/lidar/src
    catkin_init_workspace
    cd installSweep/
    ./installSweepROS.sh ~/lidar
önceden açılmış bir workspace'e kurmak için ./installSweepROS.sh [catkin workspace name] kullanılabilir.

    cd ~/lidar/src/sweep-ros/launch
    gedit sweep2scan.launch
Açılan sayfada type string value degerini /dev/sweep yap ve kaydet

    roslaunch sweep_ros view_sweep_laser_scan.launch
    
Lidar verilerini Rviz üzerinde gösterir

    roslaunch sweep_ros sweep2scan.launch
Lidar verilerini /scan topic'i üzerinden yayınlar

    sudo chown username /dev/ttyUSB0
Lidar çalıştırılırken terminalde "error opening serial port" hatası verirse yönetici olarak açabilir veya yukarıdaki komut ile lidar usb kablosu takılı olduğu sürece doğru açılmasını sağlayabilirsiniz her kablo söküp takmada tekrar bu komutu çalışmalısınız.

Referans Linkler;

http://www.jetsonhacks.com/2017/06/06/scanse-sweep-lidar-software-install/

https://github.com/scanse/sweep-ros
    

