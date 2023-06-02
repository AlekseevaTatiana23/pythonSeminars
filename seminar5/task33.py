"""Хакер Василий получил доступ к классному
журналу и хочет заменить все свои минимальные
оценки на максимальные. Напишите программу,
которая заменяет оценки Василия, но наоборот: 
    все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4

Output: 1 3 3 3 1"""

# .sort()
# sorted()
#array = [5, 90, 34, 13, 54, 3, 12]
# array.sort()
#array = sorted(array)
#print(array)

n = int(input())
numbers = [int(i) for i in input().split()][:n]
new_numbers = [sorted(numbers)[0] if n == sorted(numbers)[-1] else n for n in numbers]
print(new_numbers)


#второй вариант
s = input().split()
min1 = min(s, key=int)
max1 = max(s, key=int)
print(*[min1 if i == max1 else i for i in s])