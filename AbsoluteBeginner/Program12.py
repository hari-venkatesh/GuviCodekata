
# You are provided with a number, "N". 
# Find its factorial.

# Input Description:
# A positive integer is provided as an input.

# Output Description:
# Print the factorial of the integer.


a = int(input())
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
        
r = factorial(a)
print(r)