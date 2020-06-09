from collections import Counter


def print_perms(perm: list, options: list) -> None:
    if not options:
        print(perm)
    for i, item in enumerate(set(options)):
        new_options = options[:]
        new_options.remove(item)
        print_perms(perm+[item], new_options)
