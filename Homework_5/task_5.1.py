n=int(input("Enter the number: "))
if 0<n<50:
    for i in range(1,n+1):
     print(i, "-",end=" ")
     for j in range(1,i+1):
       if i % j ==0:
        print(j, end=' ')
        if j>=3:
          break
     print()
else:
  print("enter number between 0 and 50")
  

       
    
