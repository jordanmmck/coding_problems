# prints all subsets of size k
def subsets_size_k(subset: list, options: list, k: int) -> None:
    if k == 1:
        for option in options:
            print(subset + [option])

    for i in range(len(options[:-(k - 1)])):
        subsets_size_k(subset+[options[i]], options[i+1:], k-1)


subsets_size_k([], ['A', 'B', 'C', 'D', 'E'], 3)
