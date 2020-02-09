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
        if self.sayac["Darbe"]>2:
            self.sayac["Darbe"]=0
            self.saglik += 200
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
karlist = [DeadPool,Hulk,IronMan,CaptainAmerica]
P1 = rnd.choice(karlist)()
P2 = rnd.choice(karlist)()
while P1.saglik > 0 and P2.saglik > 0:
    time.sleep(1)
    P1.Defans(P2.Ofans())
    print(f"{P1.isim} Saglık:{P1.saglik} {P2.isim} Saglık:{P2.saglik}")
    time.sleep(1)
    P2.Defans(P1.Ofans())
    print(f"{P1.isim} Saglık:{P1.saglik} {P2.isim} Saglık:{P2.saglik}")