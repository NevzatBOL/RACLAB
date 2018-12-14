# DR Racket ile Lisp programlama

raket'ı kuralım
  
     sudo apt-get install racket
     
DrRacket programını başlatalım.

lisp alıştırmalar

    #lang slideshow
    5                         direk integar bir değer yazılabilir.
    "Merhaba"                 ""içerisinde sting bir ifade yazılabilir.
    (circle 30)               30 çaplı daire çizdirir.
    (rectangle 10 20)         10*20 dikdörtgen çizdirir.
    (hc-append 10 (circle 30)(rectangle 10 20))  daire ve dik dört geni yan yana çizdirir. aralarında 10 birim boşluk bırakır.

    (define c (circle 10))    define ile değişken tanımlana bilir. değişken içerisine string ve intiger gibi bir ifade olabileceği gibi bir şekilde atanabilir.
    c

    (define (topla a b)       topla isminde bir fonksiyon tanımladık.
      (+ a b))

    (topla 10 20)             topla fonksiyonunu çalıştırdık.

    (define (four p)          four isimli bir fonsiyon oluşturduk.
     (define two-p (hc-append p p)) p değişkenini yan yana yazdırır.
     (vc-append two-p two-p))   two-p değikenini alt alta yazdırır.

    (four (circle 10))      four fonksiyonunu çalıştırdık.
    
matamatiksel işlemler

    (+ 2 4)                 2+4=8
    (+ (+ 2 4) (+ 4 8))     (2+4)+(4+8)=18
    (+ 1 (+ 1 (+ 1 8) 2) 3 4 5)
    (sin 0)

    (define x 4)        değişken tanımladık.
    (define y 3)

    (define z (+ (* x x) (* y y))) 
    z

    (sqrt z)    karekök aldık.

string değişkenler

    (define name "hello") 
    name
    (string-append name " world")   string e ekleme yaptık.

    (define dizgi1 "merhaba")
    dizgi1

    (string-length dizgi1)    string değişkenin uzunluğunu bulduk
    (string-ith dizgi1 4)     srint değişkenin 4. karakterini bulduk.
    (string-append dizgi1 (number->string(string-length dizgi1)))

Koşul ifadeleri

    (define a #true)
    (define b #false)

    (or a b)
    (and a b)

    (if (= x 0) 0 (/ 1 x))    eğer x 0 a eşitse 0 değilse 1/x yazdırır.

    (define c 10)
    (define d 15)
    (if (= c d)
        (print "esit")
        (if (> c d)
            (print "c buyuk")
            (print "d buyuk")))

    (cond [(= c d) (print "esit")]
          [(> c d) (print "c buyuk")]
          [(< c d) (print "d buyuk")])

Fonksiyonlar

    #lang racket
    (define (f a) (* 2 a))
    (f 100)

    (define (topla a b) (+ a b))
    (topla 5 9)

    (define (uygula fonksiyon a b)
      (fonksiyon a b))

    (uygula + 10 20)
    (uygula * 10 20)

    (define (fact n)
      (if (= n 0) 1 (* n (fact (- n 1)))))

    (fact 5)

    (define (fibo n)
      (if (= n 1) 1
          (if (= n 2) 1
                        (+ (fibo (- n 1))
                                 (fibo (- n 2))))))
    (fibo 8)


listeler

    (list 1 2 3 4 "a" 5)
    (define a (list 1 2 3))
    a
    (first a)
    (car a)
    (rest a)
    (cdr a)

    (append '(20) a)
    a

    (cons 10 a)
    (cons (list 10) a)

    (define (birarttir l1) (if (empty? l1) l1 (cons (+ 1 (car l1))
                                                    (birarttir (rest l1)))))

    (birarttir (list 1 2 3))

    (define (bindir f l1) (if (empty? l1) '() (cons (f (car l1))
                                                (bindir f (rest l1)))))

    (define b (list 1 2 3))
    (define (yenif b) (* b b))
    (bindir yenif (list 2 8 3))

    (define (topla l1 l2) (cond[(empty? l1) l2]
                               [(empty? l2) l1]
                               [else (cons (+ (car l1) (car l2)) (topla (rest l1) (rest l2)))]))

    (define q (list 1 5 4 6))
    (define r (list 2 7 8 9 10))

    (topla q r)
    
Ağaçlar    
   
    (list 1 '() '())
    (define a1 (list 1 (list 2 '() '()) (list 3 '() '())))
    (define (kok agac) (first agac))
    (kok a1)

    (define (topla agac) (if (empty? agac) 0
                          (+ (first agac)
                            (topla (car (cdr agac)))
                            (topla (car (cdr (cdr agac)))))))
    (topla a1)
   
   
   
    (define myTree
    (list 53
          (list 23
                (list 11 '() '())
                (list 400 '() '()))
          (list 17 '() '())))

    (define (node agac) (car agac))
    (define (sol agac) (car (cdr agac)))
    (define (sag agac) (car (cdr (cdr agac))))
    (define (eb2 a b) (if (> a b) a b))
    (define (eb3 a b c) (eb2 (eb2 a b) (eb2 a c)))
    (define (enbuyuk agac)
     (if (empty? agac) 0
      (eb3 (node agac)
         (enbuyuk (sol agac))
         (enbuyuk (sag agac)) )))

    (enbuyuk myTree)

Ağırlık ve Graflar UCS algoritması

    (define harita (list (list 1 2 1)
          (list 1 3 3)
          (list 2 3 2)
          (list 3 2 2)
          (list 2 4 12)
          (list 2 7 8)
          (list 3 5 1)
          (list 5 12 1)))

    ;bir dugumden gidilebilecek alternatiflerin listesi
    ;dugum numaralari ve agirlikleri ile dondurulur.
    (define (alt alist dugum)
      (if(empty? alist)
         alist
         (if(= dugum (first(first alist)))
            (cons (rest (first alist)) (alt (rest alist) dugum))
            (alt (rest alist) dugum)
            )
         )
      )

    (alt harita 2)

    ;iki alternatiften ucuz olanı dondurur.
    (define (karsilastir alt1 alt2)
      (if (empty? alt2)
          alt1
      (if(> (first(rest alt1)) (first (rest alt2)))
         alt2
         alt1)))

    ;alternatiflerden minimumunu bulan foksiyon
    (define (min-alt alist)
      (if (empty? alist)
          alist
          (karsilastir (first alist) (min-alt (rest alist)))
          )
      )

    (min-alt (alt harita 2))
    (define (ucs alist baslangic bitis) (if (empty? alist)
                                            alist
                                            (cons baslangic
                                                  (if (empty? (alt alist baslangic)); hala listede eleman varsa
                                                      null
                                                      (if ( = bitis (first (min-alt (alt alist baslangic)))) ;gidebileceğimiz dugum varsa
                                                          ;aradigimiz dugumu bulduysak
                                                          (list (first (min-alt (alt alist baslangic))))
                                                          (ucs alist (first (min-alt (alt alist baslangic)))
                                                 bitis))))))

    (ucs harita 1 5)
 
Koşul Tatmin Problemleri(CSP)
 
    (define kenarlar (list (list 1 3)
                         (list 1 2)
                         (list 2 4)
                         (list 3 2)
                         (list 3 4)))

    (define dugumler (list 1 2 3 4))

    (define renkler (list 1 2 3))

    (define cozum (list (list 1 1)
                        (list 2 2)
                        (list 3 3)
                        (list 4 2)))

    (define (birinci k) (first (first k)))
    (define (ikinci k) (first (rest (first k))))

    ;komsularin listesini donduren fonksiyon (komsular dugum kenarlar_listesi)
    (define (komsular d k)
      (if (empty? k) null
          ;listede hala eleman varsa ilk siradaki dugum aranan dugume esitmi?
          (if (= (birinci k) d)
              (cons (ikinci k) (komsular d (rest k)))
              (if (= (ikinci k) d)
                  (cons (birinci k) (komsular d (rest k)))
                  (komsular d (rest k))
                  ))))

    (komsular 2 kenarlar)

    ;verilen cozum icerisindeki aranan dugumun rengini donduren fonksiyon.
    (define (renk d c)(if (empty? c) null
                          (if (= (birinci c) d)
                              (ikinci c)
                              (renk d (rest c)))))
    (renk 4 cozum)

    (define (kontrol-yardim d kl c) (if (empty? kl) #true
                                        (if (= (renk d c) (renk (first kl) c))
                                            #false
                                            (kontrol-yardim d (rest kl) c))))

    ;verilen kenarlar listesi ve cozum icin verilen komsulari ile uyumuna bak.
    (define (kontrol d k c) (kontrol-yardim d (komsular d k) c))

    (kontrol 2 kenarlar cozum)

    (define (csp ds ks c) (if (empty? ds) #true
                              (and (kontrol (first ds) ks c)
                              (csp (rest ds) ks c))))

    (csp dugumler kenarlar cozum)  
    
DFS Algoritmasının binary ağaçta kodlanması  

    (define myTree (list 53
                         (list 23
                               (list 11 '() '())
                               (list 4 '() '()))
                         (list 17 '() '())
                         ))

    (define (root tree) (first tree))
    (define (left tree) (first (rest tree)))
    (define (right tree) (first (rest (rest tree))))

    (define (count atree) (if (empty? atree) 0
                              (+ (count (left atree))
                                 (count (right atree))
                                 1)))
    (count (left myTree))

    (define (DFS atree anode) (if (empty? atree) 0
                                  (if (> (DFS (left atree) anode) 0)
                                      (DFS (left atree) anode)
                                      (if (> (DFS (right atree) anode) 0)
                                          (DFS (right atree) anode)
                                          (if (= anode (root atree))
                                              (count atree)
                                              0)))))

    (DFS myTree 4)                        

BFS Algoritmasının binary ağaçta kodlanması  

    (define myTree (list 53
                         (list 23
                               (list 11 '() '())
                               (list 4 '() '()))
                         (list 17 '() '())
                         ))

    (define (root tree) (first tree))
    (define (left tree) (first (rest tree)))
    (define (right tree) (first (rest (rest tree))))

    (define (countl atree limit) (if (empty? atree) 0
                                     (if (= limit 0) 0
                                         (+ 1 (countl (left atree) (- limit 1))
                                            (countl (right atree) (- limit 1))))))

    (countl myTree 3)

    (define (level atree anode) (if (empty? atree) 0
                                    (if (= (root atree) anode) 1
                                        (+ (level (left atree) anode)
                                           (level (right atree) anode)
                                           (if (> (+ (level (left atree) anode) (level (right atree) anode)) 0)
                                           1
                                           0)))))
    (level myTree 17)

    (define (BFS atree anode) (+ (countl atree (level atree anode))))

    (BFS myTree 23)

Oyun Ağaçları ve Tic Tac Toe

    (define tahta (list (list 1 0 -1)
          (list 0 -1 0)
          (list -1 0 1)))

    (define (satirkontrol satir) (if (= (first satir) (second satir) (third satir))
                                     (first satir)
                                     0))

    (satirkontrol (first tahta))

    (map satirkontrol tahta)

    (define (dondur atahta) (list (map first tahta)
                                  (map second tahta)
                                  (map third tahta)))

    (dondur tahta)

    (map satirkontrol (dondur tahta))

    (define (kosegen atahta) (if (= (first (first atahta))
                                    (second (second atahta))
                                    (third (third atahta)))
                                 (first (first atahta))
                                 0))

    (define (tkosegen atahta) (if (= (first (third atahta))
                                    (second (second atahta))
                                    (third (first atahta)))
                                 (second (second atahta))
                                 0))
    (define (kazananlistesi atahta) (append (map satirkontrol atahta)
                              (map satirkontrol (dondur atahta))
                              (list (kosegen atahta))
                              (list (tkosegen atahta))))

    (kazananlistesi tahta)

    (define (bireindir alist) (if (empty? alist) 0
                                  (if (not (= (first alist) 0))
                                      (first alist)
                                      (bireindir (rest alist)))))

    (define (kazanan atahta) (bireindir (kazananlistesi atahta)))

    (kazanan tahta)

First Order Logic

    (require racklog)

    (%which () %true)
    (%which () %fail)

    (define %knowbase
      (%rel ()
        [('Odysseus 'TeX)]
        [('Odysseus 'Racket)]
        [('Odysseus 'Prolog)]
        [('Odysseus 'Penelope)]
        [('Penelope 'TeX)]
        [('Penelope 'Prolog)]
        [('Penelope 'Odysseus)]
        [('Telemachus 'TeX)]
        [('Telemachus 'calculus)]))

    (%which ()
            (%knowbase 'Odysseus 'TeX))

    (%which ()
            (%knowbase 'Odysseus 'calculus))
    ;Odysseus'un bildigi dillerden birini getirir.
    (%which (what) 
            (%knowbase 'Odysseus what))

    (%more) ;daha fazla degisken dondurur.
    (%more)

    (%which (who)
            (%knowbase who 'calculus))

    (define %computer-literate
      (%rel (person)
        [(person)
          (%knowbase person 'TeX)
          (%knowbase person 'Racket)]
        [(person)
          (%knowbase person 'TeX)
          (%knowbase person 'Prolog)]))

    (%which ()
            (%computer-literate 'Penelope))

    (%which ()
            (%computer-literate 'Telemachus))

    (%which (who)
            (%computer-literate who))

    (%more)
    (%more)
    (%more)

    (%assert! %knowbase ()
              [('Odysseus 'archery)])

    (%which (who)
            (%knowbase who 'archery))

    (%assert! %knowbase ()
              [('Telemachus 'Prolog)])

    (%which () (%computer-literate 'Telemachus))

Referans Linkler

http://www.ccs.neu.edu/home/matthias/HtDP2e/

https://docs.racket-lang.org/racklog/index.html

https://www.youtube.com/watch?v=4fXewRNBJUE&list=PLh9ECzBB8tJMNe6hHxv5ztxh5e5bUHShA
