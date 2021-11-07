#a
l1=[1,4,2,6,-4,-3,-9]
l2=[x for x in l1 if x>0]
print(l2)
#b
l=int(input("Enter the limit : "))
print([x*x for x in range(l+1)])
#c
w=input("Enter a word : ")
v=["A","E","I","O","U","a","e","i","o","u"]
l=[x for x in w if x in v ]
print(l)
#d
w=input("Enter a word : ")
l=[ord(x) for x in w]
print(l)