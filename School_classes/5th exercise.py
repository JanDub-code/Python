class Hrdina:
    def __init__(self,jmeno,sila):
        self.jmeno = jmeno
        self.sila = sila
        self.zivoty = 100
        self.zbran = None

    def seber_zbran(self,zbran):
        if(self.zbran == None):
            self.zbran=zbran
            print(f"{self.jmeno} sebral {self.zbran.nazev}.")
        else:
            print(f"Brácho už máš zbraň : ({self.zbran.nazev}) zahod ten krám nebo si ho nech.")

    def zahod_zbran(self):
        print(f"{self.jmeno} zahodil ten krám. ({self.zbran.nazev})")
        self.zbran = None

    def utok(self,nepritel):
        if(self.je_nazivu()):
            if nepritel.zivoty > 0:
                nepritel.zivoty -= self.sila+self.zbran.sila
                print(f"{self.jmeno} útočí na {nepritel.jmeno} a zničí mu {self.sila+self.zbran.sila} životů. Zbývá mu {nepritel.zivoty} životů.")
            else :
                print(f"{nepritel.jmeno} už je mrtvý. ({self.jmeno} zuřivě začal kopat do mrtvoly)")
        else:
            print(f"{self.jmeno} je mrtvý a nemůže útočit.")
    
    def je_nazivu(self):
        if self.zivoty > 0:
            return True
        else:
            return False

class Monster:
    def __init__(self,jmeno,sila,jedovatost):
        self.jmeno = jmeno
        self.zivoty = 100
        self.jedovatost = jedovatost
        self.sila = sila
        

    def utok(self,nepritel):
        if(self.je_nazivu()):
            if nepritel.zivoty > 0:
                nepritel.zivoty -= self.sila+(self.jedovatost*10)
                print(f"{self.jmeno} útočí na {nepritel.jmeno} a zničí mu {self.sila+(self.jedovatost*10)} životů. Zbývá mu {nepritel.zivoty} životů.")
            else: 
                print(f"{nepritel.jmeno} už je mrtvý. ({self.jmeno} zuřivě začal kopat do mrtvoly)")
        else:
            print(f"{self.jmeno} je mrtvý a nemůže útočit.")

    def je_nazivu(self):
        if self.zivoty > 0:
            return True
        else:
            return False
        
class Combat:
    def __init__(self,hrdina,monster):
        self.hrdina = hrdina
        self.monster = monster

    def průběh(self):
        if(self.hrdina.je_nazivu() and self.monster.je_nazivu()):
            print(f"{self.hrdina.jmeno} se setkává s {self.monster.jmeno}.")

    def konec(self):
        if(self.hrdina.je_nazivu()):
            print(f"{self.hrdina.jmeno} totálně vyhrál.")
        else:
            print(f"{self.monster.jmeno} totálně vyhrál.")

class Zbran:
    def __init__(self,nazev,sila):
        self.nazev = nazev
        self.sila = sila

bob = Hrdina("Bob",50)
čupakabra = Monster("Čupakabra",20,1)
párátko = Zbran("Párátko",10)
hopskulka = Zbran("Hopskulka",20)
boj = Combat(bob,čupakabra)

boj.průběh()
bob.seber_zbran(párátko)
bob.utok(čupakabra)
čupakabra.utok(bob)
bob.utok(čupakabra)
čupakabra.utok(bob)
bob.utok(čupakabra)
bob.seber_zbran(hopskulka)
bob.zahod_zbran()
boj.konec()