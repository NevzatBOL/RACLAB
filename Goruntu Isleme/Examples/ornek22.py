#-*-coding: utf-8-*-
###Object Detection And Classification - Paralel Proglamlama###

import numpy as np
import cv2
from multiprocessing import Process
from multiprocessing import Queue

def classify_frame(net,inputqueue, outputqueue):
	while(1):
		#giriş sırasında çerçeve olup olmadığını kontrol eder.
		if not inputqueue.empty():
			frame=inputqueue.get()
			frame=cv2.resize(frame,(300,300))
			blob=cv2.dnn.blobFromImage(frame,0.007843,(300,300),127.5)
			#blob'u deep learning'e giriş olarak ayarlar.
			net.setInput(blob)
			detections=net.forward()

			#algılamaları çıktı sırasına yazar.
			outputqueue.put(detections)

#modelnetssd'nin eğitildiği sınıf etikeleri.
classes=["ArkaPlan","ucak", "bisiklet", "kus", "bot","sise","otobus","araba", "...", "sandalye", "...", "yemekTablasi", "...","...","motosiklet", "insan", "saksibitkisi","...","kanepe", "tren", "tvmonitor"]
#her sınıf etiketi için bir renk oluşturulur.
colors=np.random.uniform(0,255,size=(len(classes),3))

#Modelimizi yükledik.
net=cv2.dnn.readNetFromCaffe("DataSet/MobileNetSSD_deploy.prototxt.txt","DataSet/MobileNetSSD_deploy.caffemodel")

#giriş ve çıkış listeleri oluşturuldu.
inputqueue=Queue(maxsize=1)
outputqueue=Queue(maxsize=1)
detections =  None

#parelel işlem processi tanımlandı.
p=Process(target=classify_frame, args=(net,inputqueue,outputqueue,))
p.daemon=True
p.start()

cam=cv2.VideoCapture(0)

while(1):
	ret,frame=cam.read()
	if ret:
		#frame=cv2.resize(frame,(500,400))
		h,w=frame.shape[:2]
	
		if inputqueue.empty():
			inputqueue.put(frame)

		if not outputqueue.empty():
			detections=outputqueue.get()

		if detections is not None:
			for i in np.arange(0,detections.shape[2]):
		
				confidence=detections[0,0,i,2] #tahmin değeri
				if confidence > 0.2:
					#algılanan nesnelerin kordinatları hesaplanır.
					idx=int(detections[0,0,i,1])
					if classes[idx]=="insan":
						box=detections[0,0,i,3:7]*np.array([w,h,w,h])
			
						startx,starty,endx,endy=box.astype("int")
			
						label = "{}: {:.2f}%".format(classes[idx],
							confidence * 100)
	
						cv2.rectangle(frame,(startx,starty),(endx,endy),colors[idx],2)
						y=starty - 15 if starty -15 > 15 else starty + 15
						cv2.putText(frame,label,(startx, y),cv2.FONT_HERSHEY_SIMPLEX,0.5,colors[idx],2)

	
		cv2.imshow("frame",frame)
	if cv2.waitKey(1) & 0xff == 27:
		break

cam.release()
cv2.destroyAllWindows()
