from functools import reduce
l1 = [1, 2, 3, 4, 5]
sum_l1 = reduce(lambda x,y: x+y, l1)
print(sum_l1)


n = int(input('Zadej cislo: '))

fac = reduce(lambda x,y: x*y, range(1, n+1))
print(fac)