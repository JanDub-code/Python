import csv 
with open("/home/hans/Documents/Python/Python/School_classes/data.csv") as f:
    csv_data = csv.reader(f)
    for line in csv_data:
        print(line)

class Fix:

    def __init__(self):
        self.barva = "červená" 
        # self._barva = "červená" # protected
        # self.__barva = "červená" # private
        self.kapacita = 50

    def pis(self):
        if self.kapacita > 0:
            print("Píšu.")
            self.kapacita -= 10
        else:
            print("Nemám inkoust. Musíš ho doplnit.")
    
    def doplninkoust(self,kolik):
        self.kapacita += kolik
        print(f"Doplnil jsem inkoust. Nyní mám {self.kapacita}.")

    def vypis(self):
        print(f"Mám barvu {self.barva} a kapacitu {self.kapacita}.")

    def __del__(self):
        print("Krev za krém!!!")


class hrdina:

    def __init__(self,jmeno,sila):
        self.jmeno = jmeno
        self.sila = sila
        self.zivoty = 100
        self.zbran = None

    def utok(self,nepritel):
        if nepritel.zivoty > 0:
            nepritel.zivoty -= self.sila
            print(f"{self.jmeno} útočí na {nepritel.jmeno} a zničí mu {self.sila} životů. Zbývá mu {nepritel.zivoty} životů.")
        else :
            print(f"{nepritel.jmeno} je mrtvý.")

    def __del__(self):
        if self.zivoty > 0:
            print(f"{self.jmeno} odešel do západu slunce.")
        else:
            print(f"{self.jmeno} už byl mrtvý.")

    def vzít_zbraň(self,zbran):
        self.zbran = zbran
        print(f"{self.jmeno} si vzal {self.zbran.nazev}.")
        self.sila += self.zbran.sila

class Zbran:

    def __init__(self,nazev,sila):
        self.nazev = nazev
        self.sila = sila

    def __del__(self):
        print(f"{self.nazev} se rozpadla.")

fix1=Fix()
fix1.kapacita -=40
print(fix1.kapacita)

fix1.vypis()

fix1.pis()
fix1.pis()
fix1.doplninkoust(20)
fix1.pis()

bob = hrdina("Bob",50)
bobek = hrdina("Bobek",20)
kosa = Zbran("kosa",50)
bob.vzít_zbraň(kosa)

bob.utok(bobek)
bob.utok(bobek)

