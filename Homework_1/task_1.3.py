import math
a=int(input("Enter length of first side of the triangle, a: "))
b=int(input("Enter lenght of second side of the triangle, b: "))
c=int(input("Enter lenght of third side of the triangle, c: "))
s=(a+b+c)/2
print("Area of the triangle is ", math.sqrt(s*(s-a)*(s-b)*(s-c)))
print("Perimeter of the triangle is", a+b+c)
