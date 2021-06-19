# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

class Exchange_max_min:
    def __init__(self):
        self.list_num = [random.randint(1, 100) for _ in range(15)]

    def exchange(self):
        print(f'Список до изменнений {self.list_num}')
        min_num = min(self.list_num)
        max_num = max(self.list_num)
        ind_min_num = self.list_num.index(min_num)
        ind_max_num = self.list_num.index(max_num)
        self.list_num[ind_min_num], self.list_num[ind_max_num] = self.list_num[ind_max_num], self.list_num[ind_min_num]
        print(f'Список после изменнений {self.list_num}')

exc = Exchange_max_min()
exc.exchange()