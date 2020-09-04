def compute_trailing_zeros(n):

    # n factorial
    def compute_factorial(n):
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        return factorial

    factorial_str = str(compute_factorial(n))

    num_trailing_zeros = 0

    for i in range(len(factorial_str) - 1, -1, -1):
        if factorial_str[i] == '0':
            num_trailing_zeros += 1
        else:
            break

    return num_trailing_zeros


num_trailing_zeros = compute_trailing_zeros(5)

print(num_trailing_zeros)
