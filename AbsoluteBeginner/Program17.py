
# You are provided with a number "N", 
# Find the Nth term of the 
# series: 1, 4, 9, 16, 25, 36, 49, 64, 81, .......

# (Print "Error" if N = negative value 
# and 0 if N = 0).

# Input Description:
# An integer N is provided to you as 
# the input.

# Output Description:
# Find the Nth term in the provided series.


n=int(input())
def term(n):
    ans=0
    for i in range(1,n+1):
        ans=i**2
    return ans
k= term(n)
print(k)


# Sample Input :
# 18
# Sample Output :
# 324