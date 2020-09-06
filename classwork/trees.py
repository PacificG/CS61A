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



    