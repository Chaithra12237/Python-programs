a=int(input("Enter the final year : "))
b=int(input("Enter the current year : "))
print("Future leap years are : ")
while (b<=a):
    if b % 100==0:
        if b % 400==0:
            print(b)
    elif b % 4==0:
        print(b)
    b+=1