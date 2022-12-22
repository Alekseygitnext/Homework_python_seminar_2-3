# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint
import math

def get_numbers(n, first, last):
    return [randint(first, last) for i in range(n)]

def mult_pairs(mylist):
    return [mylist[i] * mylist[-i - 1] for i in range(math.ceil(len(mylist)/2))]

n = int(input('Введите количество чисел в списке: '))
first = 1
last = 10

mylist = get_numbers(n, first, last)
print(mylist)
print(f"Произведения пар чисел {mult_pairs(mylist)}")
