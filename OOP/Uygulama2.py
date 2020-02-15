class DosyaTool():
    def __init__(self,adres="defter.csv",**kwargs):
        self.adres = adres
        self.alanlar = ["Adi","Soyadi","Telefon"]
        for key,value in kwargs.items():
            if key == "alanlar":
                self.alanlar = value

        self.dosya = self.DosyaAc()
        self.liste = self.dosya.readlines()

    def DosyaAc(self):
        import os
        if os.path.exists(self.adres):
            return open(self.adres,"r+",encoding="UTF-8")
        else:
            return open(self.adres,"w+",encoding="UTF-8")

    def GirisAl(self):
        kayit = ""
        for item in self.alanlar:
            kayit += input(f"{item} giriniz:") + ";"
        kayit = kayit.rstrip(";") + "\n"
        return kayit

    def KayitListele(self):
        for i in range(len(self.liste)):
            satir = self.liste[i].split(";")
            print(f"{i+1}-{satir[0]} {satir[1]} {satir[2]}")

    def YeniKayit(self):
        self.liste.append(self.GirisAl())

    def KayitDuzenle(self):
        self.KayitListele()
        kayitNum = int(input("Düzenlemek İstediğiniz Kaydı Seçiniz"))
        self.liste[kayitNum-1] = self.GirisAl()

    def KayitSil(self):
        self.KayitListele()
        kayitNum = int(input("Silmek İstediğiniz Kaydı Seçiniz"))
        if kayitNum <= len(self.liste) > 0:
            del self.liste[kayitNum-1]

    def KayitArama(self):
        """
        bu kayıt aramak için
        """
        sonuc = []
        metin = input("Aramak istediğiniz kelimeyi giriniz")
        for item in self.liste:
            for item_1 in item.split(";"):
                if metin in item_1:
                    sonuc.append(item)
        print(sonuc)


    def OtomatikYeniKayit(self,line):
        self.liste.append(line)

    def Temizlik(self):
        self.liste = []
        self.acilKaydet()

    
    def Menu(self):
        menu = """
        1-Ekleme
        2-Güncelleme
        3-Silme
        4-Listeleme
        5-Çıkış
        6-Arama
        İşlem Seçiniz:
        """
        sozluk = {"1":self.YeniKayit,"2":self.KayitDuzenle,"3":self.KayitSil,
            "4":self.KayitListele,"6":self.KayitArama}
        while True:
            fonk = sozluk.setdefault(input(menu),"Stop")
            if fonk != "Stop":
                fonk()
            else:
                break

    def acilKaydet(self):
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(self.liste)
        self.dosya.flush()


    def __del__(self):
        self.acilKaydet()
        self.dosya.close()