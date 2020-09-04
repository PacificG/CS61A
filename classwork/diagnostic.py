def lens(prev = lambda x:0):
    """
    A lens store is a store that associates keys with values.
    
    To create a lens store, call the function 'lens', to get a put function.
    This function enables you to "put" a key-vlaue pair into the store, 
    and returns two functions 'get' and another 'put'.The 'get' function should
    let you look up a key and return its corresponding value, while the
    new 'put' function should let you continue adding on to the existing lens store.

    Note that you can assume that every key provided is unique. If you try to
    get the value for a key that does not exist, return 0.

    For details, refer to the doctest.

    >>> put1 = lens()
    >>> get2, put2 = put1('cat','animal')
    >>> get3, put3 = put2('table','furniture')
    >>> get4, put4 = put3('cup', 'utensil')
    >>> get5, put5 = put4('thesis','paper')
    >>> get5('thesis')
    'paper'
    >>> get5('cup')
    'utensil'
    >>> get5('table')
    'furniture'
    >>> get5('cat')
    'animal'
    >>> get3('cup')
    0
    """
    def put(k, v):
        def get(k2):
            if k2 == k:
                return v
            else:
                return prev(k2)
        return get, lens(get)
    return put



def storeroom(helium, fn_even, fn_odd):
    """
    Write a function 'storeroom' that takes a positive integer 'helium' and two functions 
    'fn_even' and 'fn_odd'.

    It applies 'fn_even' to all of the even digits in the integer and 
    applies 'fn_odd' to all of the odd digits in the integer. It then 
    returns whether the result of the even values is greater than the result of the odd
    values. You can guarantee that the number has at least one even and odd digit.

    >>> storeroom(1234, lambda x,y:x+y, lambda x,y:x*y) #4 + 2 > 3 * 1
    True
    >>> storeroom(11111111111112, lambda x, y: x+y, lambda x,y:x*y)
    True
    >>> storeroom(11111111111112, lambda x, y: x+y, lambda x,y:x + y)
    False
    >>> storeroom(12, lambda x,y:x+y, lambda x,y:x*y)
    True
    >>> storeroom(12345, lambda x,y:x+y, lambda x,y:x*y)
    False
    >>> storeroom(18383, lambda x,y:x-y, lambda x,y: x-y)
    True
    """

    evens_defined, odds_defined = False, False
    evens, odds = None, None
    while helium > 0:
        digit, helium = helium % 10, helium // 10
        if digit % 2 == 0:
            if evens is None:
                evens = digit
            else:
                evens = fn_even(evens, digit)
        else:
            if odds is None:
                odds = digit
            else:
                odds = fn_odd(odds, digit)
    return evens > odds
        
