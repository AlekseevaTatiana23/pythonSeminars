"""Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа N."""

N=int(input("Введите число N: "))
number=2
i=0
while pow(number, i)<=N: #или while number**i<=N
    print(pow(number, i)) # print(number**i)
    i+=1