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