password="tbilisi"
input_pass =input("pls enter password: ")
for tries in range(1,4):
    if tries!=3 and input_pass!=password:
        input_pass=input("inccorect password, pls try again: ")
    elif tries==3 and input_pass!=password:
        print("you are blocked")
if input_pass==password:
    print("hello")


