"""Требуется вычислить, сколько раз встречается 
некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – 
количество элементов в массиве. В последующих  
строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1"""
    
N=int(input("Введите количество элементов N: "))
data = [int(i) for i in input("Введите числа через пробел: ").split()]
if len(data) !=N:
    print("Вы ввели неверное количество элементов")
else:
    X=int(input("Введите число X: "))
count=0
for i in range(N):
    if data[i]==X:
        count+=1
print(count)

"""n = int(input())
list1 = []
for i in range(n):
    list1.append(int(input()))
x = int(input())
print(list1.count(x))"""
