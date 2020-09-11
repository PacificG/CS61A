nest = (10,20,[30,40],50)
nest[2].pop()

"""Write a function that takes in a value x, a value el, and a list and adds as many
el’s to the end of the list as there are x’s. Make sure to modify the original
list using list mutation techniques."""
def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    
    lst.extend([el]*lst.count(x))

"""Write a function that takes in a sequence s and a function fn and returns a dictionary.
The values of the dictionary are lists of elements from s. Each element e in a list
should be constructed such that fn(e) is the same for all elements in that list.
Finally, the key for each value should be fn(e)."""
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    dic = {}
    for n in s:
        dic[fn(n)] = []
        
    for n in s:
        dic[fn(n)] += [n]

    return dic

def partition_options(total, biggest):
    """
    Implement the following function partition_options which outputs all the ways to partition a number
total using numbers no larger than biggest.
    >>> partition_options(2, 2)
    [[2], [1, 1]]
    >>> partition_options(3, 3)
    [[3], [2, 1], [1, 1, 1]]
    >>> partition_options(4, 3)
    [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]


    """
    # if total == 0:
    #     return [0]
    # elif total < 0:
    #     return []
    # else:
    #     with_biggest = partition_options(total - biggest, biggest)
    #     without_biggest = partition_options(total, biggest - 1)
    #     ____________ = [[_________]______________________________]
    #     return with_biggest + without_biggest

def make_withdraw(balance):
    def withdraw(bal):
        nonlocal balance
        if bal<= balance:
            balance -= bal
        else:
            print('Insufficient funds')
        return balance

    return withdraw