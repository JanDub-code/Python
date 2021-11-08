def func1(arg1):
    e = 3
    def func2(arg2):
        l = 6
    return func2

def factory():
    const = 5
    def add_num(n):
        return n + const
    return add_num
f = factory()
print(f(5))

def factory():
    const = 5
    def add_num(n):
        return n + const
    return add_num
f = factory()
f_closure = f.__closure__
print(f_closure)

f_const = f_closure[0].cell_contents
print(f_const)


