# ROS BAŞLANGIÇ

## ROS Çalışma Ortamı (Workspace) Oluşturma  

    mkdir -p ~/catkin_ws/src        -catkin_ws ve src alt klasörünü oluşturduk.
    cd ~/catkin_ws/	                -oluşturduğumuz dizine gittik.
    catkin_make                     -çalışma ortamını yapılandırdık.
    
    source devel/setup.bash         -çalışma dizinimizi kaynakladık.
*Eğer çalışma dizinini .bashrc dosyasıne eklemezsek her yeni terminalde oluşturduğumuz çalışma dosyasını çalıştırırken yeniden kaynak yapmamız gerekir.*

    gedit ~/.bashrc 			         
    source /home/nevzat/catkin_ws/devel/setup.bash   -çalışma ortamını bashrc dosyasının sonuna ekleyin.
    
## ROS Dosya Sisteminde Gezinme

    rospack find paket_ismi         -paket arar.
    rospack find rospy
        /opt/ros/kinetic/share/rospy

    
    roscd paket_ismi/alt_dizin      -roscd ile paketin anadizinine veya alt dizinlerine gidilebilir.
    roscd rospy
    roscd rospy/cmake 
    roscd log                       -ros'un günlük dosyalarının depolandığı adrese götürür.
    
    rosls paket_ismi/alt_dizin	    -rosls ile paketin anadizinindeki veya alt dizinindeki dosyaları listeler.
    rosls rospy
        cmake  package.xml  rosbuild

## ROS Paket Oluşturma

    catkin_create_pkg paket_ismi bağımlık1 bağımlık2	-çalıştığımız dizine paket_ismi de bağımlı olarak tanımladığız paketleri oluşturur.
    
    cd ~/catkin_ws/src              -çalışma dizinimiz içerinsdeki src klasörünü gittik.
    catkin_create_pkg beginner_tutorials std_msgs rospy roscpp    -paketimizi oluşturduk.
    
    -Ros paketlerinde bulunan CMakeList.txt ve package.xml dosyalarını oluşturur.
    -Oluşturulan yeni paketin bağımlılıkları package.xml dosyasında tutulur.
    
    cd ..                         -çalışma dizinimize geri döndük.
    catkin_make                   -çalışma dizinimizi yapılandırdık.
    
    rospack depends1 paket_ismi			-girilen paketin 1. derece paket bağımlılıkları listeler.
    rospack depends1 beginner_tutorials 
        roscpp
        rospy
        std_msgs
        
    rospack depends paket_ismi			-girilen paketin tüm alt bağımlılıkları listeler.
    rospack depends beginner_tutorials
        cpp_common
        rostime
        roscpp_traits
        roscpp_serialization
        catkin
        genmsg
        ...
     
## Paket özelleştirme
    
    cd ~catkin_ws/src/beginner_tutorials
    sudo gedit package.xml

    <description> beginner_tutorials paketi </ description>		-açıklama kısmı. ilk çümle kısa olmalıdır. birden fazla açıklama kullanılabilir.
    <maintainer email="nevzatbol06@gmail.com">nevzat</maintainer>	-bakımcı etiketi. başkalarının pakette kiminle iletişime geçeceğini bilmesini sağlar.
    <license>BDS</license>						-Lisans etiketi.
    
    <buildtool_depend>catkin</buildtool_depend>		
    
    <build_depend>bağımlı_paket_ismi</build_depend>
    <run_depend>bağımlı_paket_ismi</run_depend>
    
    <build_depend>rospy</build_depend>
    <run_depend>rospy</run_depend>
    
## ROS Düğüm(Node) Kullanımı

    roscore						-ros çekirdeğini aktif hale getirir.
    
    rosrun paket_adı düğüm_adı			                -doğrudan bir düğüm çalıştırabiliriz.
    rosrun turtlesim turtlesim_node
    
    rosrun paket_adı düğüm_adı __name:=New_name	    -düğümü yeniden adlandırarak çalıştırır.
    rosrun turtlesim turtlesim_node __name:=my_turtle
    
    rosnode list					        -çalışan ros düğümlerini listeler.
    rosnode info düğüm_adı				-belli bir düğüm hakkında bilgi verir.
   
    rosnode ping düğüm_adı				-düğümü test eder.
    rosnode ping my_turtle
## ROS Konu(Topic) Kullanımı

    rostopic				                  -rostopic için kullanılabilir alt komutları ver
        rostopic bw	                  -konu tarafından kullanılan görüntü bant genişliği
        rostopic delay	              -konunun yayınlanırken geçikme süresini verir.
        rostopic echo	                -yayınlanan konuyu dinler.
        rostopic find	                -konunun tipini bulur.
        rostopic hz	                  -konunun yayınlanma hızını verir.    
        rostopic info                 -konu hakkında bilgi verir.
        rostopic list	                -yayınlanan konuları listeler.
        rostopic pub                  -mesajları belirli bir konuda yayınlar
        rostopic type	                -konunun türünü verir.

## Örnek ROS Paketi Çalıştırma
    
    roscore						                      -ros çekirdeğini aktif hale getirdik.
    
    rosrun turtlesim turtlesim_node			    -turtlesim_node düğümünü çalıştırdık.
    rosrun turtlesim turtlesim_teleop_kep		-kaplumbanın hareket etmesi için gerekli olan düğümü çalıştırdık.

    rosrun rqt_graph rqt_graph			        -sistemde neler olup bittiğinin dinamik bir grafiğini oluşturur.
    rqt_graph					                      -aynı komutu bu şekilde de çalışıtabiliriz.
    
![rqt graph](http://wiki.ros.org/ROS/Tutorials/UnderstandingTopics?action=AttachFile&do=get&target=rqt_graph_turtle_key2.png)
    
    rostopic echo /turtle1/cmd_vel			    -cmd_vel konusunu dinlenir.
    
    rostopic list -v				                -çalışan düğümler hakkında bilgi verir.
    
    rostopic type /turtle1/cmd_vel			    -yayınlanmakta olan konunun ileti türünü döndürür.
    
    rosmsg show geometry_msgs/Twist			    -mesajın ayrıntısını gösterir.
    
    #bir kez mesajı yayınlarsak;
    rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, -1.8]'
    
    #mesajı belirli bir hızda sürekli yayınlarsak;
    rostopic pub /turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, -1.8]'
   
    Parametrelerin Açıklanması:
    
    rostopic pub					                 -iletileri belirli bir konuda yayınlar.
    -1						                         -rostopic'in yanlız bir mesaj yayınlayıp çıkmalarına sağlar.
    /turtle1/cmd_vel				               -yayınlanacak konumun adıdır.
    geomery_msgs/Twist				             -yayın yaparken kullanılacak ileti türüdür.
    --						                         -çift çizgiden sonra mesaj yayınlanır.
    -r 1						                       -1hz hızında sürekli mesaj yayınlar.
   
    rostopic hz /turtle1/pose			        -mesajın yayınlanma hızını verir.

    rosrun rqt_plot rqt_plot			        -takip etmek istediğimiz değerleri grafikte çizdirebiliriz.
      topic /turtle1/pose/x	
      
![rqt plot](http://wiki.ros.org/ROS/Tutorials/UnderstandingTopics?action=AttachFile&do=get&target=rqt_plot.png)
