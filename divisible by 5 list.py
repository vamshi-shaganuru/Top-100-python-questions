#given a number N,write a program that reads N number and prints a list of numbers that 
n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l=l+[a]
k=[]
for j in l:
    if j%5==0:
        k=k+[j]
print(k)

"""
n=int(input())
b=[]
for i in range(n):
    a=int(input())
    if a%5==0 :
        b=b+[a]
print(b)
"""
