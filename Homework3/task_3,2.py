import datetime
y = int(input("Enter your birth year "))
m = int(input("Enter your birth month "))
d = int(input("Enter your birth day "))
birthday = datetime.date(y, m, d)
datetime.date.today
birthday_day = birthday.strftime("%A")
print("You was born on", birthday_day)


