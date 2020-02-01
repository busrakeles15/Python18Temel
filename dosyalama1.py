def DosyaAc(adres="defter.csv"):
    import os
    if os.path.exists(adres):
        return open(adres,"r+",encoding="UTF-8")
    else:
        return open(adres,"w+",encoding="UTF-8")


def KayitListele(liste):
    for i in range(len(liste)):
        satir = liste[i].split(";")
        print(f"{i+1}-{satir[0]} {satir[1]} {satir[2]}")

dosya = DosyaAc()
liste = dosya.readlines()
KayitListele(liste)


def YeniKayit(liste):
    liste.append(GirisAl())
    return liste

def GirisAl():
    adi = input("Adi Giriniz:")
    soyadi = input("Soyadi Giriniz:")
    tel = input("Telefon Giriniz")
    return f"{adi};{soyadi};{tel}\n"

YeniKayit(liste)

KayitListele(liste)