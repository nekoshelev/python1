# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# n = int(input('Введите день недели(цифру): '))
# if n in range(1,6):
#     print('Будний день')
# elif n in range(6,8):
#     print('Выходной день')
# else:
#     print('Не корректное значение! Введите число от 1 до 7')


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             print(not (x or y or z) == (not x and not y and not z))
#             print(x, y, z)


# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# x = int(input('Введите X: '))
# y = int(input('Введите Y: '))
# if x > 0 and y > 0:
#     print('Первая четверть')
# elif x < 0 and y > 0:
#     print('Вторая четверть')
# elif x < 0 and y < 0:
#     print('Третья четверть')
# elif x > 0 and y < 0:
#     print('Четвертая четверть')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

# n = int(input('Введите номер четверти: '))
# if n < 1 or n > 4:
#     print('Введите значение от 1 до 4')
# elif n == 1:
#     print('x > 0 и y > 0')
# elif n == 2:
#     print('x < 0 и y > 0')
# elif n == 3:
#     print('x < 0 и y < 0')
# elif n == 4:
#     print('x > 0 и y < 0')

# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

print('Введите координаты первой точки: ')
a1 = float(input('X: '))
a2 = float(input('Y: '))
print("Введите координаты второй точки:")
b1 = float(input('X: '))
b2 = float(input('Y: '))

import math
sqrt = round(math.sqrt((b1 - a1) ** 2 + (b2 - a2) ** 2),2)
print('Расстоние между точками A и B: ', sqrt)