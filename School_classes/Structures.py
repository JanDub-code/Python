elephant = [1, 2, 3, 4, 5, "ultima","segmentum"]
print(elephant)
elephant.pop()
print(elephant)
print(type(elephant))
print(elephant[5][3])
print(elephant[5][3:7])

list2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list2d)
print(list(range(31)))
print(list(range(0, 31, 3)))


nicolas_cage = ({'name': 'Nicolas', 'surname': 'Cage', 'age': 55})

print(nicolas_cage['name'])
print(type(nicolas_cage))


K = [1,2,3]
L = K.copy()  #musime využit metodu copy, jinak by se L stalo odkazem na K
L.append(4)

print(K)
print(L)

c= 4
a=4

print(id(c)), print(id(a))

megatuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(megatuple)

aristotel= {"Alfa", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega"}
funny_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Delta"}

print(aristotel.union(funny_set))

print(aristotel.intersection(funny_set))
loremYpsum = frozenset(aristotel)

print(loremYpsum)

vaha = int(input("Zadej svou vahu v kg: "))
if vaha >100:
    print("ty tlustý prase")
else:
    print("ty hubený prase")


for x in range(10):
    print(f"ahojky po {x} krát")