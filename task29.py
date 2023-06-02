"""Задана последовательность неотрицательных целых чисел. 
Требуется определить значение наибольшего элемента 
последовательности, которая завершается первым встретившимся нулем 
(число 0 не входит в последовательность)"""

"""data = [int(i) for i in input("Введите числа через пробел: ").split()]
for i in range(len(data)-1):
    if data[i]< 0:
         print("Вы ввели отрицательное число")
max_num=0
while data[i] !=0:
        if data[i]>max_num:
            max_num=data[i]
print(max_num)"""

n = int(input())
max_number = n
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)