num=[]

n1=int(input("enter digt 1:-"))
num.append(n1)
n2=int(input("enter digt 2:-"))
num.append(n2)
n3=int(input("enter digt 3:-"))
num.append(n3)
n4=int(input("enter digt 4:-"))
num.append(n4)
print(num)
if(n1>n2 and n1>n3 and n1>n4):
    print(" number 1 is greates",n1)
elif(n2>n1 and n2>n3 and n2>n4):
    print(" number 1 is greates",n2)
elif(n3>n2 and n3>n1 and n3>n4):
    print(" number 1 is greates",n3)
else:
    print(" number 4 is greater",n4)