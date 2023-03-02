from datetime import date

def is_correct(day, mounth, year):
    try:
       date.fromisoformat(f'{year}-{mounth}-{day}')
    except:
        return 'Некорректная'
    return 'Корректная'

counter = 0
while True:
    try:
        day, mounth, year = input().split('.')
        check = is_correct(day=day, mounth=mounth, year=year)
        print(check)
        if check == 'Корректная':
            counter += 1
    except:
        print(counter)
        break




# 19.05.2016
# 05.13.2010
# 21.12.2012
# 01.01.1000
# 32.04.2003
# end








