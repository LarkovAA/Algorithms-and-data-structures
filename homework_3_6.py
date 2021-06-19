# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
import random

class Summ_element:
    def __init__(self):
        self.list_num = [random.randint(0, 100) for _ in range(20)]

    def search_summ(self):
        print(f'Список элементов {self.list_num}')
        num_min = min(self.list_num)
        num_max = max(self.list_num)
        ind_min = self.list_num.index(num_min)
        ind_max = self.list_num.index(num_max)
        if ind_min > ind_max:
            print(f'Сумма чисел между мак и мин числами = {sum(self.list_num[ind_max + 1:ind_min])}')
        else:
            print(f'Сумма чисел между мак и мин числами = {sum(self.list_num[ind_min + 1:ind_max])}')

sum_num = Summ_element()
sum_num.search_summ()