def rec(n):
    if n == 0 or n == 1:
        return n
    return rec(n - 1) + n
n=int(input("enter a number :-"))
print(f"sum of {n} is:-{rec(n)}")
