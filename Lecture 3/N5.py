from forex_python.bitcoin import BtcConverter
from datetime import datetime

'''
ყველა თარიღზე არ მუშაობს რაც ალბათ მოდულის ისტორიული მონაცემების ნაკლებობის ბრალია
კონკრეტული თარიღები რაც მუშაობს არის მაგალითად:
2017-4-27
2018-7-7
'''

purchase_year = int(input("Please enter year you purchased Bitcoin: "))
purchase_month = int(input("Please enter number of month you purchased Bitcoin: "))
purchase_day = int(input("Please enter day you purchased Bitcoin: "))
purchase_money = float(input("Please enter for how many dollars you purchased Bitcoin: "))

btc_converter = BtcConverter()

date_obj = datetime(purchase_year, purchase_month, purchase_day)
bitcoin = btc_converter.convert_to_btc_on(purchase_money, 'USD', date_obj)
value_now = float(btc_converter.convert_btc_to_cur(bitcoin, 'USD'))
difference = value_now - purchase_money

print("You have bought ", bitcoin, " bitcoin for ", purchase_money, " dollars on", date_obj)
print("The value of ", bitcoin, " bitcoin now is ", value_now)

if difference < 0:
    print("You have lost ", abs(difference), " dollars")
elif difference == 0:
    print("You have not win/lost anything")
elif difference > 0:
    print("You have won ", difference, " dollars")