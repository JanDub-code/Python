def func(x):
    return x**2

print(func(4))

lambda x: x**2

names = ['Bob','Nick', 'Ann', 'Johnny', 'Elisabeth']
res = max(names, key = lambda x: len(x))
print(res)

res1 = sorted('Good News Today', key= lambda x: x.upper())
res2 = sorted('Good News Today')
print(res1)
print(res2)

#we can save nameless function lambda
add_two = lambda x: x + 2
print(add_two(2))

