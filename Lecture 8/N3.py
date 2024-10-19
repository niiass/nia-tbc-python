from datetime import datetime

date_str = input("Enter the date: ")

date_str = date_str[:-3] + date_str[-2:]
print(date_str)

dt_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f%z')
changed = dt_obj.strftime('%d-%m-%Y %I:%M:%S %z')
changed = changed[:-4] + changed[-3]

print(changed)