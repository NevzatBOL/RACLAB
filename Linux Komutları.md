# Linux Komutları

## Dosya İşlemleri

    pwd 				bulunduğumuz dizini gösterir.	
    ls				bulunduğumuz dizindeki dosyları ve klasörleri listeler.
    ls -l				bulunduğumuz dizindeki dosyları ve klasörleri özellikleri ile birlikte listeler.
    ls -a				bulunduğumuz dizindeki gizli dosya ve klasörleri listeler.
    cd				dizinler arası geçişi sağlar.
    cd .. 				bir üst dizine çıkar.
    cd ~				varsayılan dizine gider.
    cd dizin			girilen dizine gider.

    mkdir klasor			bulunduğumuz dizinde klasör oluşturur.
    mkdir -p a/b			bulunduğumuz dizinde iç içe a ve b klasörlerini oluşturur.
    mkdir -p a/b && touch a/a.txt 	bulunduğumuz dizinde iç içe klasör oluşturur ve a klasörü içine a.txt dosyasını oluşturur.
    mkdir touch a/b/b.txt		a klasörü içindeki b klasörü içine b.txt dosyasını oluşturur. 
    cp dosya klasor 		dosyayı klasor dizinine kopyalar.
    mv dosya klasor 		dosyayı klasor dizinine taşır.
    rm dosya			dosyayı siler.
    rm -r klasor			klasörü siler.	

    touch dosya.txt			bulunduğumuz dizinde dosya oluşturur.
    nano dosya.txt			dosyamızın içerisinde değişiklik yapabiliriz.
    cat dosya.txt			dosyamızın içerisini okur.
    tail -n satır_sayısı dosya.txt	dosyanın sondan satır_sayısı kadar satırını gösterir.
    head -n satır_sayısı dosya.txt	dosyanın başından satır_sayısı kadar satırını gösterir.
    rev dosya.txt			dosyayı tersten okur.
    more dosya.txt			dosyayı düz okur.
    tac dosya.txt			dosyayının sonundan okur.	

    gpg -c dosya.txt		dosyayı şifreler
    gpg -o yeni.txt dosya.txt.gpg	şifreli dosyayı yeni.txt dosyasına çıkartır.
