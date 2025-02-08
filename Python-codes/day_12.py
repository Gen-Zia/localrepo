fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4]) #  [ where to start , where to end +1 ]

print(fruit[1:4]) # including 1 but not 4

print(fruit[:5])  # default start from 0

print(fruit[0:])  # default ends at the last index of stringlen


#in case of negative index::

print(fruit[0:-3])
print(fruit[0:len(fruit)-3])  # negative means len()-index

print(fruit[-1:len(fruit) - 3]) # this means nothing as [4,2] means nothing
print(fruit[-3:-1])

for ln in fruit:
    print(ln)