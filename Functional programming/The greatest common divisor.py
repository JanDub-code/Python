def gcd(num1, num2):
    r = num1 % num2
    if r == 0:
        return num2
    
    else:
        return gcd(num2, r)

print(gcd(33,22))
