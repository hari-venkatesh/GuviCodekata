
# Write a code to get 2 integers as 
# input and find the HCF of the 2 
# integer without using recursion o
# r Euclidean algorithm.

# Input Description:
# A single line containing 2 
# integers separated by space.

# Output Description:
# Print the HCF of the integers.



a, b = map(int, input().split())

def Chcf(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i ==0)):
            hcf = i
    return hcf
    
print(Chcf(a, b))




# Sample Input :
# 2 3
# Sample Output :
# 1