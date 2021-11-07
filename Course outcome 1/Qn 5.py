l = []
l = [int(item) for item in input("Enter the list : ").split()]
print("The list is : ", l)
x = ["over" if x > 100 else x for x in l]
l = list(x)
print(l)