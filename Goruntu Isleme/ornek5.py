#-*-coding: cp1254-*-
###Renk Kümeleme###

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2

def centroid_histogram(clt):
	numlabels=np.arange(0,len(np.unique(clt.labels_))+1)	
	hist,_=np.histogram(clt.labels_,bins=numlabels)

	hist=hist.astype("float")
	hist/=hist.sum()

	return hist
def plot_colors(hist,centroids):
	bar=np.zeros((50,300,3),dtype="uint8")
	startx=0
	for (percent,color) in zip(hist,centroids):
		endx=startx+percent*300
		cv2.rectangle(bar,(int(startx),0),(int(endx),50),color.astype("uint8").tolist(),-1)
		startx=endx
	return bar

img=cv2.imread('resimler/kelebek.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.figure()
plt.axis("off")
plt.imshow(img)

img=img.reshape((img.shape[0]*img.shape[1],3))

clt=KMeans(n_clusters=2) #kaç küme oluşturacağı girilir. küme sayısı artıkça hassasiyet artar ama hız azalır.
clt.fit(img)

hist=centroid_histogram(clt)
bar=plot_colors(hist,clt.cluster_centers_)

plt.figure()
plt.axis("off")
plt.imshow(bar)

plt.show()
