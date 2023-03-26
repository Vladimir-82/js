from datetime import datetime


t = '01/11/2021 11:01'

print(type(datetime.strptime(t, '%d/%m/%Y %H:%M')))