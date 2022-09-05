
# Write a code to get an integer N and 
# print the values from N to 1.

# Input Description:
# A single line contains an integer N.

# Output Description:
# Print the values from N to 1 in 
# a separate line.



def PrintReverse(n):
    for i in range(n,0,-1):
        
        print(i)
        
n=int(input())
PrintReverse(n)
#print(PrintReverse(n))



# Sample Input :
# 10
# Sample Output :
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1