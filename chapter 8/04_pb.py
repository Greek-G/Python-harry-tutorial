def rec(n):
    if n == 0 or n == 1:
        return n
    return rec(n - 1) + n

print(rec(4))
