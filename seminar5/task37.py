"""Дано натуральное число N и 
последовательность из N элементов. 
Требуется вывести эту последовательность 
в обратном порядке.
Примечание. В программе запрещается объявлять
массивы и использовать циклы 
(даже для ввода и вывода).

Input:    2 -> 3 4
Output: 4 3"""


def reverse_numbers(num):
   if num == 0:
      return ''
   k = int(input())
   return reverse_numbers(num - 1) + f'{k} '


n = int(input())
print(reverse_numbers(n))

# r(2) -> k = 3 -> r(1) + " 3" = " 4" + " 3" = " 4 3"
#                   |
#                  k = 4
#                   |
#                  r(0) + " 4" = "" + " 4" = " 4"
#                   |
#                   ""


"""def reverse_numbers(n):
    k = input()
    if n == 1:
        return k
    return reverse_numbers(n - 1) + k + " "


n = int(input())
print(reverse_numbers(n))"""