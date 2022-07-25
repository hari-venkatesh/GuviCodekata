# You are given three numbers A, B & C. Print the largest amongst these three numbers.

# Input Description:
# Three numbers are provided to you.

# Output Description:
# Find and print the largest among the three


n = int(input())
t = int(input())
y = int(input())

if (n >= t) and (n >= y):
    l = n
elif (t >= n) and (t >= y):
    l = t
else:
    l = y
print(l)