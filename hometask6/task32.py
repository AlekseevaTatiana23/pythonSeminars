"""Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума 
 и не больше заданного максимума)"""

from random import randint

min_range=int(input("Введите минимум: "))
max_range=int(input("Введите максимум: "))
n=int(input("Введите количество элементов: "))
list_rand=[randint(1, 1000) for i in range(n)]
indexes=[]
#numbers = [int(i) for i in input().split()][:n]

print(list_rand)
for i in range(len(list_rand)):
    if list_rand[i] in range(min_range, max_range+1):
        indexes.append(i)
print(indexes)

