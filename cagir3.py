import dosyalama1 as dos
dos.alanlar = ["Uzunluk","Cins","Sayı"]
dos.adres = "olcum.csv"
import random as rnd
liste = []
for i in range(10000):
    line = f"{rnd.randrange(0,1000,10)};{rnd.randrange(0,5)};{rnd.randrange(0,100,5)}\n"
    liste = dos.OtomatikYeniKayit(liste,line)
dos.dosyaKayit(liste)
    


