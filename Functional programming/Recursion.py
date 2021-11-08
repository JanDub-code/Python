def sum_rec(num):
    if num==0:
        return num
    return num + sum_rec(num-1)

print(sum_rec(2))