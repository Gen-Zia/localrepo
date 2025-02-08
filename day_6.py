a = complex(8, 2)
b = True
c = "Harry"
d = None
print(a)
print(b)
a1 = 9
print(a + a1)
print("The type of a is ", type(a))
print("The type of b is ", type(b))
print("The type of c is ", type(c))

# list: A list is an ordered collection of data with elements separated by a comma 
# and enclosed within square brackets. Lists are mutable and can be modified after creation.

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

'''
Tuple: A tuple is an ordered collection of data with elements separated by a comma
and enclosed within parentheses. Tuples are immutable and can not be modified after creation.
'''

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

"""
dict: A dictionary is an unordered collection of data containing a key:value pair.
The key:value pairs are enclosed within curly brackets.
"""

dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)