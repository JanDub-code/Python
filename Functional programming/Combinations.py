def permutations(seq, n,*, repeat=False):
    if not n:
        return [[]]
    r = []
    for item in seq:
        left = seq if repeat else [i for i in seq if i!=item]
        for p in permutations(left,n-1,repeat=repeat):
            r.append([item]+p)  
    return r

def combinations(seq,n,*,repeat=False):
    if not n:
        return [[]]
    r = []
    for item in seq:
        left = seq if repeat else [i for i in seq if i!=item]
        
        for p in permutations(left,n-1,repeat=repeat):
        
            if sorted([item]+p) not in r:
                r.append([item]+p)  
    return r

c = combinations(['A','B','C','D'],2)
print(len(c))
print(*c,sep='\n')

c = combinations(['A','B','C','D'],2,repeat=True)
print(len(c))
print(*c,sep='\n')