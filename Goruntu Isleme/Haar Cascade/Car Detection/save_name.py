#-*-coding: utf-8 -*-
import numpy as np
import cv2
import os

def create_file():
    """
    Egitim icin kullanacigimiz resimlerin
    negatif olanlarını bg.txt dosyasına
    positif olanlarını info.lst dosyasına yazdırdık.
    
    pozitif image için isimlendirme aşağıdaki gibi olmalıdır.
    file_name/img_name.jpj n x y w h   :n=resimdeki çerçeve sayısı (birden fazla ise x y w h eklenerek devam edilir.)
    """
    for img in os.listdir("TrainImages"):
        if img[:3] == "neg":
            line="TrainImages"+'/'+img+'\n'
            with open('bg.txt','a') as f:
                f.write(line)
        elif img[:3] == "pos":
            line="TrainImages"+'/'+img+" 1 0 0 100 40\n"
            with open('info.lst','a') as f:
                f.write(line)

create_file()
