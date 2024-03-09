n = int(input("Enter the number: "))
_left="\\"
_right="/"
_middle="|"
if 0<n<50:
    for i in range(1,n+1):
        if i==1:
            print(" "*n,"*")
        else:
           print(" "*(n-i),_right*(i-1), _middle, _left*(i-1))
else:
    print("Please enter the number between 0 da 50")
if n+1:
    print(" "*n,"|")
print()


