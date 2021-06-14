# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

class Elements:
    '''
    Создаем класс который принимает в своем параметре колличество элементов
    '''
    def __init__(self, element):
        self.element = int(element)
        self.start_number = 1
        self.list_element_number = []

    def summ_elements(self):
        '''
        Данный метод класса высчитывает элементы из ряда чисел записывает их в список и вычисляет их сумму
        '''
        summ_number = self.start_number
        self.list_element_number.append(summ_number)

        for _ in range(2, self.element + 1):
            summ_number /= -2
            self.list_element_number.append(summ_number)

        summ_number = sum(self.list_element_number)
        print(summ_number)

num_element = input('Ведите колличество элементов. ')

Elements(num_element).summ_elements()
