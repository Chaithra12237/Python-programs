l=[]
a=[]
for x in range(0,3):
    word=input("Enter the word : ")
    a.append(len(word))
    l.append(word)
print(l)
print("Length of longest word : ",max(a))