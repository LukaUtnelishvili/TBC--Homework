import math
import random

n = int(input("enter number, which is greater than one: "))
if n <= 0:
   n = input("please enter nuber more than 1")

counter = 0
for i in range(0,n):
   a = random.random()
   b= random.random()
   if math.sqrt(a ** 2+ b ** 2) <= 1:
      counter+=1

c = 4 * counter / n
print("output is", c)

#shedegi uaxloveba pi-s n zrdastan ertad

