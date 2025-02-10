n=int(input("enter number:-"))
for i in range(2,n):
    if(n%i==0):
        print("number is not prime")
        break
    else:
        print("prime")