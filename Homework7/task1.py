n=int(input("Enter number: "))
if n<0 or n>=20:
    print("Please enter number from 0 to 20")
else:
    if n==0:
       print(0)
    else:
       place_in_list=0
       a=-1
       b=1
       c=0
       while place_in_list<n:
        c=a+b
        a+=b-a
        b+=c-b
        place_in_list+=1
        print(c,end=" ")
        
        