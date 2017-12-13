# Paket-Kurulumları

## CUDA 8.0 KURULUMU

https://developer.nvidia.com/cuda-80-ga2-download-archive

adresinden cuda paketi indirilir. (Linux>x86_64>Ubuntu>16.04>deb(local))

	sudo dpkg -i cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb
	sudo apt-get update
	sudo apt-get install cuda-8.0

Komutları ile kurulum tamamlanır.

## cuDNN 6.0 KURULUMU

https://developer.nvidia.com/rdp/cudnn-download

cuDNN v6.0 Library for Linux	Paketi indirilir.

indirilen paket açılır.

	tar -xzvf cudnn-8.0-linux-x64-v6.0.tgz

gerekli paketler cuda dizinine kopyalanır.


	sudo cp cuda/include/cudnn.h /usr/local/cuda/include
	sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
	sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*

Debian dosyaları indirilir ve kurulur.

cuDNN v6.0 Runtime Library for Ubuntu16.04 (Deb)

	sudo dpkg -i libcudnn6_6.0.21-1+cuda8.0_amd64.deb

cuDNN v6.0 Developer Library for Ubuntu16.04 (Deb)

	sudo dpkg -i libcudnn6-dev_6.0.21-1+cuda8.0_amd64.deb

cuDNN v6.0 Code Samples and User Guide for Ubuntu16.04 (Deb)

	sudo dpkg -i libcudnn6-doc_6.0.21-1+cuda8.0_amd64.deb


Referans Link:

http://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html

## TensorFlow KURULUMU

python 2.7 GPU için paket kurulumu

	sudo apt-get install python-pip			(pip kurulu değil ise önce pip kurulumu yapılır.)
	sudo pip install tensorflow-gpu			-gpu için
	sudo pip install tensorflow			-cpu için

Referans Link:

https://www.tensorflow.org/install/install_linux

## KERAS KURULUMU

python 2.7 için paket kurulumu
	
	sudo pip install keras

Referans Link:

https://keras.io/

## ZED KAMERA SDK KURULUMU

https://www.stereolabs.com/developers/release/2.2/

Adresinden CUDA 8 için ZED SDK for Linux paketi indirilir.

indirilen pakete çalışma izni verilir.

	sudo chmod +x ZED_SDK_Linux_Ubuntu16_CUDA8_v2.2.0.run

indirilen paket çalıştırılarak kurulum tamamlanır.

	./ZED_SDK_Linux_Ubuntu16_CUDA8_v2.2.0.run
	
### ZED KAMERA PYTHON3 PAKET KURULUMU
https://github.com/stereolabs/zed-python

Adresinden python3.5+ için pyzed kütüphanesi indirilir.

	sudo apt-get install python3-pip
	sudo pip3 install cython
	sudo pip3 install numpy
	
	python3 setup.py build
	python3 setup.py install
pyzed kütüphanesinin kurulumu tamamlanır.

#### pyzed kütüphanesinin yanında ihtiyacımız olan diğer kütüphanelerin kurulumları;

https://pypi.python.org/pypi/PyOpenGL/3.1.1a1#downloads

Adresinden PyOpenGL-3.1.1a1.tar.gz dosyası indirilir.
	
	tar -zxvf PyOpenGL-3.1.1a1.tar.gz
	cd PyOpenGL-3.1.1a1
	python3 setup.py install

opencv kurulumu aşağıda anlatılan uzun yöntemle yapılabileceği gibi görüntü pyzed kütüphanesinden alınacağından dolayı aşağıdaki komut ilede opencv kurulumu yapılabilir.

	sudo install pip3 opencv-python
	
## ROS KİNETİC KURULUMU

	sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

	sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

	sudo apt-get update


	sudo apt-get install ros-kinetic-desktop-full


	sudo rosdep init
	rosdep update


	echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
	source ~/.bashrc
	source /opt/ros/kinetic/setup.bash

	sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential

Referans Link:
http://wiki.ros.org/kinetic/Installation/Ubuntu

## OPENCV KURULUMU

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

## BAZI PYTHON PAKETLERİNİN KURULUMU

### Kütüphane kurmada kullanılabilecek metodlar;

	sudo apt-get install python-pip			(pip kurulu değil ise önce pip kurulumu yapılır.)
	
	sudo apt-get install python-kütüphane_adı
	sudo pip install kütüphane_adı
	pip search kütüphane_adı 	Kütüphane aramada kullanılır.



	matplotlib	sudo pip install matplotlib

	PIL(Pillow)	sudo pip install Pillow


	zbar		sudo apt-get install libzbar-dev	
			sudo pip install zbar			qr kod okuma kütüphanesi


	sklearn 	sudo pip install sklearn		yapay zeka kütüphanesi
	scipy		sudo pip install scipy			sklearn için gerekli.


	pytesseract	sudo pip install pytesseract		görüntüden text çekmek için kullanılır.
	tesseract	sudo apt-get install tesseract-ocr	pytesseract için gerekli.















