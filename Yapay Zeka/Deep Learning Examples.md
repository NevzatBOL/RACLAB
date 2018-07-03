# Tensorflow ile Object Detection

ilk olarak bir çalışma dizini oluşturalım ve tensorflow'un model paketini indirelim.

    mkdir object_detection
    cd object_detection
    git clone https://github.com/tensorflow/models.git

Linux için protoc-3.6.0-linux-x86_64.zip'u [indirelim.](https://github.com/google/protobuf/releases) indirdiğimiz dosyanın içerisinde bin klasörünün içinde yer alan protoc dosyasını /usr/local/bin/ klasörüne atalım ve protoc dosyasını çalıştırılabilir yapalım.

    sudo cp protoc ~ /usr/local/bin/
    sudo chmod 777 protoc
    
Oluşturduğumuz object_detection klasörüne gidelim.

    cd ~/object_detection
    cd models/research
  
    protoc object_detection/protos/*.proto --python_out=.
    export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
    
İlk örneğimizi çalıştıralım. Bunun için ilk olarak models/research/object_detection klasörüne gidelim ve jupyter ile object_detection_tutorial.ipynb çalıştıralım.

    cd ~/object_detection/models/research/object_detection
    jupyter-notebook object_detection_tutorial.ipynb

    kernel -> Restart & Run All ile tüm kodları çalıştıralım.
    
Kod her çalıştığında model dosyasını yeniden indirecektir. Model dosyasının yeniden inmesini önlemek için Download Model'in altında yer alan aşağıdaki satırları yorum satırı yapabilirsiniz.

    #opener = urllib.request.URLopener()
    #opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)

Gerçek zamanlı olarak hazır dataset ve model üzerinden çalışan jupyter ile test ettiğimiz kodları aşağıdaki gibi düzenlerek kullanabilirsiniz.

    gedit object_detection_tutorial.py 

    import numpy as np
    import cv2
    import sys
    import os

    import six.moves.urllib as urllib
    import tarfile
    import tensorflow as tf


    #Object detection imports
    sys.path.append("..")

    from utils import label_map_util
    from utils import visualization_utils as vis_util

    cap = cv2.VideoCapture(0)

    #Model preparation 

    #Variables
    #What model to download.
    MODEL_NAME = 'ssd_mobilenet_v1_coco_11_06_2017'
    MODEL_FILE = MODEL_NAME + '.tar.gz'
    DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

    #Path to frozen detection graph. This is the actual model that is used for the object detection.
    PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

    #List of the strings that is used to add correct label for each box.
    PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')

    NUM_CLASSES = 90

    #Download Model
    if os.path.exists(MODEL_FILE):
      print "-----dosya buldu----"
    else :
      print "-----dosya indiriliyor----"
      opener = urllib.request.URLopener()
      opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)

    tar_file = tarfile.open(MODEL_FILE)
    for file in tar_file.getmembers():
      file_name = os.path.basename(file.name)
      if 'frozen_inference_graph.pb' in file_name:
        tar_file.extract(file, os.getcwd())

    #Load a (frozen) Tensorflow model into memory.
    detection_graph = tf.Graph()
    with detection_graph.as_default():
      od_graph_def = tf.GraphDef()
      with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    #Loading label map
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    #Helper code
    def load_image_into_numpy_array(image):
      (im_width, im_height) = image.size
      return np.array(image.getdata()).reshape(
          (im_height, im_width, 3)).astype(np.uint8)

    #Detection
    PATH_TO_TEST_IMAGES_DIR = 'test_images'
    TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image{}.jpg'.format(i)) for i in range(1, 3) ]

    #Size, in inches, of the output images.
    IMAGE_SIZE = (12, 8)

    with detection_graph.as_default():
      with tf.Session(graph=detection_graph) as sess:
        while True:
          ret, image_np = cap.read()
          # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
          image_np_expanded = np.expand_dims(image_np, axis=0)
          image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
          # Each box represents a part of the image where a particular object was detected.
          boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
          # Each score represent how level of confidence for each of the objects.
          # Score is shown on the result image, together with the class label.
          scores = detection_graph.get_tensor_by_name('detection_scores:0')
          classes = detection_graph.get_tensor_by_name('detection_classes:0')
          num_detections = detection_graph.get_tensor_by_name('num_detections:0')
          # Actual detection.
          (boxes, scores, classes, num_detections) = sess.run(
              [boxes, scores, classes, num_detections],
              feed_dict={image_tensor: image_np_expanded})
          # Visualization of the results of a detection.
          vis_util.visualize_boxes_and_labels_on_image_array(
              image_np,
              np.squeeze(boxes),
              np.squeeze(classes).astype(np.int32),
              np.squeeze(scores),
              category_index,
              use_normalized_coordinates=True,
              line_thickness=8)

          cv2.imshow('object detection', image_np) 
          if cv2.waitKey(25) & 0xFF == 27:
            cv2.destroyAllWindows()
            break

oluşturduğumuz kodu çalıştırmak için;

       python object_detection_tutorial.py 
       
       

    
