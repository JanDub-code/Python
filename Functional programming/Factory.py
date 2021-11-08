def factory():
    def add_num(n):
        return n + 5
    return add_num
a = factory()
print(a(5))
