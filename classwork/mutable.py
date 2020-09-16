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

# def partition_options(total, biggest):
#     """
#     Implement the following function partition_options which outputs all the ways to partition a number
# total using numbers no larger than biggest.
#     >>> partition_options(2, 2)
#     [[2], [1, 1]]
#     >>> partition_options(3, 3)
#     [[3], [2, 1], [1, 1, 1]]
#     >>> partition_options(4, 3)
#     [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]


#     """
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


def memory(n):
    """
    Write a function that takes in a number n and returns a one-argument function.
    The returned function takes in a function that is used to update n. It should return
    the updated n.
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f(fn):
        nonlocal n
        n = fn(n)
        return n
    return f

def nonlocalist():
    """
    Write a function that takes in no arguments and returns two functions, prepend and
    get, which represent the “add to front of list” and “get the ith item” operations,
    respectively. Do not use any python built-in data structures like lists or dictionaries.
    You do not necessarily need to use all the lines.
    >>> prepend, get = nonlocalist()
    >>> prepend(2)
    >>> prepend(3)
    >>> prepend(4)
    >>> get(0)
    4
    >>> get(1)
    3
    >>> get(2)
    2
    >>> prepend(8)
    >>> get(2)
    3
    """
    get = lambda x: "Index out of range!"
    def prepend(value):
        nonlocal get
        f = ___________________________________________________
        def get(i):
            if i == 0:
                return value
            return ___________________(_______________________)
        _______________________________________________________
    return prepend, get


f = lambda x: [print(i) for i in range(1,x+1)]

def memory(x, f):
    """Implement the memory function, which takes a number x and a single
    argument function f. It returns a function with a peculiar behavior that you must
    discover from the doctests. You may only use names and call expressions in your
    solution. You may not write numbers or use features of Python not yet covered in
    the course.
    >>> square = lambda x: x * x
    >>> double = lambda x: 2 * x

    Return a higher-order function that prints its
    memories.
    >>> f = memory(3, lambda x: x)
    >>> f = f(square)
    3
    >>> f = f(double)
    9
    >>> f = f(print)
    6
    >>> f = f(square)
    3
    None
    """
    def g(h):
        print(f(x))
        return memory(x, h)
    return g


def announce_losses(who, last_score=0):
    """
    It’s Hog again! Write a commentary function announce losses that takes in a player
    who and returns a commentary function that announces whenever that player loses
    points.
    >>> f = announce_losses(0)
    >>> f1 = f(10, 0)
    >>> f2 = f1(1, 10) # Player 0 loses points due to swine swap
    Oh no! Player 0 just lost 9 point(s).
    >>> f3 = f2(7, 10)
    >>> f4 = f3(7, 11) # Should not announce when player 0's score does not change
    >>> f5 = f4(11, 12)
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    def say(score0, score1):
        if who == 0:
            score = score0
        elif who == 1:
            score = score1
        if score < last_score:
            print("Oh no! Player {} just lost {} point(s).".format(who, last_score - score))
        return announce_losses(who, score)
    return say


def fox_says(start, middle, end, num):
    """
    The CS 61A staff has developed a formula for determining what a fox
    might say. Given three strings—a start, a middle, and an end—a fox will say the
    start string, followed by the middle string repeated a number of times, followed by
    the end string. These parts are all separated by single hyphens.
    Complete the definition of fox says, which takes the three string parts of the fox’s
    statement (start, middle, and end) and a positive integer num indicating how many
    times to repeat middle. It returns a string. You cannot use any for or while
    statements. Use recursion in repeat. Moreover, you cannot use string operations
    other than the + operator to concatenate strings together.
    >>> fox_says('wa', 'pa', 'pow', 3)
    'wa-pa-pa-pa-pow'
    >>> fox_says('fraka', 'kaka', 'kow', 4)
    'fraka-kaka-kaka-kaka-kaka-kow'
    """
    def repeat(k):
        if k == 1:
            return middle
        return middle + '-' + repeat(k-1)
    return start + '-' + repeat(num) + '-' + end

# def subset_sum(seq, k):
#     """
#     >>> subset_sum([2, 4, 7, 3], 5) # 2 + 3 = 5
#     True
#     >>> subset_sum([1, 9, 5, 7, 3], 2)
#     False
#     >>> subset_sum([1, 1, 5, -1], 3)
#     False
#     """
#     if len(seq) == 0:
#         return False
#     return 
