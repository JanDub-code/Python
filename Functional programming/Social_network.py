friendships = [('A','B'),
               ('B','C'),
               ('A','C'),
               ('C','D'),
               ('B','F'),
               ('D','E'),
               ('F','E'),
               ('F','J'),
               ('E','H'),
               ('E','G'),
               ('G','H'),
               ('H','I'),
               ('I','J'),
               ('I','L'),
               ('L','M'),
               ('M','N'),
               ('N','O')]

def get_friends(node, network):
    res = filter(lambda x: x, map(lambda pair: pair[int(not pair.index(node))] if node in pair else '', network) )
    return set(res)

def in_common(node1, node2, network):
    return get_friends(node1, network) & get_friends(node2, network)

def are_friends(node1, node2, network):
    return node2 in get_friends(node1, network) or node1 in get_friends(node2, network)

print(are_friends('A','I',friendships))
print(in_common('B','O',friendships))
print(get_friends('A',friendships))