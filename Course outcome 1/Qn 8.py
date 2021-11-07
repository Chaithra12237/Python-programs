str=input("Enter a string : ")
c=str[0]
str=str.replace(str[0],"$")
print(c+str[1:])