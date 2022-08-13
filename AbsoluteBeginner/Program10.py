# You are provided with the radius 
# of a circle "A". Find the length 
# of its circumference.

# Note: In case the output is coming 
# in decimal, roundoff to 2nd decimal place. 
# In case the input is a negative number, 
# print "Error".

# Input Description:
# The Radius of a circle is provided as 
# the input of the program.

# Output Description:
# Calculate and print the Circumference of 
# the circle corresponding to the input 
# radius up to two decimal places.


from math import pi
a = float(input())
m = (pi * a *2)
o = "{:.2f}".format(m)
print(o)