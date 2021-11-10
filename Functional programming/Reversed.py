def reverse(seq):
    if len(seq)==1:
        return seq
        
    return [seq[-1]] + reverse(seq[:-1])

l = [0, 1, 2, 3, 4, 5, 6, 7]
print(reverse(l))