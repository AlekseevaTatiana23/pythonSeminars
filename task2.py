"""Задача 2: Найдите сумму цифр трехзначного числа."""

num=int(input("Введите трехзначное число: "))
sum3=num%10
sum2=(num//10)%10
sum1=num//100
print(sum1+sum2+sum3)

    