
from datetime import datetime
first_date=input("Input: ")
format= datetime.strptime(first_date, "%Y-%m-%dT%H:%M:%S.%f%z")
output_date =format.strftime("%d-%m-%Y %H:%M:%S %z")

print("Output:",output_date[:-4],output_date[-3])

