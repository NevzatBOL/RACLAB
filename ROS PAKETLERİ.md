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

Referans Linkler;

https://www.stereolabs.com/documentation/integrations/ros/getting-started.html

http://wiki.ros.org/zed-ros-wrapper

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

    
    

