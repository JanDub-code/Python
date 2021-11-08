
def vowel(c):
    if c in 'aeiouy':
        return c
    else:
        return ''
f = filter(vowel, 'abcdefghijk')
print(list(f))


res = []

for i in 'abcdefghijk':
    if vowel(i):
        res.append(i)

print(res)