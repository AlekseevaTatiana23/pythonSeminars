"""Пользователь вводит текст(строка).
Словом считается последовательность 
непробельных символов идущих подряд, 
слова разделены одним пробелом. Определите, 
сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore 
The shells that she sells are sea shells 
I'm sure 
So if she sells sea shells on the sea shore 
I'm sure that the shells are sea shore shells

Output: 13"""

stroka='She sells sea shells on the sea shore The shells that she sells are sea shells Im sure So if she sells sea shells on the sea shore Im sure that the shells are sea shore shells'.split()
A=stroka.upper()
number=set(A)
print(number)
num=len(number)
print(num)