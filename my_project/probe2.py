from datetime import datetime, timedelta


pattern = '%H:%M'
start, stop = datetime.strptime(input(), pattern), datetime.strptime(input(), pattern)


while True:
    if stop > start:
        lesson = start + timedelta(minutes=45)
        if stop < lesson:
            break
        print(f'{start.strftime(pattern)} - {lesson.strftime(pattern)}')
        start += timedelta(minutes=55)

    else:
        break