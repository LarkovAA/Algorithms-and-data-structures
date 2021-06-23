# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.

# Я взял из 2-ой домашки 9 задание

import random
import cProfile

def summ_number(number):
    '''
    Данная функция вычисляет сумму цифр из данного числа
    '''
    summ = 0
    number = str(number)
    for i in number:
        i = int(i)
        summ = i + summ
    return summ

class The_largest_numbers:
    '''
    Создаем класс в свойствах которого мы содержим число которое мы получаем при создании а так же 2 словаря.
    '''
    def __init__(self, num_int):
        self.num_int = num_int
        self.dic_num = {}
        self.final_dict = {}

    def generait_number(self):
        '''
        Данный метод класса случайно генерирует числа и записывает их в словарь с аналогичными значениями
        '''
        for _ in range(1, self.num_int + 1):
            gen_num = random.randint(1000, 9999)
            self.dic_num[gen_num] = gen_num

    def sum_of_digits(self):
        '''
        Данный метод вычисляет сумму цифр из полученых чисел.
        Так же по значению вычисляет эл-т словаря с наибольшим и записывает в список.
        '''
        for num in self.dic_num.keys():
            self.dic_num[num] = summ_number(self.dic_num[num])

        max_val = max(self.dic_num.values())
        self.final_dict = {k: v for k, v in self.dic_num.items() if v == max_val}
        list_dict = [self.final_dict.keys(), self.final_dict.values()]
        print(f'Максимальное число ={list_dict[0]} его сумма составляет {list_dict[1]}')


print('Работа с 10 данными')
test10 = The_largest_numbers(10)
cProfile.run('test10.generait_number()')
cProfile.run('test10.sum_of_digits()')

print('Работа с 100 данными')
test100 = The_largest_numbers(100)
cProfile.run('test100.generait_number()')
cProfile.run('test100.sum_of_digits()')

print('Работа с 1000 данными')
test1000 = The_largest_numbers(1000)
cProfile.run('test1000.generait_number()')
cProfile.run('test1000.sum_of_digits()')

print('Работа с 10000 данными')
test10000 = The_largest_numbers(1000)
cProfile.run('test10000.generait_number()')
cProfile.run('test10000.sum_of_digits()')

print('Работа с 100000 данными')
test100000 = The_largest_numbers(100000)
cProfile.run('test100000.generait_number()')
cProfile.run('test100000.sum_of_digits()')

print('Работа с 1000000 данными')
test1000000 = The_largest_numbers(1000000)
cProfile.run('test1000000.generait_number()')
cProfile.run('test1000000.sum_of_digits()')

print('Работа с 10000000 данными')
test10000000 = The_largest_numbers(10000000)
cProfile.run('test10000000.generait_number()')
cProfile.run('test10000000.sum_of_digits()')

# По результатам тестирования я выявил что Асимптотика O(N) линейная сложность