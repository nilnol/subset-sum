from bisect import bisect

import math
import random

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
        x = 2**(k) - 1
        y = 0
        while y < x:
            z = (x + y) >> 1
            for m in [x, y, z, n + x, n + y, n + z]:
                t = []
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

# Random problem instances.
def random_instance():
    l = []
    for _ in range(100):
	    l += [random.choice(range(1, 2**32+1))]
    l.sort()
    i = set()
    while len(i) < 2:
        i = i.union(set([random.choice(range(len(l)))]))
    i = list(i)
    i.sort()
    return (l, sum([l[x] for x in i]), i)

tests[1] = random_instance()
tests[2] = ([1020221313, 1293990373, 2127926062, 2985361753], 5299573439, [0, 1, 3])
tests[3] = ([744097932, 1590558985, 2120522889, 3505328389, 3873774801, 4054577474, 4161356330, 4209525027], 5839985306, [0, 1, 3])
tests[4] = ([458262832, 1078103327, 2519418529, 2999253778, 3141965406, 3283914473, 3546000499, 3773363538], 4535619937, [0, 1, 3])
tests[5] = ([1599630241, 1723245963, 2307011281, 2788586661, 3128856274, 3509778615, 3997000705, 4291342017], 6832654819, [0, 1, 5])
tests[6] = ([1066581269, 1275497322, 1381518571, 1703547994, 2148293079, 2473030227, 3415424847, 3877558961], 5243159490, [0, 3, 5])
tests[7] = ([2105978660, 2261010504, 2363269791, 3045943040, 3377167548, 3714220319, 4155142877, 4235929112], 7670223335, [1, 2, 3])
tests[8] = ([10379150, 43258760, 69027197, 217282553, 220851198, 325227631, 424842193, 438165614, 508892338, 526082435, 596455225, 645145317, 699321708, 705708628, 713680920, 841836193, 881484043, 889420343, 901292364, 949114711, 1046711482, 1080975077, 1096402082, 1129995609, 1209396184, 1263542905, 1316606387, 1365564517, 1383667269, 1395526325, 1418078289, 1423007848, 1427457453, 1431208392, 1455687518, 1463261982, 1508061378, 1511362295, 1571969349, 1607157185, 1628557423, 1735069321, 1772900457, 1842391011, 1844715537, 1880760237, 1932926175, 1963597709, 2001262161, 2012062034, 2048509182, 2073201926, 2170809724, 2197251067, 2226422708, 2305932332, 2306263793, 2340529323, 2415629516, 2507046332, 2520235012, 2577192551, 2686437660, 2726727690, 2744800712, 2796117745, 2820063647, 2833068584, 2910410869, 2918395979, 2922801845, 2985742177, 3036199312, 3279780212, 3373101750, 3416822459, 3418414405, 3427306086, 3456422704, 3547001325, 3579706595, 3725139755, 3736889371, 3737062827, 3738334947, 3741382484, 3756267335, 3894083219, 3902360976, 3912324018, 3940141318, 3945863918, 3955446269, 4003328716, 4027716225, 4081285777, 4095839682, 4116801639, 4128451053, 4214392525], 5349770737, [34, 87])
tests[9] = ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37], 36, [0, 1, 2])

tests_to_run = [2, 3, 4, 5, 6, 7, 8, 9]
"""
while True:
    a, b, c = random_instance()
    r = subset_sum_search(a, b)
    if sum(r) != b:
        print(a, b, c, [a[i] for i in c])
        break
"""
for i in tests_to_run:
    a, b, c = tests[i]
    r = subset_sum_search(a, b)
    print(r, len(r), sum(r), b)
    if sum(r) != b:
        print(a, b, c, [a[i] for i in c])

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
    print(X, len(X), sum(X), sum(a(S, i)))

