"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
квартала (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить
среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего.
"""


import collections as cs

QUARTER = 4

Organisation = cs.namedtuple('Organisation', 'org_name profit total')
org_list = []
org_count = int(input('Введите количество предприятий '))
full_profit = 0

for i in range(1, org_count + 1):
    name = input(f'Введите название {i}-го предприятия ')
    quarter_profit = []
    for quarter in range(1, QUARTER + 1):
        quarter_profit.append(int(input(f'Введите прибыль за {quarter}-й квартал ')))
    org_list.append(Organisation._make((name, quarter_profit, sum(quarter_profit))))
    full_profit += org_list[-1].total

avg = full_profit / org_count
org_upper, org_lower = [], []

for record in org_list:
    if sum(record.profit) > avg:
        org_upper.append(record.org_name)
    elif sum(record.profit) < avg:
        org_lower.append(record.org_name)

print(f'\nПрибыльные предприятия: ', *org_upper,
      f'Убыточные предприятия:', *org_lower, sep='\n')
