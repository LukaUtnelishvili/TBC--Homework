n=int(input("Enter the number: "))
if n<=0 or n>=10:
  print("Please enter the number between 0 and 10")
else:
  a=1
  while a<=n:
     b=1
     while b<=a:
        print(b, end=' ')
        b+=1
     print()
     a+=1
  a-=2
  while a>=1:
     b=1
     while b<=a:
        print(b, end=' ')
        b+=1
     print()
     a-=1
  
  