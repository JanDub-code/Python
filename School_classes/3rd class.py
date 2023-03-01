dictionary_of_apes = {

    "Chimpanzee": "Pan troglodytes",
    "Gorilla": "Gorilla gorilla",
    "Orangutan": "Pongo pygmaeus",
    "Bonobo": "Pan paniscus",
    "Gibbon": "Hylobates lar",
    "Siamang": "Hylobates syndactylus",
    "Mandrill": "Mandrillus sphinx",
}
dictionary_of_apes["Siamang"] = "Holobobardus Maximus"

print(dictionary_of_apes["Siamang"])

dictionary_of_numbers = {
    "Eva" : 741258963,
    "Adam" : 852369741,
    "Eve" : 963852741,
    "Eva" : 7412575842,
    "Adam" : 852369741,
    "Prokop" : 963852741,
    "Frank" : 741258963,
}
print( dictionary_of_numbers.keys())
print( dictionary_of_numbers.values())

for x in dictionary_of_numbers.keys():
    if(x == "Eva"):
        print(dictionary_of_numbers[x])

adresar = dict()

adresar["Dubus"] = dict()
adresar["Dubus"]["Jmeno"] = "Jan"
adresar["Dubus"]["Prijmeni"] = "Dubus"
adresar["Dubus"]["Telefon"] = 123456789

adresar["Novak"] = dict()
adresar["Novak"]["Jmeno"] = "Petr"
adresar["Novak"]["Prijmeni"] = "Novak"
adresar["Novak"]["Telefon"] = 987654321

print(adresar["Dubus"])

def secti(a,b):
    return a+b

print(secti(1,2))
print(secti("Jan","Dubus"))

def secti1(a,b):
    return a,b,a+b

x,y,z = secti1(1,2)
print(x,y,z)

def secti2(a,*args):
    return sum(args)

print(secti2(1,2,3,4))
print(secti2(1,2,3,4,5,6,7,78478,9,10))

print(1,2,3,4,5,6,7,8,9,10,sep=":")

def pozdrav(jmeno,prijmeni="XDDDD"):
    print("Ahoj",jmeno,prijmeni)

pozdrav("Jan")

def funkce(*args, **kwargs):
    print(args)
    print(kwargs)

funkce(1,2,3)
funkce(1,2,3, a=1, b=2, c=3)