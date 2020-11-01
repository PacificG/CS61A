class Link:
    empty = ()
    def __init__(self, first, rest= empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)
    
    def __repr__(self):
        if self.rest:
            rest_str = ", " + repr(self.rest)
        else:
            rest_str = ""
        return 'Link({0}{1})'.format(self.first, rest_str)


    @property
    def second(self):
        return self.rest.first
    
    @second.setter
    def second(self, value):
        self.rest.first = value


def range_link(start, end):
        """
        >>> range_link(3,6)
        Link(3, Link(4, Link(5)))
        """
        if start >= end:
            return Link.empty
        else:
            return Link(start, range_link(start+1, end))
    
def map_link(f, s):
        """
        >>> map_link(lambda x: x**2, range_link(3,6))
        Link(9, Link(16, Link(25)))
        """
        if s is Link.empty:
            return s
        else:
            return Link(f(s.first), map_link(f, s.rest))


def filter_link(f, s):
        """
        filter_link(lambda x: x % 2 != 0, range_link(3,6))
        Link(3, Link(5))
        """
        if s is Link.empty:
            return s
        else:
            filtered_rest = filter_link(f, s.rest)
            if f(s.first):
                return Link(s.first, filtered_rest)
            else:
                return filtered_rest

def add_at_last(s, v):
    """
    Add v to a list s with no repeats, returning modified s.
    >>> add_at_last(map_link(lambda x: x**2, range_link(3,6)), 16)
    Link(9, Link(16, Link(25)))
    >>> add_at_last(map_link(lambda x: x**2, range_link(3,6)), 36)
    Link(9, Link(16, Link(25, Link(36))))
    """
    # if s.first != v and s.rest is Link.empty:
    #     s.rest = Link(v)
    # else:
    #     if s.first == v:
    #         pass
    #     else:
    #         add_at_last(s.rest, v)
    # return s

    #alternate
    assert s is not Link.empty
    if s.first != v and s.rest is Link.empty:
        s.rest = Link(v)
    else:
        if s.first ==  v:
            pass
        else:
            add_at_last(s.rest, v)
    return s


def add(s, v):
    """
    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(s, 6)
    Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))
    """
    assert s is not Link.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and s.rest is Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s
    
