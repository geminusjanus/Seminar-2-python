# Задайте список из N элементов, заполненных случайными числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
a=[randint(-10,10) for i in range(10)]
print(a)
multiplication = 1
for i in a:
    multiplication *= i
print(f'Произведение элементов массива = {multiplication}')