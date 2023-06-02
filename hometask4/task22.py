"""Даны два неупорядоченных набора целых чисел
(может быть, с повторениями). Выдать без повторений
в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. 
n — кол-во элементов первого множества.
m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств."""


n=int(input("Количество элементов: "))
m=int(input("Количество элементов: "))

list_1=[int(i) for i in input("Введите целые числа: ").split()][:n]
set_1=set(list_1)
list_2=[int(i) for i in input("Введите целые числа: ").split()][:m]
set_2=set(list_2)


united_set=set_1.intersection(set_2)
united_list=list(united_set)

united_list.sort()
for i in united_list:
    print(i, end=" ")

"""for i in set_1:
    set_1.add(i)
for i in set_2:
    set_2.add(i)"""