"""Задача №15. Общее обсуждение
15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9"""

n = int(input("Введите количество арбузов: "))

min_massa=1001
max_massa=0
for i in range(n):
    massa=int(input("Введите массу арбуза: "))
    if massa>max_massa:
        max_massa=massa
    if massa< min_massa:
        min_massa=massa
print(min_massa, max_massa)