#the prefilled code will contain a list you need to concatenate given number to the list the first list should have the number concatenate at the beginning the second list should have the number concatenate at the ending
num_list =  [10, 20, 40, 100]
n = int(input())
first_list = [n]+num_list# Add the number in the beginning
second_list =num_list+[n] # Add the number at the end

print(first_list)
print(second_list)
