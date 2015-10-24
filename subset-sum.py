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
            m = n + z
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
tests[1] = ([2,3,5,7], 5)
tests[2] = ([2,3,5,7], 8)
tests[3] = ([2,3,5,7], 10)
tests[4] = ([2,3,3,3], 9)
tests[5] = ([2,3,5,7], 14)
tests[6] = ([2,3,5,7,11,13], 27)
tests[7] = ([2,3,5,7,11,13], 21)
tests[8] = ([2,3,5,7,11,13], 23)
tests[9] = ([2,3,5,7,11], 21)
tests[10] = (list(range(1, 257, 8)), 264)
tests[11] = (list(range(1, 257, 8)), 500)
tests[12] = (list(range(1, 1025, 8)), 771)
tests[13] = (list(range(1, 4097, 8)), 4471)
tests[14] = ([2,3,5], 6) # False
tests[32] = (list(range(1, 65537, 8)), 65525)
tests[33] = (list(range(1, 1025, 8)), 1023)
tests[34] = (list(range(1, 1025, 8)), 10231)
tests[35] = (list(range(-1025, 1025, 8)), 1023)
tests[36] = (list(range(2**16+1, 2**20+1, 8)), 2**18-1)
#tests[37] = (list(range(2**32+2**16+1, 2**32+2**24+1, 8)), 2**32+2**17+1+2**32+2**16+1+2**32+2**16+1+32)
#tests[37] = (list(range(2**32+2**16+1, 2**32+2**17+1, 8)), 2**32+2**17+1+2**32+2**16+1+2**32+2**16+1+32)
tests[37] = (list(range(2**128+2**16+1, 2**128+2**16+8*8192+1, 8)), 2**128+2**17+1+2**128+2**16+1+2**128+2**16+1+32)
tests[38] = ([2,3,5,7,11,13], 40)
tests[39] = ([2,3,5,7,11,13,17,19], 73)
tests[40] = ([2,3,5,7,11,13], 43)
tests[41] = ([2,3,5,7,11,13], 20)
tests[42] = ([2,3,5,7,11,13], 21)

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
tests[15] = (l, sum([l[x] for x in i]))

tests[16] = ([37,65,125,133,215,267,295,324,354,378,380,391,480,489,503], 1751)
tests[17] = ([37,65,125,133,215], 215+125)
tests[18] = ([36, 121, 138, 177, 236, 256, 262, 317, 365, 409, 433, 443, 498, 505, 511], 1256)
tests[19] = ([74, 164, 182, 205, 217, 248, 249, 261, 267, 282, 343, 353, 377, 453, 500], 1268)
tests[26] = ([2, 4, 8, 16], 17) # False
tests[27] = ([2, 3, 3, 5, 7, 11, 13], 37)

tests_to_run = [1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 16, 17, 18, 19, 26, 27]
#tests_to_run += [10, 11, 12, 13]
#tests_to_run = [14, 26, 2]
#tests_to_run = [33, 34]
#tests_to_run = [15]
#tests_to_run = [38, 39]
#tests_to_run = [40]
#tests_to_run = [3, 6]
#tests_to_run = [15]
#tests_to_run = [1, 2, 3, 10, 26, 27]
#tests_to_run = [10, 26, 27]
#tests_to_run += [41, 32, 37]
tests_to_run += [41, 42]
#tests_to_run = [2,4,5,14,18]
tests_to_run = [32]

for i in tests_to_run:
#    print("i =", i)
    a, b = tests[i]
    r = subset_sum_search(a, b)
#    r = subset_sum(a, b)
    print(r, len(r), sum(r), b)
#    print()
#    print(i, r)

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
"""
for i in range(1, 2**len(S)):
    X = subset_sum_search(S, sum(a(S, i)))
    print(sum(a(S, i)), X)
"""
