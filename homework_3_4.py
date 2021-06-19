#\ Определить, какое число в массиве встречается чаще всего
import random

class Num_num:
    def __init__(self):
        self.list_num = [random.randint(1, 10) for _ in range(20)]
        self.dict_num = {}

    def calc_num(self):
        for num in self.list_num:
            if num not in self.dict_num.keys():
                self.dict_num[num] = 1
            else:
                self.dict_num[num] += 1
        print(f'В массиве {self.list_num} имеется следующее колличество чисел {self.dict_num}')

n_n = Num_num()
n_n.calc_num()