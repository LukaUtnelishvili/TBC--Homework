print("input:")
a=input("")
b=input("")
for aso in a: 
    if len(a)!=len(b) or a.count(aso)!=b.count(aso):
        print("Output: No")
        exit()
    else:
        print("Output: Yes")
        exit()

