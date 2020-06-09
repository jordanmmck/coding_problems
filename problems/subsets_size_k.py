# prints all subsets of size k
def n_choose_k(current, options, k):

    if (k == 1):
        for element in options:
            print(current + [element])
        return

    for i, _ in enumerate(options[:-(k - 1)]):
        n_choose_k(current + [options[i]], options[i+1:], k-1)

# prints all subsets of size k


# def n_choose_k(current, options, k):

#     if (k == 1):
#         for element in options:
#             print(current + [element])
#         return

#     for i, _ in enumerate(options[:-(k - 1)]):
#         n_choose_k(current + [options[i]], options[1 + i:], k - 1)


n_choose_k([], ['a', 'b', 'c', 'd', 'e'], 3)
