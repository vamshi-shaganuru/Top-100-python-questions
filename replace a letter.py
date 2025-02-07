#program to read a word ,indexand a letter.print the word by replacing the letter at the index with the given letter
a=input()
b=int(input())
c=input()
d=a[:b]
e=a[b+1:]
print(d+c+e)