n=int(input("Enter number: "))
if n<0 or n>=10000:
    print("Please enter number from 0 to 10000")
else:
    reversed_num = 0
    sum_of_digits = 0
    
    while n != 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        sum_of_digits += digit
        n //= 10
    print("reversed number is:", reversed_num)
    print("sum of digits:", sum_of_digits)

  