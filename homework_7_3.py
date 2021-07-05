#  Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
#  Найдите в массиве медиану.
#  Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
#  Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random

class Median_number:
    '''
    Создаем класс в котором существуют следующие атрибуты: number -  колличесвто элементов в списке; list_number - сам список.
    '''
    def __init__(self, number):
        self.number = 2 * number + 1
        self.list_number = []

    def creating_list(self):
        '''
        Данный метод генерирует список элементов.
        '''
        for _ in range(self.number):
            num = random.randint(0, self.number)
            self.list_number.append(num)

    def finding_median(self):
        '''
        Данный метод определяет медиану в списке self.list_number.
        В переменную а записываем атрибут класса self.list_number и вычисляем середину списка.
        В цикле мы находим мин значение списка и удаляем их. Из оставшегося списка находим минимальный.
        '''
        a = self.list_number
        len_num = len(a) // 2 + 1
        num = 1
        while len_num > num:
            a.remove(min(a))
            num += 1

        print(f'Медианой данного числа является {min(a)}')

med = Median_number(100)
med.creating_list()
print(f'Получившийся список {med.list_number}')
med.finding_median()
