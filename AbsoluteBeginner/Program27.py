
# Let "A"  be a string. Remove all the 
# whitespaces and find it's length.

# Input Description:
# A string is provide as an input

# Output Description:
# Remove all the whitespaces and 
# then print the length of the 
# remaining string.



string = input()
def Remove(string):
    count = 0
    list = []
    
    for i in range(len(string)):
        if string[i] != ' ':
            list.append(string[i])
    
    return toString(list)
    
def toString(list):
    return ''.join(list)
    
m = len(Remove(string))
print(m)
    






# Sample Input :
# Lorem Ipsum
# Sample Output :
# 10