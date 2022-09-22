
# Write a code get an integer number 
# as input and print the sum of the digits.

# Input Description:
# A single line containing an integer.

# Output Description:
# Print the sum of the digits of the integer.



n = int(input())
def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum
    
print(getSum(n))




# Sample Input :
# 124
# Sample Output :
# 7