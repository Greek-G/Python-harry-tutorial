a=int(input("enter number:-"))
for i in range(2,a):
    if(a%i)==0:
        print("not")
        break
else:
    print("prime")