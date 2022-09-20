
# Write a code to get an integer N and 
# print the sum of  values from 1 to N.

# Input Description:
# A single line contains an integer N.

# Output Description:
# Print the sum of values from 1 to N.



n=int(input())
output=0
for i in range(1,n+1):
    output +=i
   # output +="{}".format(i)
#output +="{}".format(sum(range(n+1)))
print(output)



# Sample Input :
# 10
# Sample Output :
# 55