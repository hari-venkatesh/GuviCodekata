# You will be provided with a number. 
# Print the number of days in the 
# month corresponding to that number.

# Note: In case the input is February, 
# print 28 days. If the Input is not in 
# valid range print "Error".

a = int(input())
list = [1,3,5,7,8,10,12]
list2 = [4,6,9,11]
if a in list:
    print("31")
if a in list2:
    print("30")
if a==2:
    print("28")
else:
    print("Error")