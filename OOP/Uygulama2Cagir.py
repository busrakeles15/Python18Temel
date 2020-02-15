from Uygulama2 import DosyaTool
defter = DosyaTool(adres="defter.csv",alanlar=["Bir","İki","Üç"])
hesap = DosyaTool(adres="banka.csv",alanlar=["BankaHesapNo","Tip","Tutar"])
# defter.YeniKayit()

dataset = DosyaTool(adres="rastgele.csv",alanlar=["Uzunluk","En"])
import random as rnd
dataset.Temizlik()
for i in range(0,5000):
    line = f"{rnd.randrange(0,800,5)};{rnd.randrange(0,10000,100)}\n"
    dataset.OtomatikYeniKayit(line)
