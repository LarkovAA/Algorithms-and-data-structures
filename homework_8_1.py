# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
import hashlib

class Substring_search:
    def __init__(self, line):
        self.line = line

    def search(self):
        hash_substrings = set()
        for i in range(len(self.line)):
            if i == 0:
                max_j = len(self.line) - 1
            else:
                max_j = len(self.line)
            for j in range(max_j):
                if self.line[i:j] != ' ':
                    hash_substring = hashlib.sha1(self.line[i:j].encode('utf-8')).hexdigest()
                    hash_substrings.add(hash_substring)
                else:
                    continue

        print(f'Колличество подстрок в строке {self.line} = {len(hash_substrings)}')

text = Substring_search('Скажика дядя ведь не даром.')
text.search()



