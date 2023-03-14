from datetime import datetime

pattern = '%d.%m.%Y %H:%M'
suffixes = {
        1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2,
        11: 2, 12: 2, 13: 2, 14: 2, 0: 2,
    }

MINUTE = ('минута', 'минуты', 'минут')
HOUR = ('час', 'часа', 'часов')
DAY = ('день', 'дня', 'дней')


def choose_plural(amount, declensions):

    ind = suffixes.get(int(str(amount)[-2:]))
    if ind != None:
        return f'{amount} {declensions[ind]}'
    return f'{amount} {declensions[suffixes.get(int(str(amount)[-1]))]}'

release = datetime(year=2022, month=11, day=8, hour=12)
current_day = datetime.strptime(input(), pattern)

if current_day >= release:
    print('Курс уже вышел!')
else:
    rem = release - current_day
    tot = rem.total_seconds()
    if rem.days == 0:
        if rem.total_seconds() < 3600:
            print(f'До выхода курса осталось: {choose_plural(int(tot // 60), MINUTE)}')
        else:
            if tot // 60 % 60:
                print(f'До выхода курса осталось: {choose_plural(int(tot // 3600), HOUR)} и {choose_plural(int(tot // 60 % 60), MINUTE)}')
            else:
                print(
                    f'До выхода курса осталось: {choose_plural(int(tot // 3600), HOUR)}')
    else:
        if tot // 3600 % 24:
            print(f'До выхода курса осталось: {choose_plural(rem.days, DAY)} и {choose_plural(int(tot // 3600 % 24), HOUR)}')
        else:
            print(f'До выхода курса осталось: {choose_plural(rem.days, DAY)}')




