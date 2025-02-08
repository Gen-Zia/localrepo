import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

presenttime=time.strftime('%H')

if (int(presenttime)>6 and int(presenttime)<12):
    print("Good Morning")
elif(int(presenttime)>=12 and int(presenttime)<16):
    print("Good Noon")    
elif(int(presenttime)>16 and int(presenttime)<22):
    print ("Good Evening")
else:
    print("Good Night")