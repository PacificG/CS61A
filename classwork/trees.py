def tree(label, branches = []):
    """
    tree constructor
    branches can be empty
    """
    for branch in branches:
        assert is_tree(branch) # checks if each branch of the tree is itself a tree
    return [label] + list(branches) # returns a tree with label and its branches inside a list
 
def label(tree):
    """
    Returns the label or root of a tree
    """ 
    return tree[0]

def branches(tree):
    """
    returns the branches list
    """
    return tree[1:]

def is_tree(tree):
    """
    checks if a tree is valid or not
    """
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """
    checks if tree has just one node
    """
    return not branches(tree)


"""
Tree processing
"""

#Fibonacci

def fib_tree(n):
    if n == 1 or n == 0:
        return tree(n)
    else:
        left, right = fib_tree(n-2) , fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n,[left, right])

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)


def partition_tree(n, m):
    if n == 0:
        return tree(True)
    elif m == 0 or n < 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])

def print_partition(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_partition(left, partition + [m])
        print_partition(right, partition)

def leaves(tree):
    """
    Returns a leaf containing leaf labels of the tree
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        left, right = branches(tree)
        return leaves(left) + leaves(right)
        
def print_tree(tree, indent=0):
    print(" "*indent + str(label(tree)))
    for b in branches(tree):
        print_tree(b, indent + 1)


def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    return 1 + max([height(b) for b in branches(t)])


def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ... [tree(2,
    ... [tree(3),
    ... tree(4)]),
    ... tree(5,
    ... [tree(6,
    ... [tree(7)]),
    ... tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
     4
      9
      16
     25
      36
       49
      64
    """
    if is_leaf(t):
        return tree(label(t)**2)
    return tree(label(t)**2, [square_tree(b) for b in branches(t)])
    

"""
Write a function that takes in a tree and a value x and returns a list containing the
nodes along the path required to get from the root of the tree to a node containing
x.
If x is not present in the tree, return None. Assume that the entries of the tree are
unique.

"""
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    path = []
    def helper(tree, x):
        if is_leaf(tree):
            return [x] if label(tree) == x else None
        elif label(tree) == x:
            return [x]
        else:
            return [label(tree)] + [helper(b, x) for b in branches(tree)]
            



    helper(tree,x)
    print(path)


def primary_stress(t):
    """
    The study of stress is still an open field of inquiry in linguistics—why do we say
    “alaBAma,” but “aLAbama” and “alabaMA” make us cringe? Or how did it come
    to be that “AMERICAN history professor” and “american HISTORY professor”
    mean two different things? One model that we use to understand stress actually
    employs the tree data structure!
    In the above diagrams, every node has a “strong” child and a “weak” child, and
    primary stress is placed on the leaf that has the greatest number of strong parents.
    In the spirit of computational linguistics, let’s write a function that, given one of
    these tree structures, identifies the stressed part of a word or phrase.1
    >>> word = tree("", [tree("w", [tree("s", [tree("min")]), tree("w", [tree("ne")])]),tree("s", [tree("s", [tree("so")]), tree("w", [tree("ta")])])])
    >>> primary_stress(word)
    'so'
    >>> phrase = tree("", [tree("s", [tree("s", [tree("law")]), tree("w", [tree("degree")])]),tree("w", [tree("requirement")])])
    >>> primary_stress(phrase)
    'law'
    """
    def helper(t, num_s):
        if is_leaf(t):
            return [label(t), num_s]
        if label(t) == "s":
            num_s = num_s + 1
        return max([helper(b, num_s) for b in branches(t)], key = lambda k: k[1])
    return helper(t, 0)[0]

