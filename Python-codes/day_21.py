def average1(a=3, b=2, c=1):
  print("The average is ", (a + b + c) / 3)


def average(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)

c = average(5, 6, 7, 1)
print(c)

average1(4, 6)
average1(b=9)

def pri(*n):
  for i in n:
    print(i)

pri("Nafiz",2137,3.75)    