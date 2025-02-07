#write a program that reads a string S and checks if S in in the listprint TRUE if S is present in list or FALSE
L = ["5", "eat", "9.80", "Water", "python", "-678", "7685.26", "-2.5", "sing"]

# Write your code here
n=input()
is_present=False 
for i in L :
    if i==n :
        is_present=True 
        break 
print(is_present)
