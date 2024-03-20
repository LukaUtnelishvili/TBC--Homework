user_input= input("please enter text: ")

for i in range(0,len(user_input)):
    if i %2 ==0 and user_input[i]!="e":
       print(user_input[i],end="")
print()

