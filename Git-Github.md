# Git Kurulumu

Windows için https://git-scm.com/download/win git indirilerek kurulur.

Linux için *sudo apt-get install git*

# Git Kullanımı
  
    git config --global user.name "kullanıcı adı"
    git config --global urer.email "mail"
    
    git init    -Çalışma dizinimizi git deposu haline getirir.
    
    git add .   -Çalışma dizinindeki tüm dosyalarda yapılan değişiklikleri geçiş bölgesine alır.
    git commint -m "Değişiklik tanımı"  -yapılan değişiklikleri değişiklik tanımı ile birlikte git deposuna ekler.
    
    git add dosya_adı -dosya_adı dosyasınındaki değişiklikleri geçiş bölgesine alır.
    
    git log   -log kayıtlarını (Düzenleme kayıtları) listeler.
    
    git status    -Değişiklik yapılan dosya varmı kontrol eder.
                  -yeşil dosyalar, geçiş bölgesindeki doslardır.
                  -kırmızı dosyalar, geçiş bölgesine alınmamış dosyalardır.
    
    git diff  -Dosyalarda yapılan değişiklikler incelenebilir.
    git diff --staged   -geçiş bölgesi ile git deposu arasındaki değişiklikleri gösterir.
    
    git rm dosya_adı   -dosyayı siler.
    git rm -r klasör_adı  -klasör siler.
    git commint -m "mesaj" -Silme işlemi git deposuna kaydedilir.

    git mv dosya_adı yeni_ad  -dosyanın ismini değiştirir.
    git mv dosya_adı  klasör_adı  -dosyayı klasöre taşır.
    git commint -m "mesaj" -isim değiştirme ve taşıma işlemini git deposuna kaydeder.
    
# GitHub Kullanımı

ilk olarak github.com üyelik açılır.

