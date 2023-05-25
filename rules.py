data = [int(i) for i in input("Введите числа: ").split()]
print(data)

#array(import array || import numpy)

"""list() - set() - tuple() можно менять тип данных"""

# data = [[1, -1.575], ['Hello, world', True], [15, -7]]
# #           0                  1                 2
# print(data[2][0])

data = {"Ivan": 27, 'Alexandr': 36, 'Konstantin': {'age': 21, 'hobby': ['tennis', 'fotball']}}
# key: value
print(data['Konstantin']['hobby'][0])

# .values()
# .keys()
print(list(data.values()))
print(list(data.keys()))

# data = [[1, -1.575], ['Hello, world', True], [15, -7]]
# #           0                  1                 2
# print(data[2][0])

data = {"Ivan": 27, 'Alexandr': 36, 'Konstantin': {'age': 21, 'hobby': ['tennis', 'fotball']}}
# key: value
print(data['Konstantin']['hobby'][0])

# .values()
# .keys()
print(list(data.values()))
print(list(data.keys()))
print(list(data.items()))
for k, v in data.items():
    print(k, v)