for a in range (1,10):
    for b in range(1,a+1):
        if a==b and int(a)!=int(b):
            break
        print(f"{b}*{a}={b*a}", end="\t ")
    print()

    