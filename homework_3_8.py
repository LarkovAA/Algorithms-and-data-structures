# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

def print_element_matrix(matrix):
    for i in matrix:
        print(i, sep= '\n')

class Sum_matrix_rows:
    def __init__(self):
        self.matrix = []

    def calc_sum_matr_rows(self):
        num_line = 0
        for _ in range(4):
            rows_matrix = []
            num_line += 1
            num_column = 0
            for _ in range(5):
                num_column += 1
                if num_column < 5:
                    num = int(input(f'Введите чиcло для элемента матрицы [{num_line}][{num_column}] '))
                    rows_matrix.append(num)
                else:
                    num = sum(rows_matrix)
                    rows_matrix.append(num)
                    self.matrix.append(rows_matrix)
        for i in self.matrix:
            print(f'{i}', sep='\n')

        #print(f'{print_element_matrix(self.matrix)} получившаяся матрица')

matr = Sum_matrix_rows()
matr.calc_sum_matr_rows()