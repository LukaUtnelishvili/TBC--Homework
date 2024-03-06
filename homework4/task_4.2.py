import random
n = int(input("Enter the number "))
if n<=0 or n>=30:
    print("please enter the number between 0 and 30")
random_numbers= [random.randint(a=0, b=1000)for i in range(n)]
max_number= max(random_numbers)
print(random_numbers)
print(max_number)




