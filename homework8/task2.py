user_input= input("please enter text: ")
xmovani="AaEeIiOoUu"
for i in range (0,len(user_input)):
    if not user_input[i] in xmovani: 
        print(user_input[i],end="")
print()
