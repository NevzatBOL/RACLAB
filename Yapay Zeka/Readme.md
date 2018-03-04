# Paket Kurulumları

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



