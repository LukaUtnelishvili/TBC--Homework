a=input("enter text: ")
a=a.lower()
a=a.replace(" ","")
if not a.isalpha():
   a=""
if a[::]==a[::-1]:
    print("Output: Is palindrome")
else:
    print("Output: Is not palindrome")
   
   