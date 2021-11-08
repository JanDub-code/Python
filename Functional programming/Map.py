#function map takes two arguments
l1 = [1, 2, 3, 4, 5]
r = len(l1)
for i in range(r):
    l1[i] += 1
print(l1)

l2 = [1, 2, 3, 4, 5]
l2 = map(lambda x: x+1, l2)
print(list(l2))

def double(x):
    return x*2
m = map(double, range(5))
l1 = list(m)
print(l1)

def sum_two(a,b):
    return a+b
l1 = [1,2,3,4]
l2 = [5,6,7]
m = map(sum_two, l1, l2)
print(list(m))

l1 = [1,2,3,4]
m = map(lambda x: x+1, l1)
print(list(m))


#same thing differently written
def add_one(x):
    return x+1
m = list(map(add_one,[1, 2, 3, 4, 5]))
print(m)

def add_one(x):
    return x+1
l1 = [1, 2, 3, 4, 5]
l_result = []
for i in l1:
    l_result.append(add_one(i))
print(l_result)
