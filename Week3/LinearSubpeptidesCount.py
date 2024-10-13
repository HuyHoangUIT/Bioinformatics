def LinearSubpeptidesCount(n):
    m = n + 1
    s = 1
    for i in range (1, m):
        s += (m-i)
    return s

print(LinearSubpeptidesCount(24890))