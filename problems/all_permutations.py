def print_permutations(current: list, options: list) -> None:
    if not options:
        print(current)
    for i, item in enumerate(options):
        print_permutations(current+[item], options[:i]+options[i+1:])


print_permutations([], ['A', 'B', 'C', 'D', 'E'])
