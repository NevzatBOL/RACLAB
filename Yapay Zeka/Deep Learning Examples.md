# Tensorflow ile Object Detection
## Hazır Api Çalıştırma

ilk olarak bir çalışma dizini oluşturalım ve tensorflow'un model paketini indirelim.

    mkdir object_detection
    cd object_detection
    git clone https://github.com/tensorflow/models.git

Linux için protoc-3.6.0-linux-x86_64.zip'u [indirelim.](https://github.com/google/protobuf/releases) indirdiğimiz dosyanın içerisinde bin klasörünün içinde yer alan protoc dosyasını /usr/local/bin/ klasörüne atalım ve protoc dosyasını çalıştırılabilir yapalım.

    sudo cp protoc ~ /usr/local/bin/
    sudo chmod 777 protoc
    
Oluşturduğumuz object_detection klasörü içerisinde yer alan models/research klasörüne gidelim.

    cd ~/object_detection/models/research
  
    protoc object_detection/protos/*.proto --python_out=.
    export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
    
İlk örneğimizi çalıştıralım. Bunun için ilk olarak models/research/object_detection klasörüne gidelim ve jupyter ile object_detection_tutorial.ipynb çalıştıralım.

    cd ~/object_detection/models/research/object_detection
    jupyter-notebook object_detection_tutorial.ipynb

    kernel -> Restart & Run All ile tüm kodları çalıştıralım.
    
Kod her çalıştığında model dosyasını yeniden indirecektir. Model dosyasının yeniden inmesini önlemek için Download Model'in altında yer alan aşağıdaki satırları yorum satırı yapabilirsiniz.

    #opener = urllib.request.URLopener()
    #opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)

Gerçek zamanlı olarak kameradan alınan anlık görüntü ile örneğimizi çalıştıralım. Bunun için hazır dataset ve model üzerinden çalışan jupyter ile test ettiğimiz kodları aşağıdaki gibi düzenlerek çalıştıralım.

    cd ~/object_detection/models/research/object_detection

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
       
## Kendi Dataset'imiz ile object detection

Kendi datasetimizi oluşturmak için ilk olarak labelImg programını indirelim.

    cd ~/object_detection
    git clone https://github.com/tzutalin/labelImg.git
  
indirdiğimiz labelImg için gerekli olan paket kurulumlarını yapalım.

    sudo apt-get install pyqt5-dev-tools
    sudo pip3 install lxml
    cd ~/object_detection/labelImg/
    make qt5py3

Datasetimizi oluşturmak için öncelikle train ve test klasörleri oluşturalım. oluşturduğumuz bu klasöre labelImg i kullanarak etiketlediğimiz resimleri xml olarak kaydedeceğiz. Etiketlemede kullanacağımız resimlerin images isminde bir klasörde olmasına ve train klasörü ile aynı dizinde olmasına dikkat edelim.

     cd ~/object_detection/
     mkdir datasets
     cd datasets
     mkdir train
     mkdir test
    
Datasetimizi labelImg'i kullanarak oluşturabiliriz. Resimlerin bulunduğu images dizinini Open Dir ile açalım. Her resim için resimde algılanmasını istediğimiz nesneyi Create RectBox ile seçelim, etiketleyelim ve kaydedelim. her resim için ayrı ayrı xml dosyası oluşturulacaktır.

    python3 labelImg.py

Oluşturduğumuz xml dosyalarını csv formatına dönüştürmeliyiz bunun için aşağıdaki kodları kullanalım.

    cd ~/object_detection/datasets/
    mkdir data
    
    gedit xml_to_csv.py
    
    import os
    import glob
    import pandas as pd
    import xml.etree.ElementTree as ET

    def xml_to_csv(path):
        xml_list = []
        for xml_file in glob.glob(path + '/*.xml'):
            tree = ET.parse(xml_file)
            root = tree.getroot()
            for member in root.findall('object'):
                value = (root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[4][0].text),
                         int(member[4][1].text),
                         int(member[4][2].text),
                         int(member[4][3].text)
                         )
                xml_list.append(value)
        column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
        xml_df = pd.DataFrame(xml_list, columns=column_name)
        return xml_df


    def main():
        for directory in ['train','test']:
            image_path = os.path.join(os.getcwd(), 'images/{}'.format(directory))
            xml_df = xml_to_csv(image_path)
            xml_df.to_csv('data/{}_labels.csv'.format(directory), index=None)
            print('Successfully converted xml to csv.')

    main()

oluşturduğumuz kodu çalıştırarak train ve test klasöründe yer alan xml dosyalarını data klasörü içerisine train_labels.csv ve test_labels.csv olarak kaydedelim.

    python3 xml_to_csv.py
    
Daha önce indirmiş olduğumuz tensorflow'un models paketi içerisinde yer alan object_detection kütüphanesini kuralım.

    cd ~/object_detection/models/research
    
    sudo python3 setup.py install
    
Oluşturduğumuz csv dosyalarını record dosyasına dönüştürmek için aşağıdaki kodları kullanalım.

    cd ~/object_detection/datasets/
    
    gedit generate_tfrecord.py 

    """
    Usage:
      # From tensorflow/models/
      # Create train data:
      python3 generate_tfrecord.py --csv_input=data/train_labels.csv  --output_path=data/train.record

      # Create test data:
      python3 generate_tfrecord.py --csv_input=data/test_labels.csv  --output_path=data/test.record
    """
    from __future__ import division
    from __future__ import print_function
    from __future__ import absolute_import

    import os
    import io
    import pandas as pd
    import tensorflow as tf

    from PIL import Image
    from object_detection.utils import dataset_util
    from collections import namedtuple, OrderedDict

    flags = tf.app.flags
    flags.DEFINE_string('csv_input','','Path to the CSV input')
    flags.DEFINE_string('output_path','','Path to output TFRecord')
    FLAGS = flags.FLAGS


    # TO-DO replace this with label map
    def class_text_to_int(row_label):
        if row_label == 'light':
            return 1
        else:
            None


    def split(df, group):
        data = namedtuple('data', ['filename', 'object'])
        gb = df.groupby(group)
        return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]


    def create_tf_example(group, path):
        with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
            encoded_jpg = fid.read()
        encoded_jpg_io = io.BytesIO(encoded_jpg)
        image = Image.open(encoded_jpg_io)
        width, height = image.size

        filename = group.filename.encode('utf8')
        image_format = b'jpg'
        xmins = []
        xmaxs = []
        ymins = []
        ymaxs = []
        classes_text = []
        classes = []

        for index, row in group.object.iterrows():
            xmins.append(row['xmin'] / width)
            xmaxs.append(row['xmax'] / width)
            ymins.append(row['ymin'] / height)
            ymaxs.append(row['ymax'] / height)
            classes_text.append(row['class'].encode('utf8'))
            classes.append(class_text_to_int(row['class']))

        tf_example = tf.train.Example(features=tf.train.Features(feature={
            'image/height': dataset_util.int64_feature(height),
            'image/width': dataset_util.int64_feature(width),
            'image/filename': dataset_util.bytes_feature(filename),
            'image/source_id': dataset_util.bytes_feature(filename),
            'image/encoded': dataset_util.bytes_feature(encoded_jpg),
            'image/format': dataset_util.bytes_feature(image_format),
            'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
            'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
            'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
            'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
            'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
            'image/object/class/label': dataset_util.int64_list_feature(classes),
        }))
        return tf_example


    def main(_):
        writer = tf.python_io.TFRecordWriter(FLAGS.output_path)
        path = os.path.join(os.getcwd(), 'images')
        examples = pd.read_csv(FLAGS.csv_input)
        grouped = split(examples, 'filename')
        for group in grouped:
            tf_example = create_tf_example(group, path)
            writer.write(tf_example.SerializeToString())

        writer.close()
        output_path = os.path.join(os.getcwd(), FLAGS.output_path)
        print('Successfully created the TFRecords: {}'.format(output_path))


    if __name__ == '__main__':
        tf.app.run()
        
oluşturduğumuz kodu çalıştırarak train_labels.csv ve test_labels.csv dosyalarını data klasörü içerisine train.record ve test.record olarak kaydedelim.

      # Create train data:
      python3 generate_tfrecord.py --csv_input=data/train_labels.csv  --output_path=data/train.record

      # Create test data:
      python3 generate_tfrecord.py --csv_input=data/test_labels.csv  --output_path=data/test.record
      
Artık Modelimizi eğitmeye başlayabiliriz.      
