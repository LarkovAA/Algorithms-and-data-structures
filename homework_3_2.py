# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
import random

class Index_even_lements:
    def __init__(self):
        self.list_num = [random.randint(1, 100) for _ in range(15)]
        self.list_even_num = []

    def search_even(self):
        it = 0
        for i in self.list_num:
            if i % 2 == 0:
                self.list_even_num.append(it)
            it += 1
        print(f'Инддексы четных чиссел в масиве {self.list_num} являются {self.list_even_num}')

ind_eve = Index_even_lements()
ind_eve.search_even()

