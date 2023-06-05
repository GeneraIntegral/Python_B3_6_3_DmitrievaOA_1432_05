# Python_B3_6_3_DmitrievaOA_1432_05

import math
import random

print("Enter an operation('+', '-', '*', '/', '**', 'mod', 'rand', 'fact', 'acos'):") # Введите операцию
operation = input()

if operation == '+':
    print("Enter the first number:") # Введите первое число:
    num1 = float(input())
    print("Enter the second number:") # Введите второе число:
    num2 = float(input())
    print("Result:", num1 + num2) # Результат:

elif operation == '-':
    print("Enter the first number:") # Введите первое число:
    num1 = float(input())
    print("Enter the second number:") # Введите второе число:
    num2 = float(input())
    print("Result:", num1 - num2) # Результат:

elif operation == '*':
    print("Enter the first number:") # Введите первое число:
    num1 = float(input())
    print("Enter the second number:") # Введите второе число:
    num2 = float(input())
    print("Result:", num1 * num2) # Результат:

elif operation == '/':
    print("Enter the first number:") # Введите первое число:
    num1 = float(input())
    print("Enter the second number:") # Введите второе число:
    num2 = float(input())
    if num2 != 0:

        print("Result:", num1 / num2) # Результат:
    else:
        print("Division by 0 is impossible!") # Деление на 0 невозможно!

elif operation == '**':
    print("Enter the number to be raised to the power:") # Введите число, которое нужно возвести в степень:
    num1 = float(input())
    print("Enter the power to which you want to raise the number:") # Введите степень, в которую нужно возвести число:
    num2 = float(input())
    print("Result:", num1 ** num2) # Результат:

elif operation == 'mod':
    print("Enter the number:") # Введите число:
    num1 = float(input())
    print("Enter module:") # Введите модуль:
    num2 = float(input())
    print("Result:", num1 % num2) # Результат:

elif operation == 'rand':
    print("Enter a range to generate a random number:") # Введите диапазон для генерации случайного числа:
    print("Enter the minimum number:") # Введите минимальное число:
    num1 = int(input())
    print("Enter the maximum number:") # Введите максимальное число:
    num2 = int(input())
    print("Random number from range [", num1, ",", num2, "]:", random.randint(num1, num2)) # Случайное число из диапазона

elif operation == 'fact':
    print("Enter a number to calculate the factorial:") # Введите число для вычисления факториала:
    num1 = int(input())
    print("Result:", math.factorial(num1)) # Результат:

elif operation == 'acos':
    print("Enter a number to calculate the arc cosine (of -1 to 1):") # Введите число для вычисления арккосинуса
    num1 = float(input())
    if -1 <= num1 <= 1:
        print("Result:", math.acos(num1)) # Результат:

    else:
        print("The number must be in the range of -1 to 1!") # Число должно быть в диапазоне
