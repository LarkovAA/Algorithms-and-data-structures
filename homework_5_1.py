#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

import collections

num_bis = int(input('введите колличество предприятий: '))
bisness = collections.defaultdict(list)
for _ in range(num_bis):
    name_bis = str(input('Введите название предприятия? '))
    bisness[name_bis] = [i for i in input('Введите значение прибыли предприятия за 4 квартала ? ').split()]

# Создаем список в котором запишем все значения прибыли каждой компании
list_average_profit = []

# В цикле записываем данные прибыли
for k, t in bisness.items():
    num_ave = 0
    for num in t:
        num = int(num)
        num_ave += num
    list_average_profit.append(num_ave)
    bisness[k] = num_ave

# Вычисляем среднее значение прибыли
num_ave = (sum(list_average_profit) / len(list_average_profit))

# Создаем списки куда войдут компании с прибылью юольшей средней или меньше средней прибыли
big_num_ave = []
litle_num_ave = []

# В цикле определяем к какому списку будут относиться компании
for k in bisness.keys():
    if bisness[k] >= num_ave:
        big_num_ave.append(k)
    else:
        litle_num_ave.append(k)

print(f'Данные организации имеют прибыль выше средней {big_num_ave}')
print(f'Данные организации имеют прибыль ниже средней {litle_num_ave}')