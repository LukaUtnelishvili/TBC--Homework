import datetime
from forex_python.bitcoin import BtcConverter
y = int(input("Enter year "))
m = int(input("Enter month "))
d = int(input("Enter day "))
_price_ = float(input("price you paid for bitcoin in USD "))
if _price_ <0:
    print("price can not be less than 0")
_bought_date= datetime.date(y, m, d) 
current_date = datetime.datetime.now
b = BtcConverter()
bought_price = b.get_previous_price('USD', _bought_date)
current_price = b.get_latest_price('USD')
if bought_price is None:
    print("Bitcoin price data is not avaliable")
_amount = _price_ / bought_price
profit = current_price * _amount - bought_price * _amount
if profit >0:
    print("Your profit is", profit)
else:
    print("your loss is", profit)



