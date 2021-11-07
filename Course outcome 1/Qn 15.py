l1=["red","orange","blue","white","black"]
l2=["blue","black","orange","green","yellow"]
s1=set(l1)
s2=set(l2)
s=s1.difference(s2)
print("Colors in list 1 and not in list 2 : ")
print(list(s))