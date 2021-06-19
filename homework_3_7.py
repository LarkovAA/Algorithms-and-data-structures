# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

class Two_mins:
    def __init__(self):
        self.list_num = [random.randint(0, 100) for _ in range(20)]

    def search_two_mins(self):
        print(f'Список {self.list_num}')
        min1 = min(self.list_num)
        if self.list_num.count(min1) > 1:
            min2 = min1
        else:
            self.list_num.remove(min1)
            min2 = min(self.list_num)
        print(f'Первые минимальное число = {min1} второе минимальное число = {min2}')

min_2 = Two_mins()
min_2.search_two_mins()