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