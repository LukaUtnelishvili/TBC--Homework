row1 = "qwertyuiop"
row2 = "asdfghjkl"
row3 = "zxcvbnm"

action = input("Enter action (e/d): ")
if action != "e" and action != "d":
	print("Enter correct action")
	exit(1)
	
user_input = input("Enter text: ")
user_input=user_input.lower()
if action=="e":
	change=1
else:
	change=-1

for i in range (len(user_input)):
	if user_input[i] in row1:
		row = row1
	elif user_input[i] in row2:
		row = row2
	elif user_input[i] in row3:
		row = row3
	else:
		print(user_input[i], end = "")
		continue
	index = -1
	for j in range(len(row)):
		if user_input[i] == row[j]:
			index = j
			break
	index = (index + change) % len(row)
	print(row[index], end = "")
print()

	   