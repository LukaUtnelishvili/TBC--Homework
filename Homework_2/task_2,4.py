_car_speed = int(input("Enter car speed "))
if _car_speed < 30:
    print("SLOW")
elif _car_speed > 120:
    print("VERY FAST")
elif _car_speed > 60:
    print("FAST")
elif _car_speed > 30:
    print("MODERATE")
else:
    print("FALSE")
