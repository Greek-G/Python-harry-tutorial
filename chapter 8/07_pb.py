def remove(n,word):
    for item in n:
        n.remove(word)
        return n
n=["harry","lalu","shubma"]
word=input("enter word want remove:-")
print(remove(n,word))