class Hrdina:
    def __init__(self,jmeno,sila):
        self.jmeno = jmeno
        self.sila = sila
        self.zivoty = 100

    def utok(self,nepritel):
        if(self.je_nazivu()):
            if nepritel.zivoty > 0:
                nepritel.zivoty -= self.sila
                print(f"{self.jmeno} útočí na {nepritel.jmeno} a zničí mu {self.sila} životů. Zbývá mu {nepritel.zivoty} životů.")
            else :
                print(f"{nepritel.jmeno} už je mrtvý.")
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
        self.sila += self.jedovatost*10

    def utok(self,nepritel):
        if(self.je_nazivu()):
            if nepritel.zivoty > 0:
                nepritel.zivoty -= self.sila
                print(f"{self.jmeno} útočí na {nepritel.jmeno} a zničí mu {self.sila} životů. Zbývá mu {nepritel.zivoty} životů.")
            else: 
                print(f"{nepritel.jmeno} už je mrtvý.")
        else:
            print(f"{self.jmeno} je mrtvý a nemůže útočit.")

    def je_nazivu(self):
        if self.zivoty > 0:
            return True
        else:
            return False

bob = Hrdina("Bob",50)
čupakabra = Monster("Čupakabra",20,1)

bob.utok(čupakabra)
čupakabra.utok(bob)
bob.utok(čupakabra)
čupakabra.utok(bob)
bob.utok(čupakabra)