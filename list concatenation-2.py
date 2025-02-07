#a list is given in the prefilled code.given a number N.write a program that reads N inputsand prints the list by adding given N inputs at the end of the list
L = ["apple", "78", "970.03"]

# Write your code here
n=int(input())
for i in range(n):
    a=input()
    L=L+[a]
print(L)