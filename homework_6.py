# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Python 3.8 Win64
import sys
import random
import cProfile
# Найти максимальный элемент среди минимальных элементов столбцов матрицы
class Matrix:
    def __init__(self, column, line):
        self.matrix = []
        self.num_column = column
        self.num_line = line

    def creating_matrix(self):
        for c in range(1, self.num_column+1):
            rows_matrix = []
            for l in range(1, self.num_line+1):
                num = random.randint(0, (self.num_column + self.num_line))
                #num = input(f'Введите значение элемента матрицы [{c}][{l}] ')
                rows_matrix.append(num)
            self.matrix.append(rows_matrix)
        for i in self.matrix:
            pass
            #print(f'{i}', sep='\n')

        print(f'{sys.getsizeof(self.matrix)} байтов занимает матрица {self.num_column} на {self.num_line}')

    def max_elem_min_cilumn(self):
        list_min = []
        for l in range(self.num_line):
            list_column_min = []
            for c in range(self.num_line):
                list_column_min.append(self.matrix[c][l])
                if c == self.num_line-1:
                    list_min.append(min(list_column_min))
        max_num = max(list_min)
        #print(f'Максимальный элемент среди минимальных элементов столбцов матрицы {max_num}')
        print(f'{sys.getsizeof(max_num)} байтов занимает максимальный элемент в списке')


# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.


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
        print(f'{sys.getsizeof(self.dic_num)} байтов занимает словарь сгенерированных значений ')

    def sum_of_digits(self):
        '''
        Данный метод вычисляет сумму цифр из полученых чисел   .
        Так же по значению вычисляет эл-т словаря с наибольшим и записывает в список.
        '''
        for num in self.dic_num.keys():
            self.dic_num[num] = summ_number(self.dic_num[num])

        max_val = max(self.dic_num.values())
        self.final_dict = {k: v for k, v in self.dic_num.items() if v == max_val}
        list_dict = [self.final_dict.keys(), self.final_dict.values()]
        #print(f'Максимальное число ={list_dict[0]} его сумма составляет {list_dict[1]}')
        print(f'{sys.getsizeof(list_dict)} байт занимает операция хранению в списке значения с наибольшей суммой чисел')

mat= Matrix(1000,1000)
max_creat_mat = mat.creating_matrix()
max_elem_min_cilum = mat.max_elem_min_cilumn()

print(f'{sys.getsizeof(mat)} байт занимает операция по созданию объекта ')
print(f'{sys.getsizeof(max_creat_mat)} байт занимает операция по созданию мартицы и внесении в нее элементов ')
print(f'{sys.getsizeof(mat)} байт занимает операция по созданию объекта ')
print(f'{sys.getsizeof(max_elem_min_cilum)} байт занимает операция по определению максимального значения минимальных элементов столбцов')

cProfile.run('mat.creating_matrix()')
cProfile.run('mat.max_elem_min_cilumn()')

print('Второй алгоритм')
max_num = The_largest_numbers(500000)
gen_num = max_num.generait_number()
sum_dig = max_num.sum_of_digits()

print(f'{sys.getsizeof(max_num)} байт занимает операция по созданию объекта')
print(f'{sys.getsizeof(gen_num)} байт занимает операция по генерации чисел ')
print(f'{sys.getsizeof(sum_dig)} байт занимает операция по определению суммы чисел')

cProfile.run('max_num.generait_number()')
cProfile.run('max_num.sum_of_digits()')


# Из рассмотренных 2-х алгоритмов мы можем сделать вывод что хранение 10 списков в списке с 10 элементами занимает меньше места чем хранение 50 элементов в словаре. Более чем в 10 рез.
# Так же хранение по 1элементу в списке 28 байтов занимает хранение максимального элемента в списке а 72 байт занимает операция хранению в списке значения с наибольшей суммой чисел.
# Из этого мы можем сделать вывод о том что хранение данных при ограниченных объемов памяти использовать списки. Преимущество словарей в быстроте их работы.
# Как видно по замерам скорости работы использовангие списков хотя и экономят память но при этом в 2-3 раза работает медленней чем алгоритмы с использованием словарей.


