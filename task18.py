"""

*Пример:*

5
    1 2 3 4 5
    6
    -> 5"""
    
N=int(input("Введите количество элементов N: "))
data = [int(i) for i in input("Введите числа через пробел: ").split()]
if len(data) !=N:
    print("Вы ввели неверное количество элементов")
else:
    X=int(input("Введите число X: "))
min_dif=abs(X-data[0])
number=0

for i in range(1, len(data)):
    dif=abs(X-data[i])
    if dif<min_dif:
        min_dif=dif
        number=data[i]
print(number)