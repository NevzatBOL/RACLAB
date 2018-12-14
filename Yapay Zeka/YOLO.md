# YOLO With Object Detection

Darknet'i indirelim ve CPU derliyelim.

    mkdir yolo
    cd yolo
    git clone https://github.com/pjreddie/darknet.git
    cd darknet/
    make

hata almadan tamamlandı ise;
  
    ./darknet
    
    Çıktı;
    usage: ./darknet <function>

GPU ile dermeke için;

*Cuda kurulu olması gerekir. nvcc not found hatası alınırsa sudo apt-get install nvidia-cuda-toolkit yapılmalıdır.*

    gedit Makefile 
    
      GPU=1
      
     make
     
Opencv ile derlemek için;

*C++ için opencv kurulu olması gerekir. kurulu değilse: sudo apt-get install libopencv** ile kurulum yapılır.

    gedit Makefile 
    
      OPENCV=1  
      
    make

Kullanmakta olduğum Makefile Dosyası aşağıdaki gibidir.

    gedit Makefile 

      GPU=1
      CUDNN=1
      OPENCV=1
      OPENMP=0
      DEBUG=0
    
    make
    
## Hazır eğitilmiş model çalıştırma

ilk olarak ağırlık dosyasını indirelim.
   
    wget https://pjreddie.com/media/files/yolov3.weights
    
indirdiğimiz ağırlık parametreleri ile modelimizi test edelim.

    ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
    
Yolo varsayılan olarak eşik değerini %25 te tutar. Eşik değerini değiştirerek modelimizi çalıştırabiliriz.

    ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg -thresh 0.5

İşlem gücü düşük cihazlar için yolov3-tiny ağırlık dosyaları indirilerek çalıştırılabilir.

    wget https://pjreddie.com/media/files/yolov3-tiny.weights

yolov3-tiny modelini çalıştıralım.

    ./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights data/dog.jpg

Kameradan alınan görüntü ile modelimizi çalıştırıalım.

*Kameradan anlık gönrüntü ile çalıştırmak için darknet'in Cuda ve opencv ile derlenmiş olması gerekir.*

    ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights

**Bilgisayarın işlem hızına göre fps düşük olabilir. yolov3-tiny modeli kullanılarak daha yüksek fps'lerde işlem yapılabilir.**

**işlem hızı düşük modeller daha başarılı sonuçlar verir fakat gerçek zamanlı uygulamalarda geçikme meydana gelebilir.**

    ./darknet detector demo cfg/coco.data cfg/yolov3-tiny.cfg yolov3-tiny.weights

Video üzerinde modelimizi çalıştırmak için;

    ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights <video file>
   
# Kendi Dataset'imiz ile object detection

Kendi datasetimizi oluşturmak için ilk olarak labelImg programını indirelim.

    cd ~/yolo
    git clone https://github.com/tzutalin/labelImg.git
  
indirdiğimiz labelImg için gerekli olan paket kurulumlarını yapalım.

    sudo apt-get install pyqt5-dev-tools
    sudo pip3 install lxml
    cd ~/yolo/labelImg/
    make qt5py3

lableImg'de default olarak gelen etiketleri değiştirmek isterseniz labelImg/data/predefined_classes.txt içerisinde yer alan etiketler değiştirilebilir.

Datasetimizi oluşturan resimleri images klasöründe tutalım. Oluşturacağımız etikerleri ise labels klasörüne kaydetmeliyiz. labels klasörüne labelImg i kullanarak etiketlediğimiz txt olarak kaydedeceğiz. Frameleri test ve train olarak hepsini etiketledikten sonradan ayıracağız.

     cd ~/yolo/darknet/
     mkdir datasets
     cd datasets/
     mkdir images
     mkdir labels
     cd images/
    
Datasetimizi labelImg'i kullanarak oluşturabiliriz. Resimlerin bulunduğu images dizinini Open Dir ile açalım. PascalVOC yerine **YOLO** seçeneği seçili olmalıdır. Her resim için resimde algılanmasını istediğimiz nesneyi Create RectBox ile seçelim, etiketleyelim ve kaydedelim. her resim için ayrı ayrı txt dosyası oluşturulacaktır. Ayrıca classes.txt isminde programın tüm etiket sınıflarının yer aldığı bir dosya oluşturulacaktır. 

    python3 labelImg.py

![LabelImages](https://github.com/raclab/RACLAB/blob/master/images/AI/labelimg_example.jpg)

Etiket çıktıları aşağıdaki gibi olacaktır.

    *5 classes.txt içerisinde yer alan etiketin indexini belirtir. 
    <object-class> <x> <y> <width> <height>
    
    5 0.600000 0.363636 0.050746 0.296970
    5 0.014925 0.543939 0.023881 0.166667

Datasetimiz içerisinde yer alan resimlerinin yollarını tek dosyada toplalamız gerekli bunun için aşağıdaki kod kullanılabilir.

*Burda oluşturduğumuz etiketleri train ve test olarak ayırdık. (%10 test datası)*

    gedit data.py

    #-*-coding: utf-8 -*-
    import glob, os

    # bulundugumuz dizin
    current_dir = os.path.dirname(os.path.abspath(__file__))

    #darknet.exe'ye göre datanın konumu
    path_data = 'datasets/images/'

    # Test icin kullanılacak datanın % degeri
    percentage_test = 10;

    # train.txt ve test.txt dosyalarını olusturduk.
    file_train = open('train.txt', 'w')  
    file_test = open('test.txt', 'w')

    # datalarımızı train ve test olarak dagıtalım
    counter = 1  
    index_test = round(100 / percentage_test)  
    for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):  
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))

        if counter == index_test:
            counter = 1
            file_test.write(path_data + title + '.jpg' + "\n")
        else:
            file_train.write(path_data + title + '.jpg' + "\n")
            counter = counter + 1

    data.py

**Bu kod ile test ve train olarak ayırdığımızda farklı etiketler için ayrı ayrı %10'luk validation datası ayrılmaz tüm datanın rastgele %10'u alınır. Farklı etiketler için ayrı ayrı %10'luk test datası oluşturmak için aşağıdaki kod üzerinde düzenlemeler yaparak kullanabilirsiniz.**

    gedit data_split.py

    #-*-coding: utf-8 -*-
    import glob
    import numpy as np

    #images içerisinde yer alan farklı sınıflara ait resimlerin isimleri
    #aynı sınıfa ait resimler için isimlerin, isimsayı.jpg şekilde isimlendirildiği düsünülmüstür.
    name_class = ['Durak','Girilmez','Kirmizi_Isik','Yesil_Isik','Park_Yapilmaz','Saga_Donulmez','Sola_Donulmez']
    counter = np.zeros(len(name_class))

    #darknet.exe'ye göre datanın konumu
    path_data = 'datasets/images/'

    # Test icin kullanılacak datanın % degeri
    validation_test = 10

    # train.txt ve test.txt dosyalarını olusturduk.
    file_train = open('train.txt', 'w')  
    file_test = open('test.txt', 'w')

    #datayı test ve train olarak ayırdık.
    def yaz(name):
        for i in range(len(name_class)):
            if name_class[i] == name[:-5] or name_class[i] == name[:-6]: #resimlerin sayı.jpg kısımları cıkartılacak sekilde sondan kırpma islemi uygulanmalıdır.
                counter[i] +=1
                if counter[i] % validation_test == 0:
                    file_test.write(path_data + name + "\n")
                else :
                    file_train.write(path_data + name + "\n")	

                break

    for file_name in glob.glob('*.jpg'):
        yaz(file_name)

    python data_split.py

Yolo'da eğitim yapabilmemiz için aşağıdaki üç dosyanın oluşturulması gereklidir.

`cfg/obj.data
cfg/obj.names
cfg/Yolo-obj.cfg`

    cd ~/yolo/darknet/cfg
    
    gedit obj.data
    
    classes= 7  
    train  = datasets/images/train.txt  
    valid  = datasets/images/test.txt  
    names = data/obj.names  
    backup = backup/ 

*classes sayısı classes.txt deki etiket sayısı ile aynı olmalıdır.*

obj.names dosyası içerisine classes.txt'de yer alan etiketler yazılmalıdır.

    cd ~/yolo/darknet/data
    
    gedit obj.names
    
    Durak
    Girilmez
    Park Yapilmaz
    Sola Donulmez
    Saga Donulmez
    Yesil Isik
    Kirmizi Isik

Eğitim yapacağımız modelin configürasyon dosyasını oluşturulalım. Bunun için yolov2.cfg dosyasını kopyalayalım ve üzerinde düzenlemeler yapalım.

    cd ~/yolo/darknet/cfg
    
    cp yolov2.cfg yolov2-obj.cfg

    gedit yolov2-obj.cfg 
    
    #dosyanın en başında yer alan aşağıdaki iki satır düzenlenebilir.
    batch=64 #aynı anda işleme sokulacak resim sayısı.
    subdivisions=8 #Gpu miktarı az ise değer artırılabilir.
    
    #dosyanın en altında yer alan aşağıdaki iki satır değiştirilmelidir.
    filters=60 #filters=(classes + coords + 1)*num = (7+4+1)*5 = 60
    classes=7
   
Modelimizi Eğitmek için;

    ./darknet detector train cfg/obj.data cfg/yolov2-obj.cfg

Doğru ağırlık parametrelerine ulaşmak için daha önce eğitilmiş bir modelin ağırlık parametrelerini yükleyerek eğitim yapmak için;

    ./darknet detector train cfg/obj.data cfg/yolov2-obj.cfg <weight file>

Birden fazla GPU çalıştırarak eğitim yapmak için;

    ./darknet detector train cfg/obj.data cfg/yolov2-obj.cfg -gpus 0,1,2,3

Bir checkpoint'de eğitimi durdurur ve tekrar başlatmak isterseniz;
    
    ./darknet detector train cfg/obj.data cfg/yolov2-obj.cfg backup/yolov2-obj.backup

Eğitim sonrasında ağırlık parametreleri backup içerisinde yer alır. Ağırık parametrelerini kullanarak modelimizi gerçek zamanlı olarak çalıştıralım.

    ./darknet detector demo cfg/obj.data cfg/yolov2-obj.cfg backup/yolov2-obj_10000.weights

Referans Link:

https://pjreddie.com/darknet/

https://blog.paperspace.com/how-to-implement-a-yolo-object-detector-in-pytorch/

https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/

# yolo ile Classification

ImageNet üzerinde eğitilmiş modelin ağırlık dosyalarını indirelim ve test edelim.

    wget https://pjreddie.com/media/files/extraction.weights
    
    ./darknet classifier predict cfg/imagenet1k.data cfg/extraction.cfg extraction.weights data/dog.jpg
    
bir resim yolu belirtmeden modeli yüklerseniz test için sizden resim yolu isteyecektir. Böylece herseferinde modeli tekrar yüklemeye gerek kalmadan istediğiniz kadar resimi test edebilirsiniz. İşlemi sonlandırmak için ctrl+c komutunu kullanın.

    ./darknet classifier predict cfg/imagenet1k.data cfg/extraction.cfg extraction.weights

# yolo ile Nightmare


VGG-16 modelini kullanarak yapay zekanın her iterasyonda resimleri nasıl algıladığını ve değiştirdiğini görelim. Google'ın yapmış olduğu çalışmayı, [Inceptionism: Going Deeper into Neural Networks](https://ai.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html) bu makeleden okuyabilirsiniz. VGG-16 modelimizin ağırlık dosyalarını indirelim ve test edelim.

    wget https://pjreddie.com/media/files/vgg-conv.weights
 
    ./darknet nightmare cfg/vgg-conv.cfg vgg-conv.weights data/dog.jpg 7
    
iterasyon sayısı artıkça da karışık resimler ortaya çıkmaya başlayacaktır. Modelin çalışma parameterlerinde biraz daha oynayarak farklı sonuçlar elde edebilirsiniz.

    ./darknet nightmare cfg/vgg-conv.cfg vgg-conv.weights \data/scream.jpg 10 -range 3 -iters 20 -rate .01 -rounds 4
    
*-rounds n: mermi sayısını değiştir (varsayılan 1). Daha fazla mermi, daha çok görüntü oluşturduğunu ve genellikle orijinal görüntüde daha fazla değişiklik anlamına gelir.

-iters n: tur başına yineleme sayısını değiştir (varsayılan 10). Daha fazla yineleme, görüntü başına turda daha fazla değişiklik anlamına gelir.

-range n: olası katmanların aralığını değiştir (varsayılan 1). Bire ayarlanırsa, her yinelemede yalnızca verilen katman seçilir. Aksi takdirde, aralıktan farklı olarak bir katman seçilir (örneğin 10-3, 9-11 katmanları arasında seçim yapar).

-octaves n: olası ölçeklerin sayısını değiştir (varsayılan 4). Bir octaves'da, sadece tam boyutlu görüntü incelenir. Her ek octaves, görüntünün daha küçük bir versiyonunu ekler (önceki octaves'ın 3/4'ü).

-rate x: Görüntü için öğrenme hızını değiştir (varsayılan .05). Daha yüksek, görüntü başına yineleme başına daha fazla değişiklik anlamına gelir aynı zamanda bazı kararsızlık ve belirsizlikler getirir.

-thresh x: büyütülecek özellikler için eşiği değiştir (varsayılan 1.0). x Hedef katmanda sadece standart sapmaların ortalamadan uzak özellikleri büyütülür. Daha yüksek bir eşik daha az özelliğin daha büyük olduğu anlamına gelir.

-zoom x: her turdan sonra görüntüye uygulanan yakınlaştırmayı değiştir (varsayılan 1.0). İsteğe bağlı olarak, her turdan sonra görüntüye uygulanacak bir yakınlaştırma (x <1) veya uzaklaştırma (x> 1) ekleyebilirsiniz.

-rotate x: Her turdan sonra uygulanan dönüşü değiştir (varsayılan 0.0).*

# yolo ile RNN

RNN ile ilgli [bu](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) makeleyi okuyabilirsiniz.

George RR Martin ağırlık dosyasını indirmek için;
    
    wget https://pjreddie.com/media/files/grrm.weights
    
    ./darknet rnn generate cfg/rnn.cfg grrm.weights -srand 0 -seed JON

William Shakespeare ağırlık dosyasını indirmek için;
    
    wget https://pjreddie.com/media/files/shakespeare.weights
    
    ./darknet rnn generate cfg/rnn.cfg shakespeare.weights -srand 0

Leo Tolstoy ağırlık dosyasını indirmek için;

    wget https://pjreddie.com/media/files/tolstoy.weights
    
    ./darknet rnn generate cfg/rnn.cfg tolstoy.weights -srand 0 -seed Chapter

Immanuel Kant ağırlık dosyasını indirmek için;

    wget https://pjreddie.com/media/files/kant.weights
    
    ./darknet rnn generate cfg/rnn.cfg kant.weights -srand 0 -seed Thus -temp .8
    
Kendi modelinizi eğitmek için;

    ./darknet rnn train cfg/rnn.train.cfg -file data.txt
    
Eğitimi istediğiniz checkpoint'ten başlatabilirsiniz.    

    ./darknet rnn train cfg/rnn.train.cfg backup/rnn.train.backup -file data.txt
