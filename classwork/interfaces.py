class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

    def gen(self):
        yield self.first
        if isinstance(self.rest, Link): 
            yield from self.rest.gen()
        else:
            yield "Reached end of List"
        
        






"""
Write a function that takes in a a linked list and returns the sum of all its elements.
You may assume all elements in lnk are integers.
"""
def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    s = 0
    while lnk is not Link.empty:
        s += lnk.first
        lnk = lnk.rest
    return s

"""
Write a function that takes in a Python list of linked lists and multiplies them
element-wise. It should return a new linked list.
If not all of the Link objects are of equal length, return a linked list whose length is
that of the shortest linked list given. You may assume the Link objects are shallow
linked lists, and that lst of lnks contains at least one linked list.
"""
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    
   
    
    if Link.empty in lst_of_lnks:
        return Link.empty
    else:
        p = 1
        for i in lst_of_lnks:
            p *= i.first
        return Link(p, multiply_lnks([lnk.rest for lnk in lst_of_lnks]))

    
"""        
Implement filter link, which takes in a linked list link and a function f and
returns a generator which yields the values of link for which f returns True.
Try to implement this both using a while loop and without using any form of
iteration.
"""
def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest

def filter_no_iter(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> list(filter_no_iter(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    if link is Link.empty:
        return
    elif f(link.first):
        yield link.first
    yield from filter_no_iter(link.rest, f)


#Trees

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches
    def is_leaf(self):
        return not self.branches
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    

"""
Define a function make even which takes in a tree t whose values are integers, and
mutates the tree such that all the odd integers are increased by 1 and all the even
integers remain the same.
"""
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.is_leaf():
        if t.label % 2 != 0:
            t.label += 1
            return
    else:
        if t.label % 2 != 0:
            t.label += 1
        for b in t.branches:
            make_even(b)
            
"""
Define a function square tree(t) that squares every value in the non-empty tree
t. You can assume that every value is a number.
"""
def square_tree(t):
    """Mutates a Tree t by squaring all its elements.
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> square_tree(t)
    >>> t.label
    1
    >>> t.branches[0].branches[0].label
    9
    """
    if t.is_leaf():
        t.label = (t.label)**2
        return
    else:
        t.label = (t.label)**2
        for b in t.branches:
            square_tree(b)
        


"""
Define the procedure find path that, given a Tree t and an entry, returns a list
containing the nodes along the path required to get from the root of t to entry. If
entry is not present in t, return False.
Assume that the elements in t are unique. Find the path to an element.
For instance, for the following tree tree ex, find path should return:
https://inst.eecs.berkeley.edu/~cs61a/su20/disc/disc09.pdf  
2.3

"""
def find_path(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1)])
    >>> find_path(tree_ex, 5)
    [2, 7, 6, 5]
    """
    path = []
    def helper(t, entry, path):
        if t.is_leaf():
            if t.label == entry:
                path.append(t.label)  
            else:
                path = []
        elif t.label == entry:
            path.append(t.label)
        else:
            path.append(t.label)
            for b in t.branches:
                helper(b, entry, path)
    helper(t, entry, path)
    return path if entry in path else False


"""Assuming that every value in t is a number, define average(t), which returns the
average of all the values in t. You may not need to use all the provided lines.
"""
def average(t):
    """
    Returns the average value of all the nodes in t.
    >>> t0 = Tree(0, [Tree(1), Tree(2, [Tree(3)])])
    >>> average(t0)
    1.5
    >>> t1 = Tree(8, [t0, Tree(4)])
    >>> average(t1)
    3.0
    """
    def sum_helper(t):
        total, count = t.label, 1
        for b in t.branches:
            if b.is_leaf():
                total, count = (total + b.label, count + 1)
            else:
                t, c = sum_helper(b)
                total, count = total+ t, count + c
        return total, count
    total, count = sum_helper(t)
    return total / count


"""
Write a function that combines the values of two trees t1 and t2 together with the
combiner function. Assume that t1 and t2 have identical structure. This function
should return a new tree.
Hint: consider using the zip() function, which returns an iterator of tuples where
the first items of each iterable object passed in form the first tuple, the second items
are paired together and form the second tuple, and so on and so forth.
"""
def combine_tree(t1, t2, combiner):
    """
    >>> from operator import *
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    if t1.is_leaf():
        return Tree(combiner(t1.label, t2.label))
    else:
        return Tree(combiner(t1.label, t2.label), 
                    branches=[combine_tree(t1.branches[i], t2.branches[i], combiner) for i in range(len(t1.branches))])


"""Implement the alt tree map function that, given a function and a Tree, applies the
function to all of the data at every other level of the tree, starting at the root.
"""
def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """

    fn = map_fn
    def helper(t, map_fn):
        if not t:
            return
        t.label = map_fn(t.label)
        for b in t.branches:
            b.label = (lambda x:x)(b.label)
            for h in b.branches:
                helper(h, map_fn)
                
    helper(t, map_fn)
    print(repr(t))
    
