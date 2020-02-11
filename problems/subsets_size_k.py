# prints all subsets of size k
def n_choose_k(path_set, s, k):

    if (k == 1):
        for element in s:
            print(path_set + [element])
        return

    for i, _ in enumerate(s[:-(k - 1)]):
        n_choose_k(path_set + [s[i]], s[1 + i:], k - 1)


n_choose_k([], ['a', 'b', 'c', 'd', 'e'], 3)
