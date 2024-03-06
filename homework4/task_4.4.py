n=int(input("Enter the number "))
if 0<=n<20:
   if n==0:
    print(0)
   elif n==1:
    print(1)
   else:
    c=[0,1]
    for i in range(2,n):
      c.append(c[-1]+c[-2])
      print(c)
      
else:
  print("enter number from 0 up to 19")

       