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


Referans Link:

https://pjreddie.com/darknet/

https://blog.paperspace.com/how-to-implement-a-yolo-object-detector-in-pytorch/
