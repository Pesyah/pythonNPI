"""
6. Написать функцию, которая принимает два объекта
datetime и возвращает число по модулю дней между ними
"""
import datetime
import random

def foo(first_date, second_date):
    dif = str(abs(first_date - second_date))
    dif = dif[0:dif.index('days')]
    return f'разница дней - {dif}'
    
f_date = datetime.date(random.randrange(2010, 2025), random.randrange(1, 12), random.randrange(1, 28))
s_date = datetime.date(random.randrange(2010, 2025), random.randrange(1, 12), random.randrange(1, 28))
print(f'первая дата - {f_date}, вторая дата - {s_date}\n')

print(foo(f_date, s_date))