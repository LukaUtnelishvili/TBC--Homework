a = int(input("Enter the number "))
if a == 2 or a == 4  or a == 8 :
    print("2.", "explanation:", int(a),"is divided by 2. 2 is a prime number")
elif a == 3 or a == 9:
    print("3.", "explanation:", int(a), "is divided by 3. 3 is a prime number ")
elif a == 5:
    print("5. explanation:", int(a)," is divided by 5.", "5 is a prime number")
elif a == 7:
    print("7, explanation: 7 is divided by 7. 7 is a prime number ")    
elif a == 6:
    print("2 , 3.explanation: 6 is divided by 2 and 3. 2 and 3 are prime numbers")
elif a == 10:
    print("2 , 5. explanation : 10 is divided by 2 and  5. 2 and 5 are prime numbers")    
else :
    print("false")