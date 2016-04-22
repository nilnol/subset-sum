import math
import random


# Implements the decision version of subset sum.
# The subset sum problem: given a set and a number find a subset of the set which sums to the given number.
# Inputs: an ordered list of integers xs, and an integer n which is the target sum.
def subset_sum(xs, n):
    r = set([(n, len(xs))])
    while len(r) > 0:
        n, k = r.pop()
        if n in xs[:k]:
            return True
        m = 0
        for i in range(k):
            m += xs[i]
            if m == n:
                return True
            if m > n:
                r.add((m - n, i))
    return False


# Search version, using the decision version.
def subset_sum_search(xs, n):
    if subset_sum(xs, n):
        r = []
        while n > 0 and len(xs) > 0:
            s = xs[-1]
            xs = xs[:-1]
            if not subset_sum(xs, n):
                r.append(s)
                n -= s
        return r
    return []


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
    while len(i) < 3:
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
tests[10] = ([40101858, 76322755, 136159283, 199307000, 236806451, 257503966, 378814688, 383257677, 452055324, 542791427, 562331475, 617971320, 638557181, 656754240, 702696128, 777063735, 802892554, 912963912, 915430670, 973647658, 1070795584, 1117969828, 1155206382, 1156767057, 1180975063, 1232044790, 1314374206, 1409329005, 1411407234, 1455313086, 1463876477, 1526335168, 1528588894, 1609964402, 1628016485, 1714392503, 1727417767, 1754979404, 1818412096, 1905552710, 1939472553, 2028752538, 2110815980, 2115652496, 2119964746, 2124490852, 2134336748, 2161208058, 2164795184, 2333102864, 2351325317, 2354598172, 2372550310, 2476975047, 2492125088, 2524822753, 2565233554, 2586038210, 2649293494, 2660074193, 2663665003, 2715274977, 2844690230, 2877483690, 2910856563, 2988563655, 3024241538, 3079918753, 3094523023, 3120329400, 3132845030, 3134747920, 3169341355, 3182099989, 3261204927, 3274641117, 3334842750, 3352770217, 3410678702, 3500147856, 3543880373, 3548280943, 3550260305, 3554893043, 3726448240, 3752332634, 3769464662, 3775973858, 3884338877, 3903915987, 3935095948, 3945429985, 3973252645, 4080309119, 4115991971, 4147147299, 4173134257, 4182881211, 4242111357, 4267824074], 6257963279, [42, 95])
tests[11] = ([48906186, 66024487, 95604669, 100998714, 158291358, 168721094, 270502893, 412017392, 447279918, 482366253, 535901678, 564962570, 634308664, 691107936, 822368619, 872499243, 875706733, 951988851, 981474962, 1026401771, 1039488404, 1047898977, 1081434249, 1123450125, 1145897065, 1194611615, 1205236320, 1243510849, 1277796220, 1424260241, 1605294823, 1636483491, 1688607068, 1702581806, 1723973540, 1736928390, 1776373463, 1781289297, 1794191832, 1836507577, 1879976024, 1907761658, 1918020774, 1920393554, 1985815147, 2020899727, 2078837627, 2100655729, 2104132739, 2178385315, 2207407770, 2230214517, 2236874802, 2376607851, 2445534196, 2523179648, 2553547084, 2604817872, 2605322833, 2639480049, 2660642014, 2750258146, 2776615832, 2801875866, 2808696612, 2836018582, 2898005714, 2920493054, 3005605964, 3027876104, 3297475865, 3306473175, 3309225458, 3323966671, 3333127002, 3439798909, 3444443694, 3461037127, 3478273983, 3483118233, 3509723718, 3543469813, 3548829506, 3635866226, 3713650379, 3718215082, 3730128877, 3742194853, 3753471760, 3781551343, 3901011813, 3931836558, 3933810677, 4025493027, 4150543218, 4170723959, 4188972557, 4190335278, 4239050321, 4272960608], 2225673005, [11, 12, 19])
tests[12] = ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37], 32, [5, 7])
tests[13] = ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37], 100, [])
tests[14] = ([2, 3, 5, 7, 11, 13], 40, [])
tests[15] = ([2, 3, 5, 7, 11, 13], 21, [])
tests[16] = ([2, 3, 5, 7, 11, 13], 34, [])
tests[17] = ([2, 3, 5, 7, 11, 13], 23, [])
tests[18] = ([2, 3, 5, 7, 11, 13], 25, [])
tests[19] = ([2, 3, 5, 7, 11, 13], 37, [])
tests[20] = ([2, 3, 5, 7, 11, 13], 38, [])
tests[21] = ([2, 3, 5, 7, 11, 13], 35, [])
tests[22] = ([1, 2, 3, 4, 5, 6], 15, [0, 1, 2, 3, 4])
tests[23] = ([2,3,5,7,17,19,23,41], 37, [0,2,3,6])
tests[24] = ([2,3,5,7,17,19,23,41], 39, [])
tests[25] = ([2,3,5,7,17,19,23,41], 45, [])
tests[26] = ([32824321, 232228894, 313529596, 337243275, 345002652, 508635306, 526206869, 535860848, 561813837, 575885766, 691872100, 692900639, 742587643, 774411266, 781591881, 797410010, 822097146, 843029096, 950279292, 951844589, 980103859, 1009000736, 1071951092, 1087455133, 1273945952, 1284960006, 1297330075, 1334683958, 1348475188, 1353766826, 1362156940, 1454138714, 1466430019, 1537213589, 1548911313, 1681694992, 1696010711, 1699471991, 1745645219, 1745981255, 1809977183, 1843211537, 1941856525, 1942998955, 1952411795, 1978758238, 2035551695, 2080603797, 2125246240, 2137083892, 2164489791, 2195692780, 2218754996, 2232693470, 2506322852, 2534580849, 2544821681, 2558942275, 2568411247, 2597518020, 2604407433, 2665395771, 2691535965, 2702251465, 2754815638, 2767000823, 2767765518, 2781562311, 2796768408, 2798456908, 2807657247, 2810277864, 2934921674, 3014782608, 3082627468, 3137182170, 3185202851, 3217513361, 3350522492, 3424529023, 3449942172, 3515377297, 3563979878, 3579592646, 3638569179, 3746195129, 3761013390, 3808186532, 3887547609, 4011601107, 4041896785, 4051739376, 4071322746, 4088701551, 4105689956, 4111937669, 4126371098, 4166165815, 4180103240, 4201664658], 7018413836, [34, 55, 72])


tests_to_run = []


for i in tests_to_run:
    a, b, c = tests[i]
#    r = subset_sum_search(a, b)
#    print(r, len(r), sum(r), b)
#    if r != [] and sum(r) != b:
#        print(a, b, c, [a[i] for i in c])
#    print("n", b)
    print(i, subset_sum(a, b))


# Additionally, check every subset of a set.
S = [2,3,5,7,17,19,23,41]
#S, _, _ = tests[26]
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
    if sum(X) != sum(a(S, i)):
        print(X, len(X), sum(X), sum(a(S, i)))


