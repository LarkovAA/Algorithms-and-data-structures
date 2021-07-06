import cProfile
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
        Данный метод определяет медиану в неотсортированом списке.
        Определяем место медианы в списке  len_num.
        Создаем новый список из среза данного списка от начало до места где должен быть медиана cross_section_median.
        Определяем из этого списка максимальное значени это значение и будет медианой max_cr_sec_med.
        Для быстроты удаления мы создали переменную которая определяет место максимального элемента в списке ind_max_el.
        В цикле фор мы проходим по остальной половине списка сравниваем каждый элемент с максимальным в первом списке.
        Если мак эл больше чем число из 2-ой половине мы удаляем мак число из списка добавляем в него меньший эл-т из 2-го списка снова выбираем мак элемент и индекс его.
        После прохода мы из списка определяем максимальное число.
        '''
        len_num = len(self.list_number) // 2 + 1
        cross_section_median = self.list_number[: len_num]
        max_cr_sec_med = max(cross_section_median)
        ind_max_el = cross_section_median.index(max_cr_sec_med)
        for num in self.list_number[len_num:]:
            if max_cr_sec_med > num:
                cross_section_median.pop(ind_max_el)
                cross_section_median.append(num)
                max_cr_sec_med = max(cross_section_median)
                ind_max_el = cross_section_median.index(max_cr_sec_med)

        med = max(cross_section_median)
        print(f' медианой являеться чтсло {med}')

med = Median_number(50000)
med.creating_list()
#print(f'{med.list_number}')
# med.finding_median()
cProfile.run('med.finding_median()')