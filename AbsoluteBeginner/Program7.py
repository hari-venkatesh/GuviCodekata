# Print the First 3 multiples of the 
# given number "N". 
# (N is a positive integer)

# Note: print the characters with 
# a single space between them.

# Input Description:
# A positive integer is provided to you 
# as an input.

# Output Description:
# Print the First 3 multiples of the number 
# with single spaces between them as an output.



def mult(m, n):
    a = range(n, (m * n)+1, n)
    print(*a)
n = int(input())
m = 3
mult(m, n)