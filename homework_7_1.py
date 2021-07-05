# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).
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
            num = random.randint(-100, 99)
            self.list_number.append(num)

    def sorted_list(self):
        '''
        Метод сортирует массив с помошью метода пузырька прии этом имеет счетчик в котором определяеться было ли изменения порядка элементов в массиве или нет.
        Если нет то цикл прекращается.
        '''
        n = 1
        movement_list = []
        while n < len(self.list_number):
            for i in range(len(self.list_number) - n):
                if self.list_number[i] > self.list_number[i + 1]:
                    self.list_number[i], self.list_number[i + 1] = self.list_number[i + 1], self.list_number[i]
                    movement_list.append('True')
                else:
                    movement_list.append('False')
            if 'True' not in movement_list:
                break
            n += 1
            movement_list.clear()
        print(f'Отсортированый массив выглядит следующим образом {self.list_number}')

num = Sorted_number(15)
num.creating_list()
print(f'Созданный массив {num.list_number}')
num.sorted_list()



