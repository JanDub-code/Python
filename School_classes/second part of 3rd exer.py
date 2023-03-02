import datetime

ted=datetime.datetime.now()

print(ted)

zadam=datetime.datetime(2023, 3, 2)
zadam.strftime("%d.%m.%Y")

print(zadam)
print(zadam.weekday())

datum_ze_stringu = datetime.datetime.strptime("2023-03-02", "%Y-%m-%d")
print(datum_ze_stringu+datetime.timedelta(hours=72))
print(datum_ze_stringu-zadam+datetime.timedelta(hours=72))

x=input("Zadejte datum ve formatu YYYY-MM-DD: ")
pomocna=datetime.datetime.strptime(x, "%Y-%m-%d")
print(pomocna)

print(ted - pomocna)

def funkce():
    print("Ahoj")
    

print(funkce())

def fc(jmeno,ano):
    print(f"ahojky {jmeno} co se stane ? {ano}")

fc("Jan","uceni na 3 doby")

def ukol1( list, maxcislo):
    newlist = []
    for cislo in list:
        if cislo < maxcislo:
            newlist.append(cislo)
    print(newlist)

x=[1,2,3,4,5,6,7,8,9,10]


ukol1(x,5)