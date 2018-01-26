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
  
  
![Denetimli ve Denetimsiz öğrenme alt sınıfları](http://ahmetcevahircinar.com.tr/wp-content/uploads/2017/05/makine-ogrenmesi-algoritmalari.jpg)

## Terimler

### Underfitting (tam uyumsuzluk)
Veri setinin istenilen tahmini yapamaması durumudur.
### Overfitting  (aşırı uyumluluk)
Veri setinin tahmin yerini tamamen doğru sonucları vermesi durumudur.

![overfitting and underfitting](https://qph.ec.quoracdn.net/main-qimg-b4112b5d856f4f0da349460aeed854d8)

## Linear(Doğrusal) Regresyon
Elimizde bulunun tüm verilerin bir grafik üzerine oturtulup, doğrusal çizgi çizilmesi ve tahmin yapılması işlemidir.
Çizgi çizilirken ilk önce rastgele bir noktadan çizilir ve elimizde bulunan verilere olan uzakları hesaplanır. Hesaplanan bu uzaklıklar bizim hata değerimiz olur ve hatayı en aza indirecek şekilde doğrumuzun konumunun yeri değiştirilir.
Hatanın doğrunun her konumuna göre hesaplanması ve hatayı azaltacak şekilde yerinin değiştirilmesi işlemine  **Gradient Descent(kademeli düşürme)** adı verilir. Genellikle bu işlem en küçük kareler yöntemi kullanılarak yapılmaktadır.
![Doğrusal Regresyon](https://mertricks.files.wordpress.com/2015/06/18.png)

![maliyet fonksiyonu](https://i.hizliresim.com/azMoWR.png)
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
![Polinom Regresyon](http://www.datascience.istanbul/wp-content/uploads/2017/06/Lineer_Regresyon_Notlar%C4%B1_10_Polinom_Regresyon_with_R_Polinom_Model_Grafik.png)

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


	









