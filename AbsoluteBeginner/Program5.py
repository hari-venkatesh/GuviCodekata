# The area of an equilateral triangle is ¼(√3a2) 
# where "a" represents a side of the triangle. 
# You are provided with the side "a". 
# Find the area of the equilateral triangle.

a = int(input())
area = (1.732050*a*a)/4
res = "{:.2f}".format(area)
print(res)