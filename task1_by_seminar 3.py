# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.

from random import randint

def get_list(n, first, last):
    return [randint(first, last) for i in range(n)]

def sum_odd_position(mylist):
    return sum(mylist[1::2])
    
n = int(input('Введите количество чисел в списке: '))
first = 1
last = 10

mylist = get_list(n, first, last)
print(mylist)
print(f"Cумма элементов с нечетным индексом: {sum_odd_position(mylist)}")