#  В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

class Negative_number:
    def __init__(self):
        self.list_num = [random.randint(0, 99) - 100 for _ in range(20)]

    def search_max_neg(self):
        print(f'Список отрицательных чисел {self.list_num}')
        max_neg = max(self.list_num)
        index_max_neg_num = self.list_num.index(max_neg)
        print(f'Максимальное отрицательное число {max_neg} его индекс в списке {index_max_neg_num}')

max_neg_num = Negative_number()
max_neg_num.search_max_neg()