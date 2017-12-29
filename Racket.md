# DR Racket ile Lisp programlama

raket'ı kuralım
  
     sudo apt-get install racket
     
DrRacket programını başlatalım.
 
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
    
  

https://docs.racket-lang.org/quick/index.html
