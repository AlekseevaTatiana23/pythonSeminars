"""Заполните массив элементами 
арифметической прогрессии. Её первый элемент,
разность и количество элементов нужно ввести 
с клавиатуры. Формула для получения n-го члена
прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""



a_1=int(input())
n=int(input())
d=int(input())
list=[]
for i in range(1, n+1):
    list.append(a_1+(i-1)*d)
print(list)