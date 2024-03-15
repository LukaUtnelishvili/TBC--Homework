n=int(input("Enter number: "))
if n<=0 or n>1000:
    print("Please enter number from 1 up to 1000")
elif n!=1:
     print(n,end="->")
     while n>1:
        if n % 2==0:
            n-=n/2
            print(int(n), end="->")
        elif n % 2 !=0:
            n=n*3+1
            print(int(n), end="->")
else:
    print(n, end="->")
    while True:
        z=n*3+1
        print(int(z), end="->")
        while z%2==0:
            z-=z/2
            print(int(z), end="->")
        exit()
    
