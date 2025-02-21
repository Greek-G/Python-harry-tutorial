def table(n):
    if(n==1 and n==0):
        print("no table")
    else:
        for i in range(1,11):
            print(f"{n}*{i}={n*i}")
n=int(input("enter a number:-"))
print(table(n))