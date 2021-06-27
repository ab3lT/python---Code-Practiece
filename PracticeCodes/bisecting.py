from bisect import *


def index(a, x):
    # Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def find_lt(a, x):
    # Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError


def find_le(a, x):
    # Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError


def find_gt(a, x):
    # Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def find_ge(a, x):
    # Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect(breakpoints, score)
    return grades[i]


[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]

data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
print(data.sort(key=lambda r: r[1]))
keys = [r[1] for r in data]  # precomputed list of keys
print(data[bisect_left(keys, 0)])

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
for i in pairs:
    print(i)
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
