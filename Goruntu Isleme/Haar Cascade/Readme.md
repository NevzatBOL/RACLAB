# Haar Cascade

Haar Cascade kullanımı aşağıda anlatılmaktadır. Kullanım örenkleri ise car detection ve pencil detection dosyalarında bulunmaktadır.

* 1. Negative ve positive klasörü oluşturulur.
* 2. Positive dosyası içerisine sınıflandırma yapmak istediğimiz resimleri koyarız.
* 3. Negative dosyası içerisine sınıflandırma yapamak istediğimiz resimlerden farklı resimler koyarız. Nekadar çok ve farklı tür resim olursa başarı artar.
* 4. Resimler aynı boyutta olmalıdır. Eğitimin hızlı yapılabilmesi için resimlerin boyutu küçük tutulur.
* 5. Negative dosyası içerisindeki resimler bg.txt ismi ile dosya uzantıları kaydedilir.
* 6. Positive dosyası içerisindeki resimler info.lst ismi ile dosya uzantıları ve resimin bulunduğu karenin konumları kaydedilir.
* 6. **info.lst: file_name/img_name.jpj n x y w h**   :n=resimdeki çerçeve sayısı
* 7. data klasörü uluşturulur.
* 8. opencv_createsamples -info info_name -num Positive_resim_sayisi -w nesnenin_genişliği -h nesnenin_yüksekliği  
* 8. İlk olarak positive resimleri vec dosyası haline getiririz.
* 8. **opencv_createsamples -info info.lst -num 11 -w 20 -h 20 -vec positives.vec**
* 8. oluşturduğumuz .vec dosyasını incelemek için aşağıdaki kullanılır.
* 9. **opencv_createsamples -vec positives.vec -w 20 -h 20**
* 10. Datayı train etmek için aşağıdaki komut kullanılır.
* 10. **opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 11 -numNeg 11 -numStages 10 -w 20 -h 20**
* 10. opencv_traincascade -data Eğitim_parametrelerinin_kaydedileceği_dosya -vec vec_dosyası -bg negative_file -numPos positive_resim_sayısı -numNEg negative_resim_sayısı -numStages Eğitim_işleminin_kaç_defa_tekrarlanacağı -w nesnenin_genişliği -h nesnenin_yüksekliği 
* 10. numPose ve numNeg aynı sayıda olmalıdır. (farklı olursa eğitim sırasında hatalı parametre uyarısı veriyor.) 
* 11. cascade.xml dosyası data klasörü içerisinde oluşturulur.
* 12. Eğitilen cascade parametreleri ile detectMultiScale uygulanabilir.
