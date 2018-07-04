# ImageAI Kütüğhanesi

ilk olarak ImageAI kütüphanesini kuralım.

    sudo pip3 install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.1/imageai-2.0.1-py3-none-any.whl 
 
ilk örnek için kullanacağımız RetinaNet modelini [indirelim.](https://github-production-release-asset-2e65be.s3.amazonaws.com/125932201/e7ab678c-6146-11e8-85cc-26bc1cd06ab0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20180704%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180704T165345Z&X-Amz-Expires=300&X-Amz-Signature=6d3991922771262f6d1b826823f20b3974e458d023b79db873d5f092c5c0e782&X-Amz-SignedHeaders=host&actor_id=33426517&response-content-disposition=attachment%3B%20filename%3Dresnet50_coco_best_v2.0.1.h5&response-content-type=application%2Foctet-stream)

İndirdiğimiz RetinaNet modelini ImageAI kütüphanesini kullanarak test edelim. 

    gedit FirstDetection.py

    from imageai.Detection import ObjectDetection
    import os

    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpeg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

    for eachObject in detections:
        print(eachObject["name"] + " : " + eachObject["percentage_probability"] )
        
Konumuzu çalıştıralım.

    python FirstDetection.py        

Test Image;

![Test Image](https://github.com/raclab/RACLAB/blob/master/images/AI/ImageAI_image.jpeg)

Sonuç;

![Result_Image](https://github.com/raclab/RACLAB/blob/master/images/AI/ImageAI_imagenew.jpg)
