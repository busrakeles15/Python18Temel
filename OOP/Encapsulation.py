class Araba:
    tur = "Araba"
    __makshiz = 0
    def __init__(self,marka,model,yetki=0):
        self.model = model
        self.marka = marka
        self.__makshiz = 250
        self.yetki = yetki

    @property
    def maksimumHizGetir(self):
        if self.yetki == 1:
            return self.__makshiz
        else:
            return "yetkisiz giriş"

    @maksimumHizGetir.setter
    def maksimumHizGetir(self,hiz):
        if str(hiz).isnumeric():
            if int(hiz) > 10:
                    self.__makshiz = hiz
            else:
                print("Dönüşümde Hata Var")

    def yuru(self):
        print(self.model,self.marka,"Yürüdü")
    
    def dur(self):
        print(self.model,self.marka,"Durdu")


Arac1 = Araba("BMW","5.20",1)
Arac2 = Araba("Audi","A8L")
Arac1.yuru()
print(Arac1.maksimumHizGetir)
print(Arac2.maksimumHizGetir)
