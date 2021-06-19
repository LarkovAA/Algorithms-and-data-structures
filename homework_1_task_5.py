# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
def vchecking_distance(a, b):
    if set_alphabet.get(a) > set_alphabet.get(b):
        return set_alphabet.get(a) - set_alphabet.get(b) - 1
    else:
        return set_alphabet.get(b) - set_alphabet.get(a) - 1

set_alphabet = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8, 'з': 9, 'и': 10, 'й': 11, 'к': 12, 'л': 13, 'м': 14
                , 'н': 15, 'о': 16, 'п': 17, 'р': 18, 'с': 19, 'т': 20, 'у': 21, 'ф': 22, 'х': 23, 'ц': 24, 'ч': 25, 'ш': 26
                , 'щ': 27, 'ъ': 28, 'ы': 29, 'ь': 30, 'э': 31, 'ю': 32, 'я': 33}

a, b = [i for i in input('Введите какие буквы ходите определить. ').split()]


print(f'Данные буквы находятся на местах {a} = {set_alphabet[a]}, {b} = {set_alphabet[b]}, расстояние междду ними {vchecking_distance(a, b)} буквы')