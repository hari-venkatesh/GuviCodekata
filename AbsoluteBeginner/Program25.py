
# You are given with a number A i.e. 
# the temperature in Celcius. 
# Write a program to convert this 
# into Fahrenheit. 

# Note: In case of decimal values, 
# round-off to two decimal places.

# Input Description:
# A number is provided in Celcius as 
# the input of the program.

# Output Description:
# The output shall be the temperature 
# converted into Fahrenheit corresponding 
# to the input value print up to 
# two decimal places and 
# round off if required.



c = float(input())
f = (c*1.8)+32
r="{:.2f}".format(f)
print(r)




# Sample Input :
# 12
# Sample Output :
# 53.60