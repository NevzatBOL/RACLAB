# Git Kurulumu

Windows için https://git-scm.com/download/win git indirilerek kurulur.

Linux için *sudo apt-get install git*

# Git Kullanımı
  
    git config --global user.name "kullanıcı adı"
    git config --global urer.email "mail"
    
    git init    -Çalışma dizinimizi git deposu haline getirir.
    
    git add .   -Çalışma dizinindeki tüm dosyalarda yapılan değişiklikleri geçiş bölgesine alır.
    git commit -m "Değişiklik tanımı"  -yapılan değişiklikleri değişiklik tanımı ile birlikte git deposuna ekler.
    
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
     
    .gitignore    -git'in takip etmesini istemediğimiz dosyaların isimlerini buraya ekleriz.
    
# GitHub Kullanımı

ilk olarak github.com üyelik açılır.

Create a new repository ile yeni çalışma alanı oluşturulur. 

git çalışma alanımızı github'a yükleyelim.
Öncelikle github'a yükleyeceğimiz klasörün dizinine terminalden gidelim.

    git remote add githubRepo https://github.com/....     -oluşturduğunuz repostory linkinizi yazın.
    git push -u githubRepo master   -githubta oluşturduğunuz çalışma alanına bilgisayardaki repostory mizi yükledik.
    
    -master ana koldur başka bir branch(dal) üzerine eklemek isterseniz aynı yere o branchin ismini yazmanız yeterli.
 
 Bazı Terimler;
 
 public repostory herkese açık çalışma alanı.
 
 private repostory sadece erişim izni olanlar göre bilir.
 
 watch  bir projeyi takip etmek için kullanılır.
 
 start  bir projeyi beğenmek için kullanılır.
 
 fork   projeyi kendi hesabınıza ekler bu sayede kendi hesabınız altında proje üzerinde değişiklik yapabilirsiniz.
 
 issues projede karşılaşılan sorunların diğer insanlara sorulduğu ve çözüldüğü alandır.
 
 ## Branches (Dallar)   
 
    git pull    -github dosyalarını bilgisayara çeker.
    git branch  -projenin dallarını listeler.
    git branch --all -uzak bilgisayardaki dalları listeler.
    
    git branch yeni_dal_ismi  -yeni dal oluşturur.
    git checkout yandal   -yandala geçer.
    
    git diff master yandal  -master ile yandal arasındaki değişiklikleri listeler.
    git merge yandal  -yandalı master ile birleştirir.
    
 ## md dosyaları oluşturma
 
    # Başlık oluşturmada kullanılır.
    ## sayısı artırılarak alt başlık eklenebilir.
    
### Başlık
#### Alt başlık 1
#### Alt başlık 2
    
    ** Kalın yazı için kullanılır. **
    
**kalın yazı**

    * italik yazı için kullanılır. *
    
*italik yazı*

    satır arası`kod eklemek için` kullanılır.

Satır arası `kod` eklenir.

kod bloğu eklemek için

    ```python
    print "kod"
    print "blogu"
    ```
```python
print "kod"
print "blogu"
```
      
    [link ismi](link(https...)) -link eklemek için kullanılır
    
[Markdown](https://guides.github.com/features/mastering-markdown/)    
    
    ![resim ismi](resim linki) -resim eklemek için kullanılır.

![image](https://www.gettyimages.ca/gi-resources/images/Homepage/Hero/UK/CMS_Creative_164657191_Kingfisher.jpg)

Tablo oluşturma

    İlk Başlık | İkinci Başlık
    ------------ | -------------
    Hücre 1'den gelen içerik | 2. hücreden gelen içerik
    İlk sütundaki içerik | İkinci sütundaki içerik
    
İlk Başlık | İkinci Başlık
------------ | -------------
Hücre 1'den gelen içerik | 2. hücreden gelen içerik
İlk sütundaki içerik | İkinci sütundaki içerik    

**Referans Link:** [git-github eğitim videoları](https://www.youtube.com/watch?v=rWG70T7fePg&list=PLPrHLaayVkhnNstGIzQcxxnj6VYvsHBHy)
