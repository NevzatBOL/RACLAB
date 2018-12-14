# Linux Komutları

    man komut			komut hakkında bilgi verir.
    whoami				aktif kullanıcıyı gösterir.
    w				bu gün aktif olmuş tüm kullanıcıları gösterir.
    uname -a			kurulu olan linux serisini gösterir.
    sudo 				bir seferlik admin yetkisi verir.
    sudo -s                     	sürekli admin yetkisi verir.
    sudo su				sürekli tüm sistemde admin yetkisi verir.           	
    top				çalışmakta olan processleri gösterir.
    ps aux				çalışmakta olan bütün sistemi görüntüler.
    ps aux |grep program_adı	programın çalışma bilgilerini verir.
    kill -9 PID			PID'si verilen process'i durdurur.
    history				terminalden daha önce yazılmış tüm komutları listeler.
    sudo -H nautilus		Dosya sisteminde root yetkisi verir.


## Dosya İşlemleri

    pwd 				bulunduğumuz dizini gösterir.	
    ls				bulunduğumuz dizindeki dosyları ve klasörleri listeler.
    ls -l				bulunduğumuz dizindeki dosyları ve klasörleri özellikleri ile birlikte listeler.
    ls -a				bulunduğumuz dizindeki gizli dosya ve klasörleri listeler.
    cd				dizinler arası geçişi sağlar.
    cd .. 				bir üst dizine çıkar.
    cd ~				varsayılan dizine gider.
    cd -				önceki dizine gider.
    cd dizin			girilen dizine gider.

    mkdir klasor			bulunduğumuz dizinde klasör oluşturur.
    mkdir -p a/b			bulunduğumuz dizinde iç içe a ve b klasörlerini oluşturur.
    mkdir -p a/b && touch a/a.txt 	bulunduğumuz dizinde iç içe klasör oluşturur ve a klasörü içine a.txt dosyasını oluşturur.
    mkdir touch a/b/b.txt		a klasörü içindeki b klasörü içine b.txt dosyasını oluşturur. 
    cp dosya klasor 		dosyayı klasor dizinine kopyalar.
    cp -r klasor klasor		klasorü klasor dizinine kopyalar.
    mv dosya klasor 		dosyayı klasor dizinine taşır.
    rm dosya			dosyayı siler.
    rm -rf klasor			klasörü siler.	

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

## Dosya/Program/Paket/Aygıt arama

    find dosya			bulunduğumuz dizinde dosyayı arar.
    find |grep dosya 		tüm dizinlerde dosayı arar.
    which program_adı		programın bulunduğu dizini gösterir.
    whereis program_adı		programın bulunduğu dizini detaylı gösterir.
    
    lspci -v			bilgisayarımıza bağlı olan aygıtları lister.
    lsusb				bilgisayarımıza bağlı olan usb aygıtlarını listeler.
    
    apt-cache depends program_adı	programın ihtiyaç duyduğu paketleri listeler.
    apt-cache search program_adı	paket dosyaları içerisinde programa ait tüm paketleri listeler.
    
    dpkg -l				sistemde kurulu olan tüm paketleri listeler.
    dpkg -S program_adı		programın kurulduğu bütün paketleri listeler.
    dpkg -L program_adı		programın kurduğu bütün paketleri listeler.
    
## Bilgisayar Kapama/Yeniden Başlatma

    sudo shutdown -h now	bilgisarımızı kapatır.
    sudo shutdown -r now	bilgisayarımızı yeniden başlatır.
    sudo shutdown -c	bilgisayarı kapatma veya yeniden başlantma işlemini iptaleder.
    sudo reboot		bilgisayarı yeniden başlatır.
    
## Program Kurma/Kaldırma veya Güncelleme

    sudo apt-get install program_adı	programı kurar
    sudo apt-get purge program_adı		programı tüm yapılandırmaları ile birlikte kaldırır.
    sudo apt-get update			güncelleştirmeleri denetler.
    sudo apt-get upgrade			güncelleştirmeleri yapar.
    
## Kullanıcı Yönetimi
    
    cd /etc				kullanıcıların bulunduğu dosya etc dizininde bulunur.
    cat passwd			kullanıcıların dosyasını okur.
    sudo adduser kullanıcı_adı	yeni kullanıcı ekler.
    sudo passwd kullanıcı_adı	kullanıcının şifresini değiştir.
    su kullanıcı_adı		kullanıcı değiştirebiliriz.
    sudo deluser kullanıcı_adı	kullanıcıyı siler. fakat kullanıcıya ait dosyaları silmez.	
    
## Grup Yönetimi

    cd /etc				grupların bulunduğu dosya etc dizininde bulunur.
    cat group			grup dosyasını okur.
    sudo addgroup grup_adı		yeni grup ekler.
    adduser kullanıcı_adı grup_adı 	gruba yeni kullanıcı ekler.
    chmod 777 dosya			dosya'ya kullanıcı, gurp ve herkes için okuma, yazma ve çalıştırma haklarını tanımlar.		                                1 x(çalıştırma), 2 w(yazma), 4 r(okuma)
					örn: kullanıcı: rwx, grup r-w, herkes --x haklarına sahip olsun; chmod 751(1+2+4)(1+4)(1) dosya
    
    chgrp grup_adı dosya		dosyanın grubunu değiştirir.
    chown kullanıcı_adı dosya	dosyanın kullanıcısını değiştirir.
    
## Ağ Komutları

    ifconfig			ağ ayarlarını gözterir.
    sudo ifconfig ağ down		ağı kapatır.
    sudo ifconfig ağ up		ağı açar.
    sudo dhclient			ip adresini yeniler.
    /etc/init.d/networking restart	network servisini yeniden başlatır.
    
    ping ip/web_sitesi		ip/web_sitesine sürekli küçük veri paketleri gönderir.
    ping -c sayı ip/web_sitesi   	ip/web_sitesi girilen sayı kadar ping atar.
    apt-get install traceroute	ip takipetme paketini yükledik.
    traceroute www.google.com	ip/web_sitesi bağlanmak için getiğimiz ipleri gösterir.	
    
    nslookup
	>server			        bağlı olduğumuz dns'yi gösterir.
	>google.com		        aradığımız ağın dns'ini gösterir.
	>server 127.0.1.1	        bağlanmak istediğimiz dns'yi değiştirebiliriz.	

    sudo nano /etc/resolv.conf	dns dosyasını açarız.
    nameserver 127.0.1.1	        bağlanmak istediğimiz dns'yi değiştirebiliriz.	
    
## Sunucu Kurma

    sudo apt install tasksel	sunucu kurma arayüzünü kurar.
    sudo tasksel sunucu_adı		yeni sunucu kurar.
    
## Proxy Kurma

    foxyproxy 		chrome eklentisini kuruyoruz.
    fresh ip address	http://www.us-proxy.org/ sitesinden anonymous veya elite proxy iplerini kopyalıyoruz.
    proxy checker		http://www.checker.freeproxy.ru/checker/ sitesinden kopyaladığımız iplerin çalışırlığını test ediyoruz. çalışan ipleri kurduğumuz foxyproxy eklentisi üzerinden port numarası ile birlikte giriyoruz.
    
 ## VPN Kurma
 
     vpn book			https://www.vpnbook.com/ sitesinden openvpnden istediğimiz vpn paketini indiriyoruz.
					vpn kapetini zip den çıkartıyoruz.
     sudo openvpn orn_vpn		indirdiğimiz klasör içindeki vpnleriden birini çalıştırıyoruz.
					vpnbook sitesindeki username ve password ü kullanarak vpn e bağlanıyoruz.
                    
## Grub Onarma

    sudo add-apt-repository ppa:yannubuntu/boot-repair
    sudo apt-get update
    sudo apt-get install -y boot-repair && (boot-repair &)
    sudo update-grub
    
## Disk Bağlanma Sorunu Çözümü

**Windwos hızlı başlatma için kendini tam olarak kapatmaz, bu tip durumlarda linuxtan windows disklerine erişmemize izinverilmez. Bunu önelemek için windowsun hızlı başlatma seçeneği kapatılabilir.**

    powercfg.exe /hibernate off			windowsta cmd yi yönetici çalıştırılır. 
							Girilen komut ile windowsun hızlı başlat seçeneği kapatılır.

*Eğer diğer disklere halen erişemiyorsanız aşağıdaki kodları kullanarak tüm disklere erişim sağlaya bilirsiniz.*

    sudo fdisk -l					Disklerin hangi bölümde kurulduğunu listeler.
    sudo mkdir -p /media/sdb(x)			NTFS biçimli bir disk bölümünü /media dizini altında "sdb1" adında bir dizine bağlamak için  
							/media dizini altında sdb1 adında bir klasör yoksa bu klasörü oluşturmalıyız.
    sudo mount -t ntfs-3g /dev/sdb1 /media/sdb(x)	/media/sdb(x) dizinine bağlıyoruz. (x) yerine bağlanmak istediğimiz bölüm yazılmalıdır.
    
## Ubuntu 16.04 Güç kritik seviyeye düştüğünde derin uykuya geçmeyi aktif etme

    sudo pm-hibernate	derin uykunun çalışırlığını test ettik.
    
    Bunu yapmak için, düzenlemeye başlayın:
    sudo nano /etc/polkit-1/localauthority/50-local.d/com.ubuntu.enable-hibernate.pkla

	[Re-enable hibernate by default in upower]
	Identity=unix-user:*
	Action=org.freedesktop.upower.hibernate
	ResultActive=yes

	[Re-enable hibernate by default in logind]
	Identity=unix-user:*
	Action=org.freedesktop.login1.hibernate;org.freedesktop.login1.handle-hibernate-key;org.freedesktop.login1;org.freedesktop.login1.
	hibernate-multiple-sessions;org.freedesktop.login1.hibernate-ignore-inhibit
	ResultActive=yes

*ctrl+o ve enter'a basarak kaydedin ve ctrl+x ile çıkın.*
güç ayarlarından derin uykuyu seçerek aktif hale getirin.
    
## ubuntu 16.04 Güç kritik seviyesini ayarlama

    sudo nano /etc/UPower/UPower.conf

	UsePercentageForPolicy=true
	PercentageLow=10
	PercentageCritical=7
	PercentageAction=5
	CriticalPowerAction=HybridSleep
    
