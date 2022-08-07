import datetime
import random
from random import randrange
from datetime import timedelta


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    ran_date = start + timedelta(seconds=random_second)
    day = list(str(ran_date.day))
    if len(day) == 1:
        day.insert(0, '0')
    month = list(str(ran_date.month))
    if len(month) == 1:
        month.insert(0, '0')
    return day, month


def num_generate():
    day, month = random_date(date_1, date_2)
    number = f'{day[0]}{random.randint(1000,9999)}{day[1]}{random.randint(1000,9999)}{month[0]}{random.randint(1000,9999)}{month[1]}'
    return number


date_1 = datetime.datetime.strptime('01/01', '%d/%m')
date_2 = datetime.datetime.strptime('31/12', '%d/%m')

with open('nums.txt', 'w', encoding='utf-8') as f:
    for i in range(1000):
        f.writelines(f'{num_generate()}\n')
