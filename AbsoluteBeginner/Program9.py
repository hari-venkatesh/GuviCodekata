# You are given Two Numbers, A and B.
# If C = A + B. Find C.

# Note: Round off the output to a 
# single decimal place.

# Input Description:
# You are provided with two numbers A and B.

# Output Description:
# Find the sum of the two numbers (A + B)


a = float(input())
b = float(input())
c = a + b
res = "{:.1f}".format(c)
print(res)