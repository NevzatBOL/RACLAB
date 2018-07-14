import numpy as np

girdi=np.array([[0,0,1],[1,1,1],[1,0,1]])

gerceksonuc=np.array([[0,1,1]]).T 
W=np.array([[1.0,1.0,1.0]]).T #agirlik degerleri

for i in range(100):
	hucredegeri=np.dot(girdi,W) #skaler carpim
	tahmin=1/(1+np.exp(-hucredegeri)) #aktivasyon fonksiyonu sigmoid
	W=W+np.dot(girdi.T,((gerceksonuc-tahmin)*tahmin*(1-tahmin)))
	print np.mean(gerceksonuc-tahmin)

print 1/(1+np.exp(-(np.dot(np.array([1,0,0]),W))))
