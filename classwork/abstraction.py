"""
Abstraction for rational Numbers
"""
from math import gcd
# representation of data
def rational(n, d):
    s = gcd(n, d)
    def select(pick):
        if pick == 'n':
            return n//s
        elif pick == 'd':
            return d//s
    return select

def numer(x):
    return x('n')

def denom(x):
    return x('d')

# function of data

def print_rational(x):
    print("{}/{}".format(numer(x),denom(x)))

def add_rationals(x, y):
    nx, ny = numer(x), numer(y)
    dx, dy = denom(x), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    return rational(numer(x)*numer(y),denom(x)*denom(y))

def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


"""
Pair representation using higher order functions
"""

def pair(x, y):
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
        else:
            return "Out of index"
    return get

# lot = pair(3,4)
# lot(1)

def select(p, i):
    return p(i)

def divisors(n):
    """
    Returns list of divisors of n
    """
    return [1] + [x for x in range(2,n) if n % x == 0]

curry = lambda f: lambda x: lambda y: f(x, y)




