# OPENCV KURULUMU

#### ROS Kinetic ile birlikte opencv3.2 sürümü kurulu olarak geldiği için opencv kurulumu yapmaya gerek yoktur. python 2.7 de opencv direk import edilebilir.

Kurulum yapmak isteyenler için;

### Metod1:
	sudo apt-get install python-opencv
Komut ile Opencv Kurulması Halinde Linux'ta kamera fonksiyonu çalışmayacaktır.

### Metod2:
	sudo apt-get update
	sudo apt-get upgrade

	sudo apt-get install build-essential cmake git pkg-config
	sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev	

*eğer libtiff4-dev kütüphanesi bulunamazsa bunun yerine libtiff5-dev kullanılabilir.*

	sudo apt-get install libgtk2.0-dev libgtk-3-dev
	sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
	sudo apt-get install libxvidcore-dev libx264-dev



	sudo apt-get install libatlas-base-dev gfortran
	sudo apt-get install python2.7-dev python3.5-dev



	cd ~
	wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
	unzip opencv.zip
	
	wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
	unzip opencv_contrib.zip



	sudo apt-get install python-pip
	sudo pip install numpy



	sudo pip install virtualenv virtualenvwrapper
	
	export WORKON_HOME=$HOME/.virtualenvs
	source /usr/local/bin/virtualenvwrapper.sh
	
	echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bashrc
	echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
	
	echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
	source ~/.bashrc

	mkvirtualenv cv -p python2



	workon cv
	cd ~/opencv-3.3.0/
	mkdir build
	cd build

	cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D INSTALL_C_EXAMPLES=OFF \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules \
	-D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
	-D BUILD_EXAMPLES=ON ..



	make -j4
	sudo make install
	sudo ldconfig



	cd ~/.virtualenvs/cv/lib/python2.7/site-packages/
	ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so

*Eğer /usr/local/lib/python2.7/site-packages/ konumu boşsa aşağıdaki satır kullanılmalıdır.*

	ln -s /usr/local/lib/python2.7/dist-packages/cv2.so cv2.so

Kurulum tamamlandı.

	python
	>>> import cv2
	>>> cv2.__version__
	'3.3.0'

kurulumu kontrol edebiliriz.


*Eğer opencv kurulumu tamamlandı ve kurulan terminalde çalıştığı halde 
yeni açılan terminallerde çalışmıyorsa aşağıdaki işlemler uygulanmalıdır.*

	sudo nano ~/.bashrc
	export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH yada
	export PYTHONPATH=/usr/local/lib/python2.7/dist-packages:$PYTHONPATH 
	.bashrc dosyasına bu satır(cv2.so dosyasının bulunduğu konum) eklenerek kaydedilir.

**Raspberry Pi için;**

	sudo raspi-config
	Advanced Options > Expand Filesystem
	reboot

*Komutları uygulanarak opencv kurulumu için hazır hale getirilir.Eğer görüntü sadece raspberry pi kamera modülünden alınacaksa Metod1 ile, harici kameradan görüntü alınacaksa Metod2 Kullanılarak kurulum tamamlanır.*

Referans Link:

Ubuntu için:

http://pythonopencv.com/install-opencv-3-3-and-python2-7-3-5-bindings-on-ubuntu-16-04/
https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/

Raspberry Pi için:

https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/


# PYTHON2.7 VE OPENCV3.2 ÖRNEK UYGULAMALAR

**ornk1: Resim Üzerinde Başka Bir Parça Arama**

**ornk2: Resim Üzerinde Birden Çok Parça Arama**

**ornk3: Renk Filtresi Oluşturma**

**ornk4: Renk Filtresi**

**ornk5: Renk Kümeleme**

**ornk6: Araba Takip Etme**

**ornk7: Hareket Algılama1**

**ornk8: Hareket Algılama2**

**ornk9: Hareket Algılama3**

**ornk10: İnsan Takibi**

**ornk11: Sekil Algılama1**

**ornk12: Sekil Algılama2**

**ornk13: Renk ve Sekil Algılama**

**ornk14: Yüz ve Göz Algılama**

**ornk15: Yüz ve Göz Algılama**

**ornk16: QR Kod Okuma**

**ornk17: Resmi 16'ya Böleme ve Parçaları Karıştırıp Tekrar Birleştirme**

**ornk18: Resimden Text Çekme**

# Kaynaklar:

[sentdex python&opencv youtube kanalı](https://www.youtube.com/watch?v=Z78zbnLlPUA&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq)

[python&opencv blog](http://mavienginberk.blogspot.com.tr/search/label/opencv%20python)

[opencv tutorial](https://docs.opencv.org/trunk/d6/d00/tutorial_py_root.html)

[python&opencv örnek uygulamalar](https://www.pyimagesearch.com/)
