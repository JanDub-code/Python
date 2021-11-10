#permutation with and without repetition of elements
def permutations(seq, n):
    if not n:
        return [[]]
    r = []
    for item in seq:
        for p in permutations([i for i in seq if i!=item],n-1):
            r.append([item]+p)  
    return r

p = permutations(['A','B','C','D'],4)
print(len(p))
print(*p,sep='\n')

def permutations(seq, n,*, repeat=False):
    if not n:
        return [[]]
    r = []
    for item in seq:
        left = seq if repeat else [i for i in seq if i!=item]
        for p in permutations(left,n-1,repeat=repeat):
            r.append([item]+p)  
    return r

p = permutations(['a','b','c','d'],4,repeat=True)
print(len(p))
print(*p,sep='\n')