# Neural Networks

## Single Layer Neural Networks

![Single Layer](https://github.com/raclab/RACLAB/blob/master/images/AI/singlelayer.jpeg)

![Perseptrons](https://github.com/raclab/RACLAB/blob/master/images/AI/node.jpeg)

## Multi Layer Neural Networks

![Multi Layer](https://github.com/raclab/RACLAB/blob/master/images/AI/multilayer.png)

![Function](https://github.com/raclab/RACLAB/blob/master/images/AI/node2.png)

## Aktivasyon Fonksiyonları

![Atiactivation Function](https://github.com/raclab/RACLAB/blob/master/images/AI/activationfunction.png)

![Relu](https://github.com/raclab/RACLAB/blob/master/images/AI/relu.png)

# Keras ile Deep Learning

## Kanser Tespiti

https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/ 

Sitesinden 	*breast-cancer-wisconsin.data* dataset'imizi indiriyoruz.

    #-*-coding: cp1254-*-

    from keras.models import Sequential
    from keras.layers import Dense, Dropout, Activation
    import keras
    from keras.layers import Input, Dense
    from keras.optimizers import SGD

    from sklearn.preprocessing import Imputer
    import numpy as np
    import pandas as pd

    veri=pd.read_csv("breast-cancer-wisconsin.data") #Dataset'imizi okuduk.

    veri.replace('?', -99999, inplace=True)

    veriyeni=veri.drop(['1000025'],axis=1)

    imp=Imputer(missing_values=-99999,strategy="mean",axis=0)
    veriyeni=imp.fit_transform(veriyeni)

    giris=veriyeni[:,0:8] #input matrisi
    cikis=veriyeni[:,9] #output matrisi

    print giris.shape
    print cikis.shape

    model = Sequential() #Ardışık Model oluşturduk.
    #1. hiden Layer
    model.add(Dense(128,input_dim=8)) #Dense(Node Sayısı, input_dim=input sayısı)
    model.add(Activation('relu')) #Aktivasyon fonksiyonunu belirledik.
    #2. hiden Layer
    model.add(Dense(64))
    model.add(Activation('relu'))
    #Output Layer
    model.add(Dense(32))
    model.add(Activation('softmax')) #Output aktivasyon fonksiyonu "softmax" 'dir.

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    #ilk olarak optimizasyon fonksiyonumuzu belirledik, loss kayıp fonksiyonumuzu belirledik, metrics algoritmanın doğru yada yanlış yaptığını anlamasını sağlayacak yöntemi belirledik.

    model.fit(giris,cikis,epochs=5,batch_size=32,validation_split=0.13)
    #fit ile oluşturduğumuz modeli çalıştırma parametrelerini girdik.
    #epochs kaç defa sistemin eğitileceği
    #batch_size Tek seferde ne kadar verimizin ağdan geçeğini belirtir.
    #validation_split data setimizin % kaçını test için ayıracağımızı belirtiriz.

    #Eğitim çıktıları 
    #loss: Train verisi üzerindeki hata oranı
    #acc: Train verisi üzerindeki doğruluk oranı 
    #val_loss: test datasına göre hata oranı
    #val_acc: test datasına göre doğruluk oranı

    tahmin1=np.array([6,1,1,1,2,1,3,1]).reshape(1,8) #tahmin datası oluşturduk.
    print model.predict_classes(tahmin1) #oluşturduğumuz tahmin hatrisini modelimize verdik.

    tahmin2=np.array([10,5,5,3,6,7,7,10]).reshape(1,8)
    print model.predict_classes(tahmin2)
 
## Neural Network modeli Oluşturma

    model = Sequential() #Ardışık Model oluşturduk.
    
    model.add(Dense(128,input_dim=8)) #Dense(Node Sayısı, input_dim=input sayısı)
    model.add(Activation('relu')) #Aktivasyon fonksiyonunu belirledik.
    
    model.add(Dense(128,input_dim=8,activation='relu')) #Dense(Node Sayısı, input_dim=input sayısı, activation=Aktivasyon fonksiyonu) şeklinde tek satırda da oluşturulabilir.
    
## Aktivasyon Fonksiyonları

Bazı Aktivasyon fonksiyonları;

    model.add(Activation('relu'))
    model.add(Activation('sigmoid'))
    model.add(Activation('tanh'))
    model.add(Activation('linear'))
    model.add(Activation('softmax'))
    
Referans link: [Keras Aktivation Function](https://keras.io/activations/)  
    
## Hata(Loss) Fonsiyonları 
    
Bazı Hata Fonksiyonları;

mean_squared_error

![MSE](https://github.com/raclab/RACLAB/blob/master/images/AI/mse.png)

mean_absolute_error

![MAE](https://github.com/raclab/RACLAB/blob/master/images/AI/mae.png)

root_mean_square_error

![RMSE](https://github.com/raclab/RACLAB/blob/master/images/AI/rmse.png)

Referans link: [Keras Loss Function](https://keras.io/losses/)

## Optimizasyon Fonksiyonları

optimizasyon fonksiyonları, Loss değerine göre yapay sinir ağlarının ağırlık değerlerini düzenleyen fonksiyonlardır. Hata(loss) minimize edilmeye çalışılır.

    from keras import optimizers

    optimizer=optimizers.adam()	#parametre girilmezse default paremetreler kullanılır.
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

Bazı Optimizasyon Fonksiyonları;

    optimizer=optimizers.SGD(lr=0.01, momentum=0.0, decay=0.0, nesterov=False)
    optimizer=optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0)
    optimizer=optimizers.Adagrad(lr=0.01, epsilon=None, decay=0.0)
    optimizer=optimizers.Adadelta(lr=1.0, rho=0.95, epsilon=None, decay=0.0)
    optimizer=optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)

### Learning Rate

hatayı minimize ederken optimizasyon fonksiyonun nekdar büyüklükteki adımlar ile minimize edeceğini belirten değerdir.
Çok büyük olması hatanın belirli bir değerden sonra azalmamasına neden olur. Çok küçük değer seçilmesi durumunda hatnın minimize edilmesi için epoch sayısı artılması gerekir.

    optimizer=optimizers.sgd(lr=0.1)
    
Referans link: [Keras Optimizer Function](https://keras.io/optimizers/)

## Metric Fonksiyonu

Metric fonksiyonu modelinizin performansını değerlendirmek için kullanılır. Bir metric fonksiyonu bir hata(loss) fonksiyonuna benzer ancak bir metric'in değerlendirilmesiyle elde edilen sonuçlar model eğitilirken kullanılmaz. 
 
Kullanılan Metric fonksiyonu 'accuracy' dir. Size 0-1 arasında bir doğruluk değerini gösterir. 

Referans link: [Keras Metric Function](https://keras.io/metrics/)

## Fit Fonksiyonu

    mode.fit( x, y, batch_size=32, epoch=10, verbose=1, callbacks=[],
    validation_split=0.0, validation_data=None, shuffle=True,
    class_weight=None, sample_weight=None)
    
    x: Giriş verisi 
    y: Giriş verisine ait Etiketler

    batch_size: Bir ileri çalışma ve geri yayılma esnasında kullanılacak örnek sayısı
    epoch: iterasyon sayısı Bütün veri setinin kaç kez tekrar eğitimde kullanılacağı

    verbose: eğitim esnasında verilecek ilerleme bilgisini ayarlayan parametre
        0 : stdout a bir çıkış yok
        1 : ilerleme çubuğuyla göster ‘[=====>............]’
        2 : her iterasyon için tek ilerleme çubuğu gösterir

    callbacks: Eğitim esnasında çalışıtırılan fonksiyonlar

    validation_split: (0. < x < 1). bir oran da verinin bir kısmını eğitimde kullanmayıp doğrulama -validation – için kullanılır. Meseala 0.2 demek Eğitim verisinin %20 sinin doğrulama işlemi için kullanılacağı anlamına gelir.    
    validation_data: Doğrulama verisini Eğitim verisinden ayrı olarak da verebiliriz.

    shuffle: Her iterasyonda eğitim verisinin sırasının karıştırılmasını sağlar. (True)

    class_weight: Eğitim esnasında loss hesaplanırken her sınıf için ayrı ağırlık parametresi (dict)
    sample_weight: Eğitim veri setinde loss hesabında her örnek için ayrı bir katsayı kullanımına imkan verir

Referans link: [Derin Deli Mavi Keras](http://derindelimavi.blogspot.com.tr/2017/01/keras-giris-1.html)

## Dropout Metodu

Dropout hiden layer'daki bazı düğümlerin rastgele iptal edilmesi prensibine dayanır. Eğitim hatasını azaltır.

![dropout](https://github.com/raclab/RACLAB/blob/master/images/AI/dropout.png)

    model.add(Dropout(0.5)) hiden layerlarda düğümlerin %50'sini siler.

Referans link: [Dropout Makale](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf)

# Convolution Neural Networks

![Convolution Neural Networks](https://github.com/raclab/RACLAB/blob/master/images/AI/convolutionlayer.png)

![Conv](https://github.com/raclab/RACLAB/blob/master/images/AI/convolutionlayer2.jpeg)

# Convolution Kernel

![conv kernel](https://github.com/raclab/RACLAB/blob/master/images/AI/convolutoin1.png)

Görüntü işlemede konvolüsyon, görüntü matrisleri üzerinde filtre matrislerin dolaştırılarak çarpılması işlemidir. Bu işlem görüntü üzerindeki farklı detayların ortaya çıkarılmasında kullanır. Oluşturulan filtre matrislerinin yani kernellerin parametreleri deep learning uygulamalarında rastgele olarak belirlenir. 

![out size](https://github.com/raclab/RACLAB/blob/master/images/AI/convolutoin2.jpeg)

konvolüsyon işleminden sonra elde edilen yeni görüntü matrisinin boyutu (Görüntü_Matrisi - Filtre_Matrisi)/Stride + 1 formülü ile bulunur. Stride filtre matrisinin dolaştırıldığı piksel aralık değeridir.

![padding](https://github.com/raclab/RACLAB/blob/master/images/AI/convolutoin3.jpeg)

Görüntü matrisine direk kernel uyulanması durumunda görüntün kenarları yoksayılmış olur. Görüntünün kenar piksellerinde önemli bilgiler içerebileceğinden istenmeyen bir durumdur ve kenar ekleme işlemi uygulanır. Kenar ekleme işlemi için görüntün kenarlarını sıfır ekleme (padding) ile sağlanır.

![depth](https://github.com/raclab/RACLAB/blob/master/images/AI/convolutoin4.jpeg)

Filtre kernelleri ile görüntü matrislerinin derinlik değerleri eşit olmalıdır. 

![depth](https://github.com/raclab/RACLAB/blob/master/images/AI/convolutoin5.jpeg)

Görüntüye uygulanan kernel sayısı elde edilen yeni çıktının derinlik değerini verir.

Örnek konvolüsyon uygulaması: [Convolutin Demo](http://cs231n.github.io/assets/conv-demo/index.html)

## Pooling

![pooling](https://github.com/raclab/RACLAB/blob/master/images/AI/pooling.jpeg)

pooling görüntün boyutlarını küçülterek datayları azaltmak için kullanılır. Genel itibari ile iki farklı pooling metodu vardır. 
Average Pooling: matrisin ortalama değerini alır. Ortalama değer çoğu durumda görüntüde olmayan değerlere karşılık geldiği için çok sık kullanılmaz.
Max Pooling: matrisin maksimum değerini alır. matrislerin en büyük değerleri en önemli piksellere karşılık geldiği için çok uygulanan metodtur.

## Keras ile Convolution Neural Networks

    # -*- coding: utf-8 -*-
    import numpy
    from keras.datasets import cifar10
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, Flatten
    from keras.constraints import maxnorm
    from keras.layers.convolutional import Conv2D, MaxPooling2D
    from keras.utils import np_utils
    from keras import backend as K
    K.set_image_dim_ordering('th')

    from matplotlib import pyplot
    from scipy.misc import toimage
    import scipy.misc
    from scipy import ndimage
    from scipy import misc

    #Dataset'i yükledik.
    (x_train, y_train),(x_test, y_test) = cifar10.load_data()

    #Dataları float32 formatına çevirdik.
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train = x_train/255.0
    x_test = x_test/255.0

    y_train = np_utils.to_categorical(y_train)
    y_test = np_utils.to_categorical(y_test)
    num_classes = y_test.shape[1]

    #Dataset'in her sınıfından birer resim göstertilir.
    for i in range(0,9):
        pyplot.subplot(330 + 1 + i)
        pyplot.imshow(toimage(x_train[i]))

    pyplot.show()

    #Model oluşturduk.
    model = Sequential()

    #1. Konvolüsyon
    model.add(Conv2D(32, kernel_size=(3, 3), input_shape=(3, 32, 32), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.2)) #piksel değerlerinin %20'sini sildik.
    #2. Konvolüsyon
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.2))
    model.add(MaxPooling2D(pool_size=(2, 2))) #Resmi Küçültük.

    #3. Konvolüsyon
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.2))
    #4. Konvolüsyon
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.2))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    #5. Konvolüsyon
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.2))
    #6. Konvolüsyon
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
    model.add(MaxPooling2D(pool_size=(2, 2)))


    model.add(Flatten()) #Görüntü matrisini vektör haline getirdik.
    #1. hiden layer
    model.add(Dense(1024, activation='relu', kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.2))
    #2. hiden layer
    model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.2))
    #Output layer
    model.add(Dense(num_classes, activation='softmax'))

    #Modelin hata, otimizasyon ve doğruluk fonksiyonunu belirledik.
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    print model.summary() #Oluşturduğumuz modeli yazdırdık.

    #oluşturduğumuz modeli Eğittik.
    model.fit(x_train,y_train,validation_data=(x_test, y_test),epochs=10,batch_size=64)

    #Eğittiğimiz modelin doğruluk oranını yazdırdık.
    scores = model.evaluate(x_test, y_test, verbose=0)
    print("Accuracy: %.2f%%" % (scores[1]*100))

    #Eğittiğimiz modeli dataset dışındaki resimler ile test ettik.
    kedi = ndimage.imread("kedi.jpg")
    kedi = scipy.misc.imresize(kedi,(32,32))
    kedi = numpy.array(kedi)
    kedi = kedi.reshape(1,3,32,32)

    print model.predict_classes(kedi)

    araba = ndimage.imread("araba.jpeg")
    araba = scipy.misc.imresize(araba,(32,32))
    araba = numpy.array(araba)
    araba = araba.reshape(1,3,32,32)

    print model.predict_classes(araba)

# ImageNet

![image net history](https://github.com/raclab/RACLAB/blob/master/images/AI/imagenet.jpeg)

## ImageNet Algorithms

### AlexNet - 2012 

![Alexnet](https://github.com/raclab/RACLAB/blob/master/images/AI/alexnet1.png)

![Alexnet paralel](https://github.com/raclab/RACLAB/blob/master/images/AI/alexnet2.png)

### ZfNet - 2013

![Zfnet](https://github.com/raclab/RACLAB/blob/master/images/AI/zfnet.png)

### VggNet - 2014

![Vggnet](https://github.com/raclab/RACLAB/blob/master/images/AI/vggnet.png)

### LeNet - 2014

![Lenet](https://github.com/raclab/RACLAB/blob/master/images/AI/lenet.png)

### ResNet - 2015

![ResNet](https://github.com/raclab/RACLAB/blob/master/images/AI/resnet.jpeg)

[ResNet-50](http://ethereon.github.io/netscope/#/gist/db945b393d40bfa26006)     [ResNet-101](http://ethereon.github.io/netscope/#/gist/b21e2aae116dc1ac7b50)        [ResNet-152](http://ethereon.github.io/netscope/#/gist/d38f3e6091952b45198b)
