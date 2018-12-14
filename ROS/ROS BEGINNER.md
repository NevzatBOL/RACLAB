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
    
    rosls paket_ismi/alt_dizin	-rosls ile paketin anadizinindeki veya alt dizinindeki dosyaları listeler.
    rosls rospy
        cmake  package.xml  rosbuild

## ROS Paket Oluşturma

    catkin_create_pkg paket_ismi bağımlık1 bağımlık2	-çalıştığımız dizine paket_ismi de bağımlı olarak tanımladığız paketleri oluşturur.
    
    cd ~/catkin_ws/src              			-çalışma dizinimiz içerinsdeki src klasörünü gittik.
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

    roscore								-ros çekirdeğini aktif hale getirir.
    
    rosrun paket_adı düğüm_adı			                -doğrudan bir düğüm çalıştırabiliriz.
    rosrun turtlesim turtlesim_node
    
    rosrun paket_adı düğüm_adı __name:=New_name	    		-düğümü yeniden adlandırarak çalıştırır.
    rosrun turtlesim turtlesim_node __name:=my_turtle
    
    rosnode list					        	-çalışan ros düğümlerini listeler.
    rosnode info düğüm_adı						-belli bir düğüm hakkında bilgi verir.
   
    rosnode ping düğüm_adı						-düğümü test eder.
    rosnode ping my_turtle
## ROS Konu(Topic) Kullanımı

    rostopic				-rostopic için kullanılabilir alt komutları ver
        rostopic bw	                	-konu tarafından kullanılan görüntü bant genişliği
        rostopic delay	              	-konunun yayınlanırken geçikme süresini verir.
        rostopic echo	                -yayınlanan konuyu dinler.
        rostopic find	                -konunun tipini bulur.
        rostopic hz	                	-konunun yayınlanma hızını verir.    
        rostopic info                 	-konu hakkında bilgi verir.
        rostopic list	                -yayınlanan konuları listeler.
        rostopic pub                  	-mesajları belirli bir konuda yayınlar
        rostopic type	                -konunun türünü verir.

## Örnek ROS Paketi Çalıştırma
    
    roscore						-ros çekirdeğini aktif hale getirdik.
    
    rosrun turtlesim turtlesim_node			-turtlesim_node düğümünü çalıştırdık.
    rosrun turtlesim turtle_teleop_key 		-kaplumbanın hareket etmesi için gerekli olan düğümü çalıştırdık.

    rosrun rqt_graph rqt_graph			-sistemde neler olup bittiğinin dinamik bir grafiğini oluşturur.
    rqt_graph					-aynı komutu bu şekilde de çalışıtabiliriz.
    
![rqt graph](https://github.com/raclab/RACLAB/blob/master/images/ROS/rosgraph.png)
    
    rostopic echo /turtle1/cmd_vel			    -cmd_vel konusunu dinlenir.
    
    rostopic list -v				    -çalışan düğümler hakkında bilgi verir.
    
    rostopic type /turtle1/cmd_vel			    -yayınlanmakta olan konunun ileti türünü döndürür.
    
    rosmsg show geometry_msgs/Twist			    -mesajın ayrıntısını gösterir.
    
    #bir kez mesajı yayınlarsak;
    rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, -1.8]'
    
    #mesajı belirli bir hızda sürekli yayınlarsak;
    rostopic pub /turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, -1.8]'
   
    Parametrelerin Açıklanması:
    
    rostopic pub					-iletileri belirli bir konuda yayınlar.
    -1						-rostopic'in yanlız bir mesaj yayınlayıp çıkmalarına sağlar.
    /turtle1/cmd_vel				-yayınlanacak konumun adıdır.
    geomery_msgs/Twist				-yayın yaparken kullanılacak ileti türüdür.
    --						-çift çizgiden sonra mesaj yayınlanır.
    -r 1						-1hz hızında sürekli mesaj yayınlar.
   
    rostopic hz /turtle1/pose			-mesajın yayınlanma hızını verir.

    rosrun rqt_plot rqt_plot		        -takip etmek istediğimiz değerleri grafikte çizdirebiliriz.
      topic /turtle1/pose/x	
      
![rqt plot](https://github.com/raclab/RACLAB/blob/master/images/ROS/matplot.png)
    

## ROS Hizmetleri ve Parametreleri

    rosservice					-hizmet komutlarını listeler.
    rosservice list					-sunulan hizmetleri listeler.

    rosservice type /hizmet				-kullanılanmak istenen hizmetin türünü listeler.
    rosservice type /clear
        std_srvs/Empty
        
    rosservice call /hizmet				-hizmeti çağırır.
    rosservice call /clear
        
    rosservice type /servis_ismi | rossrv show	-rossrv ros hizmet türleri hakkında bilgi görüntülemek için kullanılır.
    rosservice type /spawn | rossrv show
            float32 x
            float32 y
            float32 theta
            string name
            ---
            string name

    rosparam					-paremetre komutlarını listeler.
    rosparam list					-kullanılabilecek parametreleri listeler.

    rosparam set parametre_ismi parametre_değeri	-parametreyi uygular.
    rosparam set /background_r 150
    rosservice call /clear
    
    rosparam get parametre_ismi			-parametrenin değerlerini çeker.
    rosparam get /background_g
        86
    rosparam get /					-tüm parametre değerlerini listeler.
        background_b: 255
        background_g: 86
        background_r: 150
        roslaunch:
          uris: {'aqy:51932': 'http://aqy:51932/'}
        run_id: e07ea71e-98df-11de-8875-001b21201aa8

    rosparam dump file_name.yaml			-tüm parametreleri yaml uzantılı bir dosyaya kaydettik.
    rosparam dump params.yaml
    
    rosparam load file_name.yaml isim		-yaml uzantılı dosyadan tüm paremtreleri isim alanına yükledik.
    rosparam load params.yaml copy
    rosparam get /copy/background_r
    
## Rqt_console ve Roslaunch Kullanma
    rosrun rqt_console rqt_console			-düğümlerin çıktısını görüntülemek için kullanılır.
    rosrun rqt_logger_level rqt_logger_level	-günlükçüyü açar.
						        -günlükçü düzeyi ayarlanarak, ayarlanan öncelik sıralamasına göre;
						        -ölümcül, hata, uyarı, bilgi ve hata ayıklama iletilerini alırız.
    
 ![rpt_console](https://github.com/raclab/RACLAB/blob/master/images/ROS/console.png)
  ![rqt_rqt_logger_level](https://github.com/raclab/RACLAB/blob/master/images/ROS/loggerlevel.png)
     
      rosrun turtlesim turtlesim_node
     
  ![rqt_consol_warn](https://github.com/raclab/RACLAB/blob/master/images/ROS/console2.png)
  
      roslaunch paket_ismi file_name    -Birden fazla paketi tek seferde çalıştırmak için .launch pekiti oluşturulur.
                                        -Bu paketin çalıştırılması ile birden fazla Node çalıştırılmış olur.
      cd ~/catkin_ws/src/beginner_tutorials/	
      mkdir launch
      cd launch
      touch turtlemimic.launch
      gedit turtlemimic.lauch
         <launch>

          <group ns="turtlesim1">
            <node pkg="turtlesim" name="sim" type="turtlesim_node"/>
          </group>

          <group ns="turtlesim2">
            <node pkg="turtlesim" name="sim" type="turtlesim_node"/>
          </group>

          <node pkg="turtlesim" name="mimic" type="mimic">
            <remap from="input" to="turtlesim1/turtle1"/>
            <remap from="output" to="turtlesim2/turtle1"/>
          </node>

        </launch>
        
      roslaunch beginner_tutorials turtlemimic.launch
      rostopic pub /turtlesim1/turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, -1.8]'
      
## ROS Dosya Düzenlemek 		
    rosed paket_adı dosya_adı	-düzenlenmek istenen dosyanın konumuna gitmeye gerek kalmadan direk dosyaya erişmemizi sağlar.
    export EDITOR='nano -w'		-varsayılan dosya editörü vim dir. bu editörü nano ile değiştirdik.
                            	-sadece tanımlanan terminalde geçerlidir.

    echo $EDITOR			-tanımlı olan editörü gösterir.

## ROS Msg ve Srv Oluşturma
	
	    -msg: bir ros mesajının alanlarını tanımlayan basit metin dosyasıdır.
        -srv: bir hizmeti açıklar.
        -srv dosyası bir istek ve yanıt içeren mesaj dosyasıdır. iki kısım --- ile ayrılır.
    roscd beginner_tutorials
    mkdir msg						-msg dosyasını oluşturduk.
    echo "int64 num"> msg/Num.msg				-Num.msg dosyasına int64 num mesajını ekledik.

    rosed beginner_tutorials package.xml			-package.xml dosyası içerisinde aşağıdaki kodların bulunduğundan emin oluruz.
      <build_depend>message_generation</build_depend>	-message_gereration oluşturma zamanında ihtiyacımı var.
      <run_depend>message_runtime</run_depend>		-message_runtime çalıma zamanında ihtiyacımız var.


    rosed paket_adı CMakeList.txt
    find_package(catkin REQUIRED COMPONENTS
       roscpp
       rospy
       std_msgs
       message_generation				-message_generation bağımlılığını ekledik.
    )
    catkin_package(
      ...
      CATKIN_DEPENDS message_runtime		-ileti zaman bamlılığını dışa aktardık.
      ...
    )
    add_message_files(
      FILES
      Num.msg					-mesaj dosyamızı ekledik.
    )
    generate_messages(				-generate_message() fonksitonun çağrıldığından emin olmalıyız.
      DEPENDENCIES
      std_msgs
    )

    rosmsg show paket_ismi/ileti			-oluşturduğumuz msg dosyasının görünür olduğundan emin oluruz.
    rosmsg show beginner_tutorials/Num
        int64 num
        
    rosmsg show ileti				-iletinin hangi pakette tanımlı olduğunu bilmiyorsak bu komutu kullanırız.
    rosmsg show Num
        [beginner_tutorials/Num]:
        int64 num
        
    roscd beginner_tutorials
    mkdir srv							-srv klasörünü oluşturduk.
    roscp paket_ismi kopyalancak_dosya kopyalancak_yer&dosya_adı	-srv dosyasını başka bir paketten kopyalayarak oluşturduk.
    roscp rospy_tutorials AddTwoInts.srv srv/AddTwoInts.srv

    add_service_files(				
      FILES
      AddTwoInts.srv				-.srv hizmet dosyamızı ekledik.
    )

    rossrv show paket_ismi/hizmet_adı		-hizmet_adı(.srv) dosyasının okur.
    rossrv show beginner_tutorials/AddTwoInts
        int64 a
        int64 b
        ---
        int64 sum
        
    rossrv show hizmet_adı		-hizmet_adı dosyasının bulunduğu tüm paketleri ve dosya içeriklerini yazdırır.
    rossrv show AddTwoInts
        [beginner_tutorials/AddTwoInts]:
        int64 a
        int64 b
        ---
        int64 sum

        [rospy_tutorials/AddTwoInts]:
        int64 a
        int64 b
        ---
        int64 sum
    
    roscd paket_ismi
    cd ../..
    catkin_make install
    
 ## ROS Basit Yayıncı ve Abone Yazma C++
    
    roscd beginner_tutorials
    mkdir -p src
    cd src
    touch talker.cpp
    touch listener.cpp
    
    gedit talker.cpp    -talker.cpp dosyasını düzenlemek için açılır.
    gedit listener.cpp  -listener.cpp dosyası düzenlemek için açılır.

### talker.cpp
    #include "ros/ros.h"
    #include "std_msgs/String.h"
    #include <sstream>

    int main(int argc,char **argv)
    {
            ros::init(argc,argv,"talker");  //Node'u (düğümü) başlatır.
            ros::NodeHandle n;              //düğümü başlatır ve son düğüm yıkıldığında düğümün kullandığı tüm kaynakları temizler.
            ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter",1000);     //mesaj yayınlama düğümlerini(Node) ayarladık.
            ros::Rate loop_rate(10);        //çalışma hızımızı ayarlar. (10hz)

            int count=0;
            while(ros::ok())
            {
                    std_msgs::String msg;   //yayınlanacak mesajın türünü belirtik.

                    std::stringstream ss;
                    ss<<"hello world"<<count;	//mesajı oluşturduk.
                    msg.data=ss.str();

                    ROS_INFO("%s",msg.data.c_str());

                    chatter_pub.publish(msg);       //mesajı yayınladık.

                    ros::spinOnce();                //geri çağrıları almak için kullanılır.

                    loop_rate.sleep();              //çalışma hızımızı 10hz e ayarlamak için artan sürede uyku moduna geçiyoruz.
                    ++count;
            }
            return 0;
    }

### listener.cpp

    #include "ros/ros.h"
    #include "std_msgs/String.h"

    void chatterCallback(const std_msgs::String::ConstPtr&msg)
    {
            ROS_INFO("I heard: [%s]",msg->data.c_str());
    }

    int main(int argc,char **argv)
    {
            ros::init(argc,argv,"listener");
            ros::NodeHandle n;
            ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);
            //subscribe ile bir topic(konuyu) dinleriz.
            //subscribe'ın ikinci paremetresi mesajın boyutudur.
            //Mesajlar işlenenden daha hızlı geliyorsa, bu atılmaya başlaşlamadan önce belleğe atılacak ileti sayısıdır.
            //üçüncü paremetresi çağrılacak fonksiyonun adıdır.
            
            ros::spin();	//bir döngüye girer ve mümkün olduğunca hızlı ileti çağırır.
            return 0;
    }

*C++ dosyası oluşturulduktan sonra çalıştırıla bilmesi için oluşturulan dosyaların CMakeLists.txt dosyasına eklenmesi gerekir.*

    roscd beginner_tutorials 
    gedit CMakeLists.txt	
    
    include_directories(include ${catkin_INCLUDE_DIRS})

    add_executable(talker src/talker.cpp)
    target_link_libraries(talker ${catkin_LIBRARIES})
    add_dependencies(talker beginner_tutorials_generate_messages_cpp)

    add_executable(listener src/listener.cpp)
    target_link_libraries(listener ${catkin_LIBRARIES})
    add_dependencies(listener beginner_tutorials_generate_messages_cpp)

    cd ~/catkin_ws
    catkin_make     -her c++ dosyası düzenlenme işleminden sonra catkin_make yapılmalıdır.
    
    roscore		-oluşturulan talker ve listener kodları çalıştırılır.
    rosrun beginner_tutorials talker.cpp
    rosrun beginner_tutorials listener.cpp
    
## ROS Basit Yayıncı ve Abone Yazma Python    

    roscd beginner_tutorials
    mkdir scripts
    cd scripts
    touch talker.py
    touch listener.py
    
    gedit talker.py
    gedit listener.py
    
### talker.py
    #!/usr/bin/env python
    import rospy
    from std_msgs.msg import String

    def talker():
        pub = rospy.Publisher('chatter', String, queue_size=10)  #yayıncı oluşturulur. Topic name: chatter  
        rospy.init_node('talker', anonymous=True)   #yayıncının Node name:talker
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():  #paket kaparılana kadar devam et. (ctrl+c ile kapatılır.)
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            pub.publish(hello_str)  #mesaj yayınlanır.
            rate.sleep()

    if __name__ == '__main__':
        try:
            talker()
        except rospy.ROSInterruptException:
        pass
        
    
    chmod +x talker.py  -oluşturduğumuz python dosyasını çalıştırılabilir yaptık.
    
### listener.py
    #!/usr/bin/env python
    import rospy
    from std_msgs.msg import String

    def callback(data):
        rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data) #dinlenen mesaj yazdırılır.

    def listener():
        rospy.init_node('listener', anonymous=True) #dinleyici düğümü(Node).
        rospy.Subscriber('chatter', String, callback)   #dinlenecek konu
        rospy.spin()

    if __name__ == '__main__':
        listener()

    chmod +x listener.py    -oluşturduğumuz python dosyasını çalıştırılabilir yaptık.
    
    roscore                                 
    rosrun beginner_tutorials talker.py
    rosrun beginner_tutorials listener.py


## ROS Basit Hizmet ve İstemci Yazma C++    
	roscd beginner_tutorials/src
	touch add_two_ints_server.cpp
	touch add_two_ints_client.cpp
	
	gedit add_two_ints_server.cpp
	gedit add_two_ints_client.cpp

###  add_two_ints_server.cpp
	#include "ros/ros.h"
	#include "beginner_tutorials/AddTwoInts.h"

	bool add(beginner_tutorials::AddTwoInts::Request  &req,
		 beginner_tutorials::AddTwoInts::Response &res)
	{
		//daha önce oluşturduğumuz AddTwoInts.h  çağırdık.
		//Bu işlev, hizmetin iki int eklemesini sağlar, srv dosyasında tanımlanan istek ve yanıt türünü alınır ve bir boolean döndürür.
		res.sum = req.a + req.b;
		ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
		ROS_INFO("sending back response: [%ld]", (long int)res.sum);
		return true;
	 }

	int main(int argc, char **argv)
	{
		ros::init(argc, argv, "add_two_ints_server");
		ros::NodeHandle n;

		ros::ServiceServer service = n.advertiseService("add_two_ints", add);
		ROS_INFO("Ready to add two ints.");
		ros::spin();
		return 0;
	}

###  add_two_ints_client.cpp
	#include "ros/ros.h"
	#include "beginner_tutorials/AddTwoInts.h"
	#include <cstdlib>

	int main(int argc,char **argv)
	{
		ros::init(argc,argv,"add_two_ints_client");
		if(argc != 3)
		{
			ROS_INFO("usage: add_two_ints_client X Y");
			return 1;
		}

		ros::NodeHandle n;
		ros::ServiceClient client = n.serviceClient<beginner_tutorials::AddTwoInts>("add_two_ints");
		beginner_tutorials::AddTwoInts srv;
		srv.request.a=atoll(argv[1]);
		srv.request.b=atoll(argv[2]);
		if(client.call(srv))
		{
			ROS_INFO("Sum: %ld", (long int)srv.response.sum);
		}
		else
		{
			ROS_ERROR("Failed to call service add_two_ints");
			return 1;
		}

		return 0;
	}
	
	
	roscd beginner_tutorials 
    	gedit CMakeLists.txt
	
	add_executable(add_two_ints_server src/add_two_ints_server.cpp)
	target_link_libraries(add_two_ints_server ${catkin_LIBRARIES})
	add_dependencies(add_two_ints_server beginner_tutorials_gencpp)

	add_executable(add_two_ints_client src/add_two_ints_client.cpp)
	target_link_libraries(add_two_ints_client ${catkin_LIBRARIES})
	add_dependencies(add_two_ints_client beginner_tutorials_gencpp)

	
	cd ~/catkin_ws
    	catkin_make     -her c++ dosyası düzenlenme işleminden sonra catkin_make yapılmalıdır.
    

	roscore
	rosrun beginner_tutorials add_two_ints_server
	rosrun beginner_tutorials add_two_ints_client 1 3		say1+say2 toplanır.
	
## ROS Basit Hizmet ve İstemci Yazma Python
	roscd beginner_tutorials/scripts
	touch add_two_ints_server.py
	touch add_two_ints_client.py
	
	gedit add_two_ints_server.py
	gedit add_two_ints_client.py
	
### add_two_ints_server.py
	#!/usr/bin/env python

	from beginner_tutorials.srv import *
	import rospy

	def handle_add_two_ints(req):
		print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
		return AddTwoIntsResponse(req.a + req.b)

	def add_two_ints_server():
		rospy.init_node('add_two_ints_server')
		s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
		print "Ready to add two ints."
		rospy.spin()

	if __name__ == "__main__":
		add_two_ints_server()


	chmod +x add_two_ints_server.py		-python dosyasını çalıştırılabilir yaptık.

### add_two_ints_client.py
	import sys
	import rospy
	from beginner_tutorials.srv import *

	def add_two_ints_clients(x,y):
		rospy.wait_for_service('add_two_ints')
		try:
			add_two_ints=rospy.ServiceProxy('add_two_ints',AddTwoIns)
			resp1=add_two_ints(x,y)
			return resp1.sum
		except rospy.ServiceException, e:
			print "Serice call failed: %s"%e

	def usage():
		return "%s [x y]"%sys.argv[0]

	if __name__ = "__main__":
		if len(sys.argv)==3:
			x=int(sys.argv[1])
			y=int(sys.argv[2])
		else:
			print usage()
			sys.exit(1)
		print "Requesting %s+%s"%(x,y)
		print "%s + %s = %s"%(x,y,add_two_ints_client(x,y))


	chmod +x add_two_ints_client.py		-python dosyasını çalıştırılabilir yaptık.
	
	cd ~/catkin_ws
    	catkin_make
	
	roscore
	rosrun beginner_tutorials add_two_ints_server.py
	rosrun beginner_tutorials add_two_ints_client.py 1 3

## Verilerin Kaydedilmesi ve Oynatılması

	roscd beginner_tutorials 
	mkdir ~/bagfiles	kayıt için bir dosyalarını tutacağımız dosya oluşturduk.
	cd ~/bagfiles		
	
	rosrun turtlesim turtlesim_node 
	rosrun turtlesim turtle_teleop_key
	rosbag record -a			yayınlanan tüm verileri kaydettik.
	
	*kayıt işlemi başlatıldıktan sonra turtle kontrol edilir ve ctrl+c ile kapatılır.
	
	rosbag info kayıtdosyası.bag		kaydettiğimiz dosyayı okuduk.
	
	rosrun turtlesim turtlesim_node 
	rosbag play kayıtdosyası.bag		kaydettiğimiz dosyayı oynattık.
	
	rosbag play -r 2 kayıtdosyası.bag	kaydettiğimiz dosyayı -r seçeneği ile belirlenmiş bir faktörde değiştirebiliriz.
	
*bazı durumlarda kayıt dosyasını sadece belirli verileri kaydetmek için kullanmamız gerekebilir.
bu tip durumlarda aşağıdaki satırdaki gibi kayıt işlemi yapılabilir.*

	rosbag record -o subset /turtle1/cmd/vel /turtle1/pose	
	
## Roswtf ile Hataların Bulunması
	roscore
	roswtf		-çalışan ros paketlerinin ve düğümlerindeki hata ve uyarıları listeler.

## Sistem Bağlılıkları Yönetme
	rosdep install paket_ismi	-paketin ihtiyaç duyduğu tüm bağımlılıkları indirir.
	rosdep install turtlesim
	
	-hata alırsak eğer aşağıdaki satırlar uygulanarak tekrar çalıştırılmalıdır.
	sudo rosdep init
	rosdep update			-rosdep güncelenir.

	rosdep resolve paket_ismi	-bağımlılıkları çözümler.
	
## Kaynaklar
	
http://wiki.ros.org/ROS/Tutorials

http://robohub.org/programming-for-robotics-introduction-to-ros/
