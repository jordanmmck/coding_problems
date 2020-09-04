import random
import math


def rand_set(n_set, m):
    res = set([])
    while m:
        ind = math.floor(random.random()*len(n_set))
        res.add(n_set[ind])
        del n_set[ind]
        m -= 1

    return res


print(rand_set([1, 2, 3, 4, 5, 6, 7], 4))
