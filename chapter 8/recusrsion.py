def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n-1)

n = int(input("enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = fact(n)
    print(f"Factorial of {n} is: {result}")