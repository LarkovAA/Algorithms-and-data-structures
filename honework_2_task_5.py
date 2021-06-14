# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

class Table_symbols:
    def __init__(self):
        self.start_num = 32
        self.finish_num = 128

    def table_output(self):
        '''
        Данный метод выводит номер символа и сам символ по 10 элементов в ряд.
        '''
        iteration_counter = 1
        for i in range(self.start_num, self.finish_num):
            if iteration_counter % 10 == 0:
                print(f'{i}:{chr(i)}', sep='\n')
            else:
                print(f'{i}:{chr(i)}', end=' ')
            iteration_counter += 1

Table_symbols().table_output()