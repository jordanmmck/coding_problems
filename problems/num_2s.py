def num_2s(n):
    count = 0
    for i in range(1, n+1):
        s = str(i)
        count += s.count('2')

    return count


x = num_2s(20)
