def square(n):
  # docstring must be after the definition of function otherwise it will be comment
  '''Takes in a number n, returns the square of n'''  # this is not ignored by compiler
  print(n**2)
  
square(5)
print(square.__doc__)