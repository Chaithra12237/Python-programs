num=int(input("Enter the number : "))
print("Factors are : ")
for x in range(1,num+1):
    if num%x==0:
        print(x," ",end="")