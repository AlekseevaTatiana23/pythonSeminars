"""Дан список чисел. Посчитайте, сколько 
в нем пар элементов, равных друг другу. 
Считается, что любые два элемента,
равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится
список чисел. Все числа списка находятся
на разных строках.
Ввод:			Вывод:
1 2 3 2 3			2"""

list_1 = [int(i) for i in input().split()]  # [2, 2, 2, 2]
result = {}  # key: value
for i in list_1:  # i = 2
    if i in result:  # есть ли ключ i внутри словаря
        result[i] = result[i] + 1  # {2: 1}
    else:  # если ключа i нет внутри словаря
        result[i] = 1
print(sum([element // 2 for element in result.values()]))