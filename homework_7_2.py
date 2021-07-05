# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). ]
# Выведите на экран исходный и отсортированный массивы.
import random

class Sorted_number:
    '''
    Создаем класс в котором существуют следующие атрибуты: number -  колличесвто элементов в списке; list_number - сам список.
    '''
    def __init__(self, number):
        self.number = number
        self.list_number = []

    def creating_list(self):
        '''
        Данный метод генерирует список элементов.
        '''
        for _ in range(self.number):
            num = random.randint(0, 49)
            self.list_number.append(num)

    def sorted_list(self, list_num):
        '''
        Метод принимает в качестве параметра список значений и с помошью сортировки слияния производим сотрировку списка.
        '''
        if len(list_num) <= 1:
            return
        middle = len(list_num) // 2
        l = list_num[:middle]
        r = list_num[middle:]
        self.sorted_list(l)
        self.sorted_list(r)
        c = self.merge(l, r)
        for i in range(len(list_num)):
            list_num[i] = c[i]

        self.list_number = list_num

    def merge(self, a, b):
        '''
        Метод принимает в качестве параметров 2 списка из каждого списка мы берем по элементно равниваем значения.
        На выходе мы получаем новый список с частично отсортировонными значениями.
        '''
        c = [0] * (len(a) + len(b))
        i = k = n = 0
        while i < len(a) and k < len(b):
            if a[i] <= b[k]:
                c[n] = a[i]
                i += 1
                n += 1
            else:
                c[n] = b[k]
                k += 1
                n += 1
        while i < len(a):
            c[n] = a[i]
            i += 1
            n += 1
        while k < len(b):
            c[n] = b[k]
            k += 1
            n += 1
        return c


num = Sorted_number(15)
num.creating_list()
print(f'Получившийся список {num.list_number}')
num.sorted_list(num.list_number)
print(f'Получившийся отсортированый список {num.list_number}')