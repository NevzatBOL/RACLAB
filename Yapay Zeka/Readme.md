# Paket-Kurulumları

## CUDA 9.0 KURULUMU

https://developer.nvidia.com/cuda-90-download-archive

adresinden cuda paketi indirilir. (Linux>x86_64>Ubuntu>16.04>deb(local))

	sudo dpkg -i cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64.deb
	sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
	sudo apt-get update
	sudo apt-get install cuda-9.0

Komutları ile kurulum tamamlanır.

Referans Link:

https://github.com/earcz/NVIDIA-GPU-Surucusu-ve-CUDA-Yukleme/wiki/CUDA-Yukleme

## cuDNN 7.1.4 KURULUMU

https://developer.nvidia.com/rdp/cudnn-download

cuDNN v7.1.4 Library for Linux	Paketi indirilir.

indirilen paket açılır.

	tar -xzvf cudnn-9.0-linux-x64-v7.1.tgz
	
gerekli paketler cuda dizinine kopyalanır.


	sudo cp cuda/include/cudnn.h /usr/local/cuda/include
	sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
	sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*

Debian dosyaları indirilir ve kurulur.

cuDNN v7.1.4 Runtime Library for Ubuntu16.04 (Deb)

	sudo dpkg -i libcudnn7_7.1.4.18-1+cuda9.0_amd64.deb

cuDNN v7.1.4 Developer Library for Ubuntu16.04 (Deb)

	sudo dpkg -i libcudnn7-dev_7.1.4.18-1+cuda9.0_amd64.deb 

cuDNN v7.1.4 Code Samples and User Guide for Ubuntu16.04 (Deb)

	sudo dpkg -i libcudnn7-doc_7.1.4.18-1+cuda9.0_amd64.deb


Referans Link:

http://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html

## TensorFlow KURULUMU

python 2.7 için paket kurulumu

	sudo apt-get install python-pip			(pip kurulu değil ise önce pip kurulumu yapılır.)
	sudo pip2 install tensorflow-gpu			-gpu için
	sudo pip2 install tensorflow			-cpu için

python 3.5+ için paket kurulumu

	sudo apt-get install python3-pip			(pip kurulu değil ise önce pip kurulumu yapılır.)
	sudo pip3 install tensorflow-gpu			-gpu için
	sudo pip3 install tensorflow			-cpu için

Referans Link:

https://www.tensorflow.org/install/install_linux

## KERAS KURULUMU

python 2.7 için paket kurulumu
	
	sudo pip2 install keras

python 3.5+ için paket kurulumu
	
	sudo pip3 install keras

Referans Link:

https://keras.io/


# Kaynaklar

[jetson-inference](https://github.com/dusty-nv/jetson-inference)

[mit-cs231n](http://cs231n.github.io/)

[mit-cs231n-convolution-networks](http://cs231n.github.io/convolutional-networks/)

[Stanford Tutorials](http://ufldl.stanford.edu/tutorial/)

[Deel Learning Blog](https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/)

[Deep Learning Tutorials](http://deeplearning.net/tutorial/contents.html)

[LeNet Tutorial](http://deeplearning.net/tutorial/lenet.html)

[Neural Network](http://neuralnetworksanddeeplearning.com/chap1.html)              *Toplam 6 chapter*

[Deep Learning and Opencv](http://www.learnopencv.com/)

[IntelAIWorkshop](https://github.com/mstfldmr/IntelAIWorkshop)

[Deep Learning Türkiye](https://github.com/deeplearningturkiye/turkce-yapay-zeka-kaynaklari)

[Makine Öğrenmesi Youtube](https://www.youtube.com/channel/UCvaBuYQM07ZYa4NfZ3hRzvw/playlists)



