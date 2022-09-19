
# Write a code to get an integer N 
# and print values from 1 till N 
# in a separate line.

# Input Description:
# A single line contains an integer N.

# Output Description:
# Print the values from 1 to N in a 
# separate line.



n=int(input())
def Print(n):
    for i in range(1,n+1,+1):
        print(i)
        
Print(n)




# Sample Input :
# 5
# Sample Output :
# 1
# 2
# 3
# 4
# 5