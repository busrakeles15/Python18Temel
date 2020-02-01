adres = "defter.csv"
alanlar = ["adi","soyadi","telefon"]
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




menu = """
1-Ekleme
2-Güncelleme
3-Silme
4-Listeleme
5-Çıkış
İşlem Seçiniz:
"""
anahtar = 1
def sifirla(liste):
    global anahtar
    anahtar = int(not anahtar)
def Menu():
    sozluk = {"1":YeniKayit,"2":KayitDuzenle,"3":KayitSil,"4":KayitListele,"5":sifirla}
    with DosyaAc() as dosya:
        liste = dosya.readlines()
        while anahtar == 1:
            sozluk.get(input(menu))(liste)
        else:
            dosya.seek(0)
            dosya.truncate()
            dosya.writelines(liste)

if __name__ == "__main__":
    Menu()
    
    

