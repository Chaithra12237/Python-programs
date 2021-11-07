upper=int(input("Enter the upper limit="))
lower=int(input("Enter the lower limit="))
l=[]
l1=[]
for x in range(lower, upper + 1):
    if x % 2 == 0:
        l.append(x)
for y in l:
    for z in range(1,y):
          if (z*z) ==y:
             l1.append(y)
print(l1)