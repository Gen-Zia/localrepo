# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info) 
# print(info.keys())
# print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

# print(info.items())
# for key, value in info.items():
#   print(f"The value corresponding to the key {key} is {value}") 

ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

ep1.update(ep2)
print(ep1)

ep1.pop(670)    # specipic pair through key
print(ep1)

# ep1.clear()
# print(ep1)

ep1.popitem()    ## pop last pair
print(ep1)

del ep2[222]
print(ep2)