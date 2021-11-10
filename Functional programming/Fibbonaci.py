def fibo(nth):
    if nth == 0 or nth == 1:
        return nth
    else:
        return fibo(nth-1) + fibo(nth-2)
    
a = fibo(0)
b = fibo(1)
c = fibo(5)    
print('{}\n{}\n{}'.format(a,b,c))
