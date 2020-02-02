adres = ""
alanlar = []
def DosyaAc():
    import os
    if os.path.exists(adres):
        return open(adres,"r+",encoding="UTF-8")
    else:
        return open(adres,"w+",encoding="UTF-8")


def GirisAl(*args):
    kayit = ""
    for item in args:
        kayit += input(f"{item} giriniz:") + ";"
    kayit = kayit.rstrip(";") + "\n"
    return kayit


def KayitListele(liste):
    for i in range(len(liste)):
        satir = liste[i].split(";")
        print(f"{i+1}-{satir[0]} {satir[1]} {satir[2]}")

def YeniKayit(liste):
    liste.append(GirisAl(*alanlar))
    return liste

def OtomatikYeniKayit(liste,line):
    liste.append(line)
    return liste

def KayitDuzenle(liste):
    KayitListele(liste)
    kayitNum = int(input("Düzenlemek İstediğiniz Kaydı Seçiniz"))
    liste[kayitNum-1] = GirisAl(*alanlar)
    return liste

def KayitSil(liste):
    KayitListele(liste)
    kayitNum = int(input("Silmek İstediğiniz Kaydı Seçiniz"))
    if kayitNum <= len(liste) > 0:
        del liste[kayitNum-1]
    return liste

def KayitArama(liste):
    sonuc = []
    metin = input("Aramak istediğiniz kelimeyi giriniz")
    for item in liste:
        for item_1 in item.split(";"):
            if metin in item_1:
              sonuc.append(item)
    print(sonuc)

def dosyaKayit(liste):
    with DosyaAc() as dosya:
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)


menu = """
1-Ekleme
2-Güncelleme
3-Silme
4-Listeleme
5-Çıkış
6-Arama
İşlem Seçiniz:
"""
anahtar = 1
def sifirla(liste):
    global anahtar
    anahtar = int(not anahtar)
def Menu():
    sozluk = {"1":YeniKayit,"2":KayitDuzenle,"3":KayitSil,
    "4":KayitListele,"5":sifirla,"6":KayitArama}
    with DosyaAc() as dosya:
        liste = dosya.readlines()
        while anahtar == 1:
            fonk = sozluk.get(input(menu))
            if fonk:
                fonk(liste)
        else:
            dosya.seek(0)
            dosya.truncate()
            dosya.writelines(liste)

if __name__ == "__main__":
    adres = "defter.csv"
    alanlar = ["adi","soyadi","telefon"]
    Menu()
    
    

