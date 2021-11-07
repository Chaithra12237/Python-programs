n = int(input("Enter the limit : "))
n1, n2 = 0, 1
count = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence is : ")
   while count < n:
       print(n1)
       n3 = n1 + n2
       n1 = n2
       n2 = n3
       count += 1