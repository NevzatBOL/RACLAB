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

    gedit Makefile 
    
      GPU=1
      
     make
     
Opencv ile derlemek için;

    gedit Makefile 
    
      OPENCV=1  
      #Derlerken hata verirse aşağıdaki satır kullanılır.
      cv2=1
      
     make
    
## Hazır eğitilmiş model çalıştırma

ilk olrak ağırlık dosyasını indirelim.
   
    wget https://pjreddie.com/media/files/yolov3.weights
    
Referans Link:

https://pjreddie.com/darknet/
