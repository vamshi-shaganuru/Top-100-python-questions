#write a program to print N inputs and list containing the first and last three inputs
n=int(input())
l=[]
for i in range(n):
    string=input()
    l=l+[string]
new=l[:3]+l[n-3:]
print(new)

# n=int(input())
# b=[]
# for i in range(1,n+1):
#     a=input()
#     if i<=3 or i>(n-3):
#         b=b+[a]
# print(b)