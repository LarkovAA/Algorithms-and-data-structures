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
                num = input(f'Введите значение элемента матрицы [{c}][{l}] ')
                rows_matrix.append(num)
            self.matrix.append(rows_matrix)
        for i in self.matrix:
            print(f'{i}', sep='\n')

    def max_elem_min_cilumn(self):
        list_min = []
        for l in range(self.num_line):
            list_column_min = []
            for c in range(self.num_line):
                list_column_min.append(self.matrix[c][l])
                if c == self.num_line-1:
                    list_min.append(min(list_column_min))
        max_num = max(list_min)
        print(f'Максимальный элемент среди минимальных элементов столбцов матрицы {max_num}')

mat= Matrix(3,3)
mat.creating_matrix()
mat.max_elem_min_cilumn()


