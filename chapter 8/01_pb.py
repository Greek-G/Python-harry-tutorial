def max():
    a=int(input("enter a number :-"))
    b=int(input("enter b number :-"))
    c=int(input("enter c number :-"))
    if(a>b and a>c):
        return a
    if(b>a and b>c):
        return b
    if(c>b and c>a):
        return c
print(f'greates number is:-{max()}')