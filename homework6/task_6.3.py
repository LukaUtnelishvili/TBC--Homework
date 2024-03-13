import random
your_number=int(input("Enter your number: "))
tries=1
max_tries=10
comp_number=random.randint(a=0,b=100)
while tries!=max_tries:
    if your_number<=0 or your_number>=100:
        your_number=int(input("Please enter number between 0 and 100: "))
    elif your_number<comp_number:
        your_number=int(input("HIGH: "))
    elif your_number>comp_number:
        your_number=int(input("LOW: "))
    tries+=1
if your_number==comp_number:
    print("You are winner")
elif tries==max_tries:
    print("Computer Is Winner")


