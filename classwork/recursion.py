def max_lst(lst):
    def helper(lst, max_till):
        if len(lst) == 0:
            return max_till
        elif lst[0] > max_till:
            max_till = lst[0]
            return helper(lst[1:],max_till)
        elif lst[0] <= max_till:
            return helper(lst[1:],max_till)
    return helper(lst, -999999)

def find_max(lst):
    if lst == []:
        return float('-inf')
    f = lst[0]
    r = find_max(lst[1:])
    if f > r:
        return f
    return r

def recursive_mul(m, n):
    if n == 1:
        return m
    else:
        return m + recursive_mul(m, n-1)

def is_prime(n):
    def helper(n, checked):
        if n == checked:
            return True
        elif n % checked == 0:
            return False
        return helper(n, checked + 1)
    return helper(n, 2)

"""
You want to go up a flight of stairs that has n steps. You can either take 1
or 2 steps each time. How many different ways can you go up this flight of
stairs? Write a function count_stair_ways that solves this problem. Assume
n is positive.
"""

def count_stair_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return count_stair_ways(n-1) + count_stair_ways(n-2)



# def count_k(n, k):
#     """
#     >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
#     4
#     >>> count_k(4, 4)
#     8
#     >>> count_k(10, 3)
#     274
#     >>> count_k(300, 1) # Only one step at a time
#     1
#     """
#     def helper(sum, n, k):
#         if k > n:
#             return 0
#         elif k == 1:
#             return 1
#         elif n == 1:
#             return 1
#         elif n==k:
#             return 1 + count_k(n, k-1) 
#         sum += count_k(n-1,k) + count_k(n-2,k)
#         return sum
#     return helper(0, n, k) + helper(0, n, k-1)


def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i]*i for i in range(len(s)) if i % 2 == 0]
        
        
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    >>> max_product([1,7,3])
    7
    """
    if s == []:
        return 1
    elif len(s) == 1:
        return s[0]
    elif len(s) == 2:
        return max(s[0],s[1])
    return max(s[0] * max_product(s[2:]),s[1]*max_product(s[3:]))

def check_hole_number(n):
    """
    A hole number is a number in which every other digit dips below the digits immediately adjacent to it.
    For example, the number 968 would be considered a hole number because the number 6 is smaller than
    both of its surrounding digits. Assume that we only pass in numbers that have an odd number of digits.
    Define the following function so that it properly identifies hole numbers.
    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    >>> check_hole_number(3245968)
    False
    """
    
    if ((n%1000)//10 - ((n%1000)//100)*10 > (n%1000)//100 and (n%1000)//10 - ((n%1000)//100)*10 > n%10) or ((n%1000)//10 - ((n%1000)//100)*10 < (n%1000)//100 and (n%1000)//10 - ((n%1000)//100)*10 < n%10):
        return check_hole_number(n//10) if n//100 != 0 else True
    return False
    


def check_mountain_number(n):
    """
    Define the following function so that it properly identifies mountain numbers. A mountain number is a
    number that either
    i. has digits that strictly decrease from right to left OR strictly increase from right to left
    ii. has digits that increase from right to left up to some point in the middle of the number (not necessarily
        the exact middle digit). After reaching the maximum digit, the digits to the left of the maximum
        digit should strictly decrease

    >>> check_mountain_number(103)
    False
    >>> check_mountain_number(153)
    True
    >>> check_mountain_number(123456)
    True
    >>> check_mountain_number(2345986)
    True
    """
    def helper():
        if _________________________________________________________:
            return _________________________________________________________
        if _________________________________________________________:
            return _________________________________________________________
        return _________________________________________________________
#     return helper()