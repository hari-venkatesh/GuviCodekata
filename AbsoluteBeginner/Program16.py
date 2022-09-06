
# Write a code to get an integer N and 
# print the even values from 1 till N 
# in a separate line.

# Input Description:
# A single line contains an integer N.

# Output Description:
# Print the even values from 1 to N 
# in a separate line.


i=int(input())
lst=range(1,i+2)
for i in lst:
    if i % 2==0:
        print(i,end="\n")




# Sample Input :
# 6
# Sample Output :
# 2
# 4
# 6