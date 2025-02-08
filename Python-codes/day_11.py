name = "Harry"
friend = "Rohan"
anotherFriend = 'Lovish'

app= "i want to \"eat an apple\""  # if we want double quotation inside
# app = 'i want to "eat an apple"'  // this will work too

apple = '''He said, 
Hi Harry
hey I am good
"I want to eat an apple"'''  # '''''' for multiple lines
 
print("Hello, " + name)
print(app)
print(apple)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # Throws an error
print("Lets use a for loop\n")
for character in apple:
    print(character)