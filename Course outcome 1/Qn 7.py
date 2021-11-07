l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
#a
if len(l1)==len(l2):
    print("lists have same length")
else:
    print("No have same length")
#b
if sum(l1)==sum(l2):
    print("Lists have same sum")
else:
    print("Not have same sum")

#c
l3=[x for x in l1 if x in l2]
if len(l3)<1:
    print("No value occur in both")
else:
    print("common values are :",l3)

