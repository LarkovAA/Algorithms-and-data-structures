# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
import random

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

number = int(input('Введите количество сгенерируемых цифр '))

max_num = The_largest_numbers(number)
max_num.generait_number()
max_num.sum_of_digits()