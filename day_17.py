name = 'Abhishek'
for i in name:
  print(i)
  if(i =="b"):
    print("This is something special!")
    
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for i in color:    # nested loop
    print(i)

for k in range(5):  # start -default(0), end, step-default(1)
  print(k + 1)
  
# for k in range(1, 20001):
#   print(k)

  
for k in range(1, 12, 3):  # start , end+1, step
  print(k)