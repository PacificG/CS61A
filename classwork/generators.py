def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)
    
def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])

# Write a generator function generate_subsets that returns all subsets of the positive
# integers from 1 to n. Each call to this generator’s next method will return a list of
# subsets of the set [1, 2, ..., n], where n is the number of previous calls to next.
def generate_subsets():
    """
    >>> subsets = generate_subsets()
    >>> for _ in range(3):
    ...     print(next(subsets))
    
    [[]]
    [[], [1]]
    [[], [1], [2], [1, 2]]
    """

    def gen(n):
        return [[]] + list(substrings(list(range(1, n+1))))
    n = 0
    while True:
        yield gen(n)
        n += 1

