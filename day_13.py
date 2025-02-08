# Strings are immutable
a = "!!!Harry!! !!!!!!!!! Harry!!!!!!!"
print(len(a))
print(a)
print(a.upper()) # doesnt change a but make a copy 
print(a.lower())
print(a.rstrip("!")) #remove the  ! at the end
print(a.replace("Harry", "John"))
print(a.split(" "))  # make a list of split strings
blogHeading = "introduction tO jS"
print(blogHeading.capitalize()) 
#uppercase the first letter then lowercase everything else

str1 = "Welcome to the Console!!!"
print(len(str1))
print(str1.center(50)) # shift to center
print(len(str1.center(50)))
print(a.count("Harry"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))    # return true false whether it ends with or not

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))    # endswith( "string",starting index, ending index )

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))    # returns -1 when not found
# print(str1.index("ishh")) # returns index but shows error when not found

str1 = "WelcomeToTheConsole00"
print(str1.isalnum())     # A-Z,a-z,0-9
str1 = "Welcome00"
print(str1.isalpha())     #A-Z,a-z

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())    
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is aN honest man."
print(str1.title())    # capitalize first letter of every word and rest lowercase