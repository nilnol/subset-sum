import sys
sys.setrecursionlimit(2**16)

from bisect import bisect

import math

# Implements the search version of subset sum.
# The subset sum problem: given a set and a number find a subset of the set which sums to the given number.
# Inputs: an ordered list of integers xs, and an integer n which is the target sum.
def subset_sum_search(xs, n):
#    print(n, xs)
    if n < sum(filter(lambda x: x < 0, xs)):
        return []
    if n > sum(filter(lambda x: x >= 0, xs)):
        return []
    for k in range(0, len(xs) + 1):
        x = n + 2**(k) - 1
        y = 1
        while y < x:
            z = (x + y) >> 1
            t = []
            for m in [n + x, n + y, n + z]:
                while m > 0:
                    i = int(math.floor(math.log(m)/math.log(2)))
                    m -= 2**i
                    if i < len(xs):
                        t.append(xs[i])
                        if sum(t) > n:
                            t.pop()
                    if sum(t) == n:
                        return t
            if sum(t) < n:
                y = z + 1
            else:
                x = z
    return []

# Decision version, using the search version.    
def subset_sum(xs, n):
    return sum(subset_sum_search(xs, n)) == n

import math
# Optimization version, using the decision version.
# Source for optimization version algorithm:
# https://courses.cs.washington.edu/courses/csep521/05sp/lectures/sss.pdf
def subset_sum_optim(xs, n):
    t = xs[:]
    for i in range(math.floor(math.log(n)/math.log(2)), -1, -1):
        t.insert(bisect(t, 2**i), 2**i)
    for i in range(math.floor(math.log(n)/math.log(2)), -1, -1):
        t.remove(2**i)
        if not subset_sum(t, n):
            n -= 2**i
    return n

# Testing, testing...
tests = {}

import random

l = []
for _ in range(100):
	l += [random.choice(range(1, 8193))]

l.sort()

i = set()
while len(i) < 30:
    i = i.union(set([random.choice(range(len(l)))]))

i = list(i)
i.sort()
tests[1] = (l, sum([l[x] for x in i]))

tests_to_run = [1]

for i in tests_to_run:
#    print("i =", i)
    a, b = tests[i]
    r = subset_sum_search(a, b)
#    r = subset_sum(a, b)
    print(r, len(r), sum(r), b)
#    print()
#    print(i, r)
"""
# Additionally, check every subset of a set.
S = [2,3,5,7,17,19,23,41]
def a(xs, i):
    xs = xs[:]
    rs = []
    while i > 0:
        x = xs.pop(0)
        if i % 2 == 1:
            rs += [x]
        i >>= 1
    return rs

for i in range(1, 2**len(S)):
    X = subset_sum_search(S, sum(a(S, i)))
    print(sum(a(S, i)), X)
"""
