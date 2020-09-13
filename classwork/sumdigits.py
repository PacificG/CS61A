import trace

def split(n):
    return n//10, n % 10

def sum_digits(n):
    """
    returns sum of digits of a number

    >>> sum_digits(52)
    7
    >>> sum_digits(1234)
    10
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last


def luhn_sum(n):
    """
    >>> luhn_sum(2221001234123450)
    40
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2*last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit


def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

def reverseCascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

def play_alice(n):
    if n == 0:
        print('bob wins!')
    else:
        play_bob(n-1)

def play_bob(n):
    if n  == 0:
        print('alice wins!')
    elif n % 10 == 0:
        play_alice(n-2)
    else:
        play_alice(n-1)


def fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i += 1

def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def condition(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return condition

def print_delayed(x):
    """Return a new function. This new function, when called,
    will print out x and return another function with the same
    behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    """
    def delay_print(y):
        print(x)
        
        return print_delayed(y)
    return delay_print

    
def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    """
    def inner_print(x):
        if n == 0:
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print


def parabola(x):
    """A parabola function (for testing the again function)."""
    return (x-3) * (x-6)
def vee(x):
    """A V-shaped function (for testing the again function)."""
    return abs(x-2)
def again(f):
    """Return the smallest non-negative integer n such that f(n) == f(m) for some m < n.
    >>> again(parabola) # parabola(4) == parabola(5)
    5
    >>> again(vee) # vee(1) == vee(3)
    3
    """
    n = 1
    while True:
        m = 0
        while m < n:
            if f(n) == f(m):
                return n
            else:
                m += 1
        n += 1

def ramp(n):
    """Return whether non-negative integer N has more increases than decreases.
    >>> ramp(123) # 2 increases (1 -> 2, 2 -> 3) and 0 decreases
    True
    >>> ramp(1315) # 2 increases (1 -> 3, 1 -> 5) and 1 decrease (3 -> 1)
    True
    >>> ramp(176) # 1 increase (1 -> 7) and 1 decrease (7 -> 6)
    False
    >>> ramp(5) # 0 increases and 0 decreases
    False
    """
    n, last, tally = n//10 , n % 10 , 0
    while n:
        n, last, tally = n // 10, n % 10, tally + 1 if last > n % 10 else tally - 1
    return tally > 0

def over_under(y):
    """Return a function that takes X and returns:
    -1 if X is less than Y
    0 if X is equal to Y
    1 if X is greater than Y
    >>> over_under(5)(3) # 3 < 5
    -1
    >>> over_under(5)(5) # 5 == 5
    0
    >>> over_under(5)(7) # 7 > 5
    1
    """
    return lambda x: 0 if x == y else (-1 if x < y else 1)

def process(n, tally, result):
    """Process all pairs of adjacent digits in N using functions TALLY and RESULT."""
    while n >= 10:
        tally, result = tally(n % 100 // 10, n % 10)
        n = n // 10
    return result()

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def ups(k):
    """Return tally and result functions that compute whether N has exactly K increases.
    >>> f, g = ups(3)
    >>> process(1200849, f, g) # Exactly 3 increases: 1 -> 2, 0 -> 8, 4 -> 9
    True
    >>> process(94004, f, g) # 1 increase: 0 -> 4
    False
    >>> process(122333445, f, g) # 4 increases: 1 -> 2, 2 -> 3, 3 -> 4, 4 -> 5
    False
    >>> process(0, f, g) # 0 increases
    False
    """
    def f(left, right):
        return ups(min(k, k + sign(left - right)))
    return f , lambda : k == 0


# def at_most(n, k):
#     """Return whether non-negative integer N has at most K increases.
#     >>> at_most(567, 3)
#     True
#     >>> at_most(567, 2)
#     True
#     >>> at_most(567, 1)
#     False
#     """
#     result = k
#     while k >= 0:
#         a, b = ups(k)
#         k, result = k - 1,  
#     return result