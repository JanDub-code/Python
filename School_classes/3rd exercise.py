slovik = { "jmeno" : "Adam", "vek": "23" }

print(slovik["jmeno"])
slovik["prijmeni"] = "Novak"
print(slovik)

del(slovik["prijmeni"])

print(slovik)

list1 = ["xlogin1","jmeno1","xlogin2","jmeno2"]
#recreate list1 as dictionary
pop = dict()
for i in range(0,len(list1),2):
    pop[list1[i]] = list1[i+1]

print(pop)

data= [
  {
    "xlogin": "xvalovic",
    "jmeno": "Roman",
    "predmety": [
      "PYT",
      "ALG"
    ]
  },
  {
    "xlogin": "xhavlik",
    "jmeno": "Jan",
    "predmety": [
      "AI",
      "ALG"
    ]
  },
  {
    "xlogin": "xnadule",
    "jmeno": "Nada",
    "predmety": [
      "WD",
      "PYT"
    ]
  },
  {
    "xlogin": "xmuron",
    "jmeno": "Mikulas",
    "predmety": [
      "TZI",
      "PTN"
    ]
  },
  {
    "xlogin": "xpernes",
    "jmeno": "Petr",
    "predmety": [
      "PYT",
      "MAT"
    ]
  }
]

for student in data:
    if("ALG" in student["predmety"]):
        print(student["jmeno"])

X1=set()

for student in data:
    for predmet in student["predmety"]:
        X1.add(predmet)

print(X1)  
   
seznam = dict()

print(seznam)

import random

hra = ["kamen", "nuzky", "papir"]

x = input("Zadejte svuj tah: kamen,nuzky,papir (konec pro ukonceni hry))")

while(x != "konec"):
    x = input("Zadejte svuj tah: kamen,nuzky,papir (konec pro ukonceni hry))")
    y = random.choice(hra)
    if(x == y):
        print("Remiza")
    elif(x == "kamen" and y == "nuzky"):
        print("Vyhrava hrac")
    elif(x == "nuzky" and y == "papir"):
        print("Vyhrava hrac")
    elif(x == "papir" and y == "kamen"):
        print("Vyhrava hrac")   
    elif(x=="kamen" and y=="papir"):
        print("Vyhrava pocitac")
    elif(x=="nuzky" and y=="kamen"):
        print("Vyhrava pocitac")
    elif(x=="papir" and y=="nuzky"):
        print("Vyhrava pocitac")

