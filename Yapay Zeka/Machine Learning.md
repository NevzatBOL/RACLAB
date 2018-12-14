# MAKİNE ÖĞRENMESİ
Makine öğrenmesi esas olarak 1959 yılında bilgisayar biliminin yapay zekada sayısal öğrenme ve model tanıma çalışmalarından geliştirilmiş bir alt dalıdır. Makine öğrenimi, bilgisayarların algılayıcı verisi ya da veritabanları gibi veri türlerinedayalı öğrenimini olanaklı kılan algoritmaların tasarım ve geliştirme süreçlerini konu edinen bir bilim dalıdır.Makine öğreniminde araştırmalarının odaklandığı konu bilgisayarlara karmaşık örüntüleri algılama ve veriye dayalı akılcı kararlar verebilme becerisi kazandırmaktır. Bu tür algoritmalar statik program talimatlarını harfiyen takip etmek yerine örnek girişlerden veri tabanlı tahminleri ve kararları gerçekleştirebilmek amacıyla bir model inşa ederek çalışırlar.Makine öğrenimi istatistik, olasılık kuramı, veri madenciliği, örüntü tanıma, yapay zekâ, uyarlamalı denetim ve kuramsal bilgisayar bilimi gibi alanlarla yakından bağlantılıdır.
	
	
## ÖĞRENME YAKLAŞIMLARI
### Denetimli(Supervised) Öğrenme:
Veri,etkiye tepki prensibiyle çalısan sistemlerden alınır ve giris-çıkıs düzeninde organize edilir.
### Denetimsiz(Unsupervised) Öğrenme:
Sınıf bilgisi olmayan veya verilmeyen veri içerisindeki grupları kesfetmeyi hedefler.
### Yarı Denetimli Öğrenme:
Bu kavram tam olarak yukarıdaki iki kavramın arasında yer alır ve etiketlenmemiş büyük miktarda bir veri ile etiketlenmiş küçük miktarda bir verinin beraber kullanılmasıdır.
### Takviyeli Öğrenme:
Öğreticinin, sistemin ürettiği sonuç için doğru ya da yanlış olarak bir değerlendirmesidir.
### Yoğun Öğrenme:
Hiyerarşik öğrenme olarak da bilinir. Bu öğrenme yöntemi derin grafiklerde birçok doğrusal ve doğrusal olmayan dönüşümlerden ve çoklu işlem katmanlarından oluşturulmuş verilerde, üst düzey soyutlamalar kullanılarak elde edilen model girişimlerine dayalı bir dizi algoritmalarla geliştirilmiş makine öğrenmesidir.
  
  
![Denetimli ve Denetimsiz öğrenme alt sınıfları](https://github.com/raclab/RACLAB/blob/master/images/AI/machinelearningalgorithm.jpeg)

## Terimler

### Underfitting (tam uyumsuzluk)
Veri setinin istenilen tahmini yapamaması durumudur.
### Overfitting  (aşırı uyumluluk)
Veri setinin tahmin yerini tamamen doğru sonucları vermesi durumudur.

![overfitting and underfitting](https://github.com/raclab/RACLAB/blob/master/images/AI/underfitting.png)

## Linear(Doğrusal) Regresyon
Elimizde bulunun tüm verilerin bir grafik üzerine oturtulup, doğrusal çizgi çizilmesi ve tahmin yapılması işlemidir.
Çizgi çizilirken ilk önce rastgele bir noktadan çizilir ve elimizde bulunan verilere olan uzakları hesaplanır. Hesaplanan bu uzaklıklar bizim hata değerimiz olur ve hatayı en aza indirecek şekilde doğrumuzun konumunun yeri değiştirilir.
Hatanın doğrunun her konumuna göre hesaplanması ve hatayı azaltacak şekilde yerinin değiştirilmesi işlemine  **Gradient Descent(kademeli düşürme)** adı verilir. Genellikle bu işlem en küçük kareler yöntemi kullanılarak yapılmaktadır.
![Doğrusal Regresyon](https://github.com/raclab/RACLAB/blob/master/images/AI/linearregression.png)

![maliyet fonksiyonu](https://github.com/raclab/RACLAB/blob/master/images/AI/maliyetfonksiyonu.png)

Yukarıda bulunan fonksiyon lineer regresyon için hata hesaplamasında kullanılan maliyet fonksiyonudur. Tüm veriler için gerçek değer(y) eksi tahmini değerin(f(x)) kareleri alınıp ikiye bölünerek hesaplanır.

### Numpy Kütüphanesi ile Linear Regresyon Örneği

	import numpy as np
	import pandas as pd #csv dosyasi okumak icin gerekli kutuphane
	import matplotlib.pyplot as plt
	data = pd.read_csv("linear.csv")  # Verimizi okuyalim
	print(data) # Veriyi inceleyelim.
	x = data["metrekare"] # Metrekareleri bir axis' e cekelim, panda nin ozelligi.
	y = data["fiyat"] 
	print(x)
	print(y) # Ne olusturdugumuza bakmak onemli.
	plt.scatter(x,y) # verileri 2 boyutlu grafik uzerine yerlestirir
	#Dogrumuzun denklemi y = m*a+b , Biz ise en uygun m ve b yi ariyoruz. m Egim, b kesim noktasi
	m,b = np.polyfit(x,y,1)# NumPy bizim icin grafige oturtuyor cizgimizi.
	# np.polyfit(x ekseni, y ekseni, kacinci dereceden polinom denklemi) 
	#lineer regresyonda birinci dereceden kullanacagiz.
	a = np.arange(150) # Denklemimiz hazir. a nin araligini ayarlayalim.
	plt.scatter(x,y) # Scatter ile nokta cizdirimi yapiyoruz.
	plt.plot(m*a+b) 
	z = int(input("Kac metrekare?"))
	tahmin = m*z+b
	print(tahmin)	#tahmin edilen degeri yazdirdik
	plt.scatter(z,tahmin,c="red",marker=">")  #tahmin degerini kirmizi nokta ile gosterir
	plt.show()
	print("m=",m,"b+",b) #y=mx+b dogrusunun hesaplanan m ve b katsayilari

### Sk-Learn Kütüphanesi ile Linear Regresyon Örneği

	import numpy as np
	import pandas as pd
	from sklearn.linear_model import LinearRegression as lr
	import matplotlib.pyplot as plt
	data = pd.read_csv("linear.csv")
	x = data["metrekare"]
	y = data["fiyat"]
	x = x.reshape(99,1) #matris boyutumuzu belirttik
	y = y.reshape(99,1) #matris boyutumuzu belirttik
	lineerregresyon = lr() # Lineer Regresyonu cagirdik.
	lineerregresyon.fit(x,y) # Verilerimizi x ve y eksenine oturttuk.
	lineerregresyon.predict(x) #x'e gore, yani metrekareye gore ev fiyatlarini tahmin edecegiz.
	m = lineerregresyon.coef_ 
	# Coefficient - yani katsayi, bu komutla egimimizi Yani m i buluyoruz.
	b= lineerregresyon.intercept_
	# Intercept - b dir. yani y = mx+b 'de x'e sifir verdigimizde kalan deger.
	a = np.arange(150)
	plt.scatter(x,y) # Gercek verilerimizi nokta nokta, scatter ile cizdiriyoruz.
	plt.scatter(a,m*a+b, c="red",marker=">") # dogrumuzu kirmizi noktalar ile ciziyor
	plt.show()
	print('Egim: ', lineerregresyon.coef_)
	print('Y de kesistigi yer: ', lineerregresyon.intercept_)
	print("Denklem")
	print("m=",m,"b+",b) # y=mx+b dogrusunun katsayilari
	
linear.csv dosyasını https://drive.google.com/open?id=1mDpK7w5JQJ_9Qhk5u5jinO9lRFf76lTs adresinde indirebilirsiniz

### Lasso Regresyon
Lineer regresyonda hesaplanan maliyet fonksiyonuna gerçek değer eksi tahmini değerlerimizin mutlak değerlerinin toplamının bir alfa aşırı parametresi ile çarpılmış fonksiyonun eklenmesiyle bulunur.
### Ridge Regresyon
Lineer regresyonda hesaplanan maliyet fonksiyonuna gerçek değer eksi tahmini değerlerimizin karelerinin toplamının bir alfa aşırı parametresi ile çarpılmış fonksiyonun eklenmesiyle bulunur.

## Polynominal(Polinom) Regresyon

Verilerin bir grafik üzerinde doğrusal bir şekilde dağılmadığı durumlarda tahmin yapabilmemizi sağlanayan bir yöntemdir. Tahmin derecesi ve denklemi belirli olan bir eğriye bakılarak yapılır. Eğrimizin derecesini belirlerken çok düşük dereceler kullanmak **Underfitting (tam uyumsuzluk)** problemine, çok yüksek dereceler kullanmak ise **Overfitting  (aşırı uyumluluk)** problemine neden olur. 

![Polinom Regresyon](https://github.com/raclab/RACLAB/blob/master/images/AI/polinomregresyon.png)

### Numpy Kütüphanesi ile Polinom Regresyon Örneği

	import numpy as np
	import pandas as pd #csv dosyasi okumak icin gerekli kutuphane
	import matplotlib.pyplot as plt
	data = pd.read_csv("linear.csv")  # Verimizi okuyalim
	print(data) # Veriyi inceleyelim.
	x = data["metrekare"] # Metrekareleri bir axis' e cekelim, panda nin ozelligi.
	y = data["fiyat"] 
	print(x)
	print(y) # Ne olusturdugumuza bakmak onemli.
	plt.scatter(x,y) # verileri 2 boyutlu grafik uzerine yerlestirir
	#Dogrumuzun denklemi y = m*a+b , Biz ise en uygun m ve b yi ariyoruz. m Egim, b kesim noktasi
	a, b, c, d = np.polyfit(x,y,3)# NumPy bizim icin grafige oturtuyor cizgimizi.
	#derecemiz arti bir tane degiskene np.polyfit() fonksiyonunun degerini gonderdik.
	# np.polyfit(x ekseni, y ekseni, kacinci dereceden polinom denklemi) 
	#lineer regresyonda birinci dereceden kullanacagiz.
	z = np.arange(150) # Denklemimiz hazir. z nin araligini ayarlayalim.
	plt.scatter(x,y) # Scatter ile nokta cizdirimi yapiyoruz.
	plt.plot(z,a*z*z*z+b*z*z+c*z+d)
	#bir eksene aralik bir eksene 3. derece icin denkelemi yazdirdik y=ax^3+bx^2+cx+d 
	plt.show()
	print(a,"x^3+",b,"x^2+",c,"x+",d) #dogrunun hesaplanan a b c d katsayilari

## Logistics (Lojistik) Regresyon

Lojistik regresyon cevap değişkeninin kategorik olarak ikili ve çoklu kategorilerde gözlendiği durumlarda açıklayıcı değişkenlerle sebep-sonuç ilişkisini belirlemede kullanılan bir yöntemdir.

![Lojistik Regresyon](https://github.com/raclab/RACLAB/blob/master/images/AI/logiscticregression.jpeg)

Yukarıdaki resimde doğru ve yanlış olan veriler lojistik regresyon yöntemi ile sınıflandırılmıştır.

## K-Nearest Neighbor (K- En Yakın Komşular) Algoritması ile Sınıflandırma

Elimizde olan ve hangi sınıftan olduğunu bildiğimiz verileri kullanarak yeni gelen ve sınıfı belirli olmayan verilerin sınıflarını tahmin etmek için kullanılan bir yöntemdir. Sınıfı belirli olan ve sınıfı tahmin edilecek olan verilerimizi grafik üzerine yerleştirilir. Tahmin edilecek noktaya en yakın K sayısı kadar noktaya olan uzaklıkları öklit bağıntısı ile hesaplanır. En yakın K adet noktalarda hangi sınıf fazla ise yeni gelen verimizin sınıfı o kabul edilir. K sayısı belirlerken sonuçta 2 sınıfın sayıları eşit çıkmayacak şekilde belirlenmesi gerekmektedir. Örneğin iki sınıfımız varsa belirlenen noktaların sayıları eşit çıkabileceğinden dolayı K değerimize çift bir değer yerine tek bir değer vermemiz gerekir. K'nin en çok kullanılan değerleri 3 ile 10 arasındadır.

![KNN](https://github.com/raclab/RACLAB/blob/master/images/AI/knn.gif)
