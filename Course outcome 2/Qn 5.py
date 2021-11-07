n=int(input("Enter number of lines : "))
for a in range(1, n+1):
    for b in range(1, a+1):
        print(a*b, " ", end="")
    print()