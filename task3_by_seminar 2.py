# Реализовать алгоритм перемешивания списка
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для получения случайного int

import random

def get_mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
mixed_list = get_mix_list(list)

print("Исходный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)
