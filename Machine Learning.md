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

## Linear(Doğrusal) Regresyon
Elimizde bulunun tüm verilerin bir grafik üzerine oturtulup, doğrusal çizgi çizilmesi ve tahmin yapılması işlemidir.
Çizgi çizilirken ilk önce rastgele bir noktadan çizilir ve elimizde bulunan verilere olan uzakları hesaplanır. Hesaplanan bu uzaklıklar bizim hata değerimiz olur ve hatayı en aza indirecek şekilde doğrumuzun konumunun yeri değiştirilir.
Hatanın doğrunun her konumuna göre hesaplanması ve hatayı azaltacak şekilde yerinin değiştirilmesi işlemine  **Gradient Descent(kademeli düşürme)** adı verilir. Genellikle bu işlem en küçük kareler kullanılarak yapılmaktadır.
![Doğrusal Regresyon](https://mertricks.files.wordpress.com/2015/06/18.png)

## Polynominal(Polinom) Regresyon
![Polinom Regresyon](https://www.google.com.tr/search?biw=1309&bih=604&tbm=isch&sa=1&ei=mtRpWqmtM4XVwQKs-qGoDQ&q=polinom+regresyon&oq=polinom+regresyon&gs_l=psy-ab.3..0i24k1l3.684573.687605.0.687812.17.10.0.7.7.0.189.1177.0j9.9.0....0...1c.1.64.psy-ab..1.16.1201...0j0i67k1.0.cYLuzlkgJDM#imgrc=_64KNAnmUTSsSM:)









