# Задачи:
# 1. Напишите программу, которая принимает на вход два числа и
# проверяет, является ли одно число квадратом другого.

# number1 = int(input('Введите первое число: '))
# number2 = int(input('Введите второе число: '))
# if number1 ** 2 == number2 or number2 ** 2 == number1:
#     print('yes')
# else:
#     print('no')

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:

# numbers = []
# for _ in range(5):
#   n = int(input('Введите число: '))
# numbers.append(n)

# Или

# maxx = numbers[0]
# for i in numbers:
#   if i > maxx:
#     maxx = i
# print(maxx)

# Или

# maxx = int(input('Введите число: '))
# for i in range(4):
#   n = int(input('Введите число: '))
# if n > maxx:
#     maxx = n
# print(maxx)

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# num2 = [-num]
# for _ in range(2*num):
#   num2.append(-num+1)
#   num=num-1
# print(num2)


# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# number1 = float(input('Введите первое число: '))
# s = number1 * 10%10
# print(int(s))

# a = float(input())
# if a % 1 == 0:
#   print('нет')
# else:
#   print(int(a * 10) % 10)

# a = input()
# if '.' in a:
#   print(a[a.index('.') + 1])
# elif ',' in a:
#   print(a[a.index(',') + 1])
# else:
#   print('нет')

# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
n = int(input())
if (n % 5 == 0 or n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
    print('True')
else:
    print('false')
