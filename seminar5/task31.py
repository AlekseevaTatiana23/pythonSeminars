"""Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a1 = 1, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21"""



def fibonacci(Num):
   if Num in [0, 1]:
       return 1
   return fibonacci (Num-1)+ fibonacci (Num-2)

N=int(input("Введите количество элементов N: "))
print(fibonacci(N))

# 0 1 1 2 3 5 8 13 21 34
# 0 1 2 3 4 5 6 7  8  21
# fib(4) -> fib(3) + fib(2) = 2 + 1 = 3
#             |         |
#    fib(2) + fib(1)=1   fib(1)=1 + fib(0)=0
#      |
# fib(1) + fib(0) = 1 + 0 = 1
#   |        |
#   1        0