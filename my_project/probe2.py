from datetime import datetime, timedelta
current_day = input()
date1 = datetime.strptime(current_day, '%H:%M:%S')
print(date1)

