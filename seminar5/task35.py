# Напишите функцию, которая принимает
# одно число и проверяет, является ли оно простым
#
# Напоминание: Простое число - это число,
# которое имеет 2 делителя: 1 и n(само число)

def numbers(num):
    for i in range(2, (num/2 + 1)): #от 2 , т.к. простое число не может быть кратно 2. 1 не является простым числом
        if num % i ==0:
            return('no')
    return 'yes'

n=int(input())
print(numbers(n))



"""n = int(input())
k = 0
if n == 1 and n % 2 == 0:
    print("Число непростое")
elif n in (2, 3):
    print("Число простое")
else:
    for i in range(3, (n // 2) + 1, 2):
        if n % i == 0:
            k += 1
    if k == 0:
        print("Число простое")
    else:
        print("Число непростое")"""
