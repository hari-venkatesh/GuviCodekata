
# Using the method of looping, 
# write a program to print the table of 9 
# till N in the format as follows:
# (N is input by the user)
# Guvi is the best

# 9 18 27...

# Print NULL if 0 is input

# Input Description:
# A positive integer is provided as an input.

# Output Description:
# Print the table of nine with single space between 
# the elements till the number that is input.


n = int(input())

count = 1
num = 9
k = 0
y = ""
while (count <= n):
    k += 1
    h = num * k

    if (count != 1):
        y += " " + str(num * k)
    else: 
        y += str(num * k)

    count += 1
        
print(y)


# Sample Input :
# 3
# Sample Output :
# 9 18 27