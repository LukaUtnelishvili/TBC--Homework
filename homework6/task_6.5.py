n=int(input("Enter the number: "))
if n<=0 or n>=10:
  print("Please enter the number between 0 and 10")
else:
  a=0
  while a<=n:
     print("  "* (n-a), end=" ")
     b=a
     while b>=0:
        print(b,end=' ')
        b-=1
     b=1
     while b<=a:
        print(b,end=" ")
        b+=1
     print()
     a+=1


