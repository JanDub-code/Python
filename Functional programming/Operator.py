import operator as op
print(op.add(2,3))

print(op.mul(2,3))
#lambda x,y: x*y we can use operator instead of lambda

nums = [0, -1, -7, 2, 4, -8, 3, 8, -8, -10]
positive = list(map(op.abs,nums))
print(positive)







