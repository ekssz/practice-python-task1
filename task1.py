'''
Get and display the random natural numbers m and n that are not
exceed 20, n integers ranging from a to b inclusive, and m
non-negative random real numbers not exceeding n. The values ​​of a and b
entered from the keyboard.
'''

# -*- coding: utf-8 -*-

import random

# ввід значень a та b
a = int(input("Введіть значення a: "))
b = int(input("Введіть значення b: "))

# генерація випадкових чисел m та n за допомогою random
m = random.randint(0, 20)
n = random.randint(a, b)

# виведення на екран рандомних чисел
print("Випадкове натуральне число m:", m)
print("Випадкове натуральне число n:", n)

# генерація m невідємних випадкових чисел, що не перевищують n
random_numbers = [random.uniform(0, n) for _ in range(m)]

# виведення на екран згенерованих дійсних чисел
print("Невід'ємні випадкові дійсні числа, що не перевищують n:")
for number in random_numbers:
    print(number)
