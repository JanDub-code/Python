
def vynasob_cislo(n):
    
    def vynasob(x):
        return x*n
    return vynasob

print(vynasob_cislo(2)(3))

import math as m    

from math import sqrt as s

print(s(4))

import random

print(random.randint(1, 10))

import my_module as hehe

print(hehe.pozdrav())

from my_module import pozdrav

print(pozdrav())