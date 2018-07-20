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

*C++ için opencv kurulu olması gerekir. kurulu değilse: sudo apt-get install libopencv* ile kurulum yapılır.

    gedit Makefile 
    
      OPENCV=1  
      
     make
    
## Hazır eğitilmiş model çalıştırma

ilk olrak ağırlık dosyasını indirelim.
   
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

video üzerinde modelimizi çalıştırmak için;

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

Datasetimizi oluşturmak için öncelikle train ve test klasörleri oluşturalım. oluşturduğumuz bu klasöre labelImg i kullanarak etiketlediğimiz resimleri txt olarak kaydedeceğiz. Etiketler ile resimlerin aynı dizinde olmasına dikkat edelim. Etiketleri test ve train olarak etiketleri sonradan ayıracağız.

     cd ~/yolo/darknet/
     mkdir -p datasets/images
     cd datasets/images
    
Datasetimizi labelImg'i kullanarak oluşturabiliriz. Resimlerin bulunduğu images dizinini Open Dir ile açalım. PascalVOC yerine YOLO seçeneği seçili olmalıdır. Her resim için resimde algılanmasını istediğimiz nesneyi Create RectBox ile seçelim, etiketleyelim ve kaydedelim. her resim için ayrı ayrı txt dosyası oluşturulacaktır. Ayrıca classes.txt isminde programın tüm etiket sınıflarının yer aldığı bir dosya oluşturulacaktır. 

    python3 labelImg.py

![LabelImages](https://github.com/raclab/RACLAB/blob/master/images/AI/labelimg_example.jpg)

Etiket çıktıları aşağıdaki gibi olacaktır.

    *15 classes.txt içerisinde yer alan etiketin indexini belirtir. 
    <object-class> <x> <y> <width> <height>
    
    15 0.600000 0.363636 0.050746 0.296970
    15 0.014925 0.543939 0.023881 0.166667

Elusturduğumuz etiketlerin resimlerinin yollarını tek dosyada toplalamız gerekli bunun için;

*burda oluşturduğumuz etiketleri train ve test olarak ayırdık. (%10 test datası)*

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

yolo'da eğitim yapabilmemiz için aşağıdaki üç dosyanın oluşturulması gereklidir.

`cfg/obj.data
cfg/obj.names
cfg/Yolo-obj.cfg`

    cd ~/yolo/darknet/cfg
    
    gedit obj.data
    
    classes= 15  
    train  = datasets/images/train.txt  
    valid  = datasets/images/test.txt  
    names = data/obj.names  
    backup = backup/ 

*classes sayısı classes.txt deki etiket sayısı ile aynı olmalıdır.*

obj.names dosyası içerisine classes.txt'de yer alan etiketler yazılmalıdır.

    cd ~/yolo/darknet/data
    
    gedit obj.names
    
    dog
    person
    cat
    tv
    car
    meatballs
    marinara sauce
    tomato soup
    chicken noodle soup
    french onion soup
    chicken breast
    ribs
    pulled pork
    hamburger
    cavity
    light

Eğitim yapacağımız modelin configürasyon dosyasını oluşturulalım. Bunun için yolov3.cfg dosyasını kopyalayalım ve üzerinde düzenlemeler yapalım.

    cd ~/yolo/darknet/cfg
    
    cp yolov3.cfg yolov3-obj.cfg

    gedit yolov3-obj.cfg 
    
    batch=64
    subdivisions=8 #Gpu miktarı az ise değer artırılabilir.
    classes=15
    
Referans Link:

https://pjreddie.com/darknet/

https://blog.paperspace.com/how-to-implement-a-yolo-object-detector-in-pytorch/

https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/

https://medium.com/@ribomo42/how-to-train-yolo-v2-with-your-own-data-object-and-labels-on-darknet-2b90dbfecb02
