a = "1"
# a = 1
b = "2"
# b = 2
print(int(a) + int(b)) # explicit typecasting

# Implicit TypeCasting
c = 1.9
d = 8

print(c + d)

'''
Python converts a smaller data type to a higher data type to prevent data loss.

'''

# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))