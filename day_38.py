# def func1():
#   try:
#     l = [1, 5, 6, 7]
#     i = int(input("Enter the index: "))
#     print(l[i])
#     return 1
#   except:
#     print("Some error occurred")
#     return 0

#   finally:
#     print("I am always executed")
#   # print("I am always executed")


# x = func1()
# print(x)



### task  :: --->>>


a = input("Enter any number between 5 and 9: ")

if a.lower() == "quit":  # Allow "quit" without an error
    print("Exiting...")
else:
    a = int(a)  # Convert input to integer if not "quit"
    if a > 9 or a < 5:
        raise ValueError("Input is not between 5 and 9.")
    else:
        print("Valid input:", a)
