def print_subsets(s: list) -> None:
    n = len(s)
    for i in range(2**n):
        bits = list(f'{i:0b}')
        bits = ['0']*(n-len(bits)) + bits
        print([s[j] for j in range(n) if bits[j] == '1'])


print_subsets(['A', 'B', 'C', 'D', 'E', 'F'])
