nakupni_kosik= []

nakupni_kosik.append("jablko")
nakupni_kosik.append("hruska")
nakupni_kosik.append("banan")
nakupni_kosik.append("pomeranc")
nakupni_kosik.append("mandarinka")


nakupni_kosik.pop(0)
odpad = nakupni_kosik.pop()
print(nakupni_kosik)

print(odpad)

print(nakupni_kosik[-1])

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list3 = list1+list2

print(list3)
list3.extend(["brumbrumbrum"]*9)
print(list3)

cislo = list(range(0,101,5))
print(cislo)

list_of_lists = [["Herman",50],["susan", 60],["joseph", 70]]
print(list_of_lists[-1][0])

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2= {1, 2, 3, 4, 5, 44,55,77,88,990}

set4 = set1.union(set2)
print(set4)

mzk= {'Harry Potter','Dvacet tisic mil pod morem','Hoši z Marsu','Klub věrných'}
mahenova = {'Auf der Suche nach der verlorenen Zeit','Klub věrných','Kniha o mrtvých'}

print(mzk.intersection(mahenova))

print(mahenova.difference(mzk))

vstup = input("pokud souhlasis napis : ano ")
if vstup in ["ano","okay"]:
    print("diky")
else:
    print("chcípni hajzle")

    
    n=0
while(n !=100):
    print("už to nikdy neudělám")
    n+=1

for i in range(0,100):
    print("už to nikdy neudělám")


liststudentu = []
for i in range(0,5):
    liststudentu.append(input("zadej jmeno studenta : "))

liststudentu.sort()
print(liststudentu)

for i in range(0,5):
    print("*"*i)
for i in range(5,0,-1):
    print("*"*i)