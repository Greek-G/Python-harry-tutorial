roll=[]
r1=int(input("enter number 1:-"))
roll.append(r1)
r2=int(input("enter number 2:-"))
roll.append(r2)
r3=int(input("enter number 3:-"))
roll.append(r3)
r4=int(input("enter number 4:-"))
roll.append(r4)


c=int(input("enter number to find:-"))
if(c in roll):
    print("enter number is in list")
else:
    print("enter number is not present")