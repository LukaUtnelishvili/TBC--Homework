user_input= input("please enter text: ")
i = 0
while i<len(user_input):
    if len(user_input) % 2==0:
        if  i==len(user_input)//2: 
            print((user_input[i-1]+user_input[i])*5,end="")
        elif i==0 or i==len(user_input)-1:
            print(user_input[i]*5,end="")
    else:
        if i==0 or i==len(user_input)//2 or i==len(user_input)-1:
            print(user_input[i]*5,end="")
    i+=1      


 