number=int(input("enter the number "))
if number <=0 or number>=1000:
    print("please enter number between 0  and 1000")
else:
  for i in range(1, number+1):
    if number % i ==0:
        print(i)




