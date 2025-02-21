def convert(n):
    if(n==1 and n==0):
        return 
    else:
        return n*2.54
n=int(input("enter a number-"))
print(f" inches {n} into cm is {convert(n)}")
    