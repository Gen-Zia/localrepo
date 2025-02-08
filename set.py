s = {2, 4, 2, 6}
print(s)          # no duplicate values

info = {"Carla", 19, False, 5.9, 19}
print(info)        # no order 

# harry={}         # empty dictionary

harry = set()      # empty set 
print(type(harry))

for value in info:
  print(value)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)

# cities.update(cities2)
# print(cities)

cities4 = cities.intersection(cities2)
print(cities4)

# cities3 = cities.intersection(cities2)
# print(cities3)


cities5 = cities.symmetric_difference(cities2)  ## all of A and B except A intersection B
print(cities5)

# cities.symmetric_difference_update(cities2)
# print(cities)

cities6 = cities.difference(cities2)
print(cities6)


### Sets Methonds ::

print(cities.isdisjoint(cities2))

cit = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cit2 = {"Seoul", "Kabul"}
print(cities.issuperset(cit2))
cit3 = { "Madrid","Berlin"}
print(cit.issuperset(cit3))

print(cit2.issubset(cit))
print(cit3.issubset(cit))

cit3.add("Dhaka")
print(cit3)

cit.remove("Delhi")   # shows error if not found
print(cit)

cit.discard("Delhi")  # doesnt show error if not found
print(cit)

del cit2     # delete whole set
cit3.clear() # clear all element

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")