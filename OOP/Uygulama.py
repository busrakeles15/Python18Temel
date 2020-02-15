class MarvelHero:
    tip = "Marvel"
    def __init__(self,guc,saglik,isim,Super=0):
        self.guc = guc
        self.saglik = saglik
        self.isim = isim
        self.SuperPow = Super
        self.sayac = dict.fromkeys(["vur","vur2","vur3","darbe","savunma","kacinma"],0)

    def sayacarttir(self,isim):
        self.sayac[isim] += 1
        
    def vur(self):
        self.sayacarttir(self.vur.__name__)
        return self.guc
    
    def vur2(self):
        self.sayacarttir(self.vur2.__name__)
        return self.guc*1/2
    
    def vur3(self):
        self.sayacarttir(self.vur3.__name__)
        return self.guc*2/3

    def darbe(self,guc):
        self.sayacarttir(self.darbe.__name__)
        self.saglik -= guc
        return self.saglik
    
    def savunma(self,guc):
        self.sayacarttir(self.savunma.__name__)
        self.saglik -= guc/2
    
    def kacinma(self,guc):
        self.sayacarttir(self.kacinma.__name__)
        return self.saglik

    def Ofans(self):
        import random as rnd
        liste = [self.vur,self.vur2,self.vur3]
        return rnd.choice(liste)()

    def Defans(self,guc):
        import random as rnd
        liste = [self.kacinma,self.savunma,self.darbe]
        return rnd.choice(liste)(guc)


class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__(100, 600, "Deadpool",4)


    def Defans(self,guc):
        print(self.isim,"Süper Güç Kullanıldı")
        import random as rnd
        if self.sayac["savunma"]>4:
            self.sayac["savunma"]=0
            self.saglik += 200
        liste = [self.kacinma,self.savunma,self.darbe]
        return rnd.choice(liste)(guc)   

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__(100, 800, "Hulk",2)

class IronMan(MarvelHero):
    def __init__(self):
        super().__init__(90, 500, "IronMan",5)
    def Defans(self,guc):
        print(self.isim,"Süper Güç Kullanıldı")
        import random as rnd
        # if self.sayac["Darbe"]>2:
        #     self.sayac["Darbe"]=0
        #     self.saglik += 200
        liste = [self.kacinma,self.savunma,self.darbe]
        return rnd.choice(liste)(guc)  

class CaptainAmerica(MarvelHero):
    def __init__(self):
        super().__init__(75, 500, "CaptainAmerica",4)

    def Ofans(self):
        print(self.isim,"Süper Güç Kullanıldı")
        guc = 0
        import random as rnd
        liste = [self.vur,self.vur2,self.vur3]
        guc =  rnd.choice(liste)()
        if self.sayac["vur"]>3:
            guc *= 2
            self.sayac["vur"] = 0
        return guc
import random as rnd
import time       
class Oyun():

    def __init__(self,tip = 0):

        self.tip = tip
        self.karlist = [DeadPool,Hulk,IronMan,CaptainAmerica]
        self.P1 = None
        self.P2 = None
        self.OyunSec()

    def OyunSec(self):
        if self.tip:
            self.USvsPC()
        else:
            self.PCvsPC()

    def PCvsPC(self):
        self.P1 = rnd.choice(self.karlist)()
        self.P2 = rnd.choice(self.karlist)()
        while self.P1.saglik > 0 and self.P2.saglik > 0:
            time.sleep(1)
            self.P1.Defans(P2.Ofans())
            print(f"{self.P1.isim} Saglık:{self.P1.saglik} {self.P2.isim} Saglık:{self.P2.saglik}")
            time.sleep(1)
            P2.Defans(P1.Ofans())
            print(f"{self.P1.isim} Saglık:{self.P1.saglik} {self.P2.isim} Saglık:{self.P2.saglik}")
    
    def USvsPC(self):
        self.P1 = rnd.choice(self.karlist)()
        for i in range(len(self.karlist)):
            print(f"{i+1}-{self.karlist[i].__name__}")
        self.P2 = self.karlist[int(input("Karakteri seçiniz"))-1]()
        while self.P1.saglik > 0 and self.P2.saglik > 0:
            time.sleep(1)
            self.P1.Defans(self.OfansSec())
            print(f"{self.P1.isim} Saglık:{self.P1.saglik} {self.P2.isim} Saglık:{self.P2.saglik}")
            time.sleep(1)
            self.DefansSec(self.P1.Ofans())
            print(f"{self.P1.isim} Saglık:{self.P1.saglik} {self.P2.isim} Saglık:{self.P2.saglik}")
    
    def OfansSec(self):
        menu = """
        1 -vur1
        2 -vur2
        3 -vur3
        Saldırı Tipini Seçiniz:
        """
        hareket =int(input(menu))
        if hareket == 1:
            fonk = self.P2.vur()
        return fonk

    def DefansSec(self,guc):
        menu = """
        1 -Kaçınma
        2 -Savunma
        3 -Darbe
        Savunma Tipini Seçiniz:
        """
        defans = int(input(menu))
        if defans == 1:
           fonk = self.P2.kacinma
        return fonk(guc)

