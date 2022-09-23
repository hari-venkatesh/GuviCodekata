
# Write a code get an integer number 
# as input and print the odd and 
# even digits of the number separately.

# Input Description:
# A single line containing an integer.

# Output Description:
# Print the even and odd integers of 
# the integer in a separate line.



mix = list(map(int, input()))
mix.sort()
def Split(mix):
    evlist = []
    odlist = []
    for i in mix:
        if (i % 2 == 0):
            evlist.append(i)
        else:
            odlist.append(i)
    print(*evlist)
    print(*odlist)

Split(mix)




# Sample Input :
# 1234
# Sample Output :
# 2 4
# 1 3