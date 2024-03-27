n = int(input("enter number, which is greater than one: "))
if n <= 0:
   n = input("please enter nuber more than 1")

x = 0
sign = 1
for i in range(1,n+1):
   x+= sign * 1 / (2 * i - 1)
   sign *= -1
x *= 4
print("x =",x)

# rac ufro izdreba n, x ufro miiswrafvis pi ricxvisken
