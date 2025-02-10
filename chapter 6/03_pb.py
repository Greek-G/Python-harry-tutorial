p1="buy now"
p2="click this"

c=input("enter a comment:-")

if(( p1 in c) or (p2 in c)):
    print("enter comment is spam")

else:
    print("not spam")