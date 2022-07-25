# You are given with Principle amount($), 
# Interest Rate(%) and 
# Time (years) in that order. 
# Find Simple Interest.

# Print the output up to two decimal places 
# (Round-off if necessary).

# (S.I. = P*T*R/100)

# Input Description:
# Three values are given to you as the input. 
# these values correspond to Principle amount, 
# Interest Rate and Time in that 
# particular order.

# Output Description:
# Find the Simple interest and 
# print it up to two decimal places. 
# Round off if required.

p,i,t = map(float, input().split())


si = (p * i *t)/100
print(round(si, 2))