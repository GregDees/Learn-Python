# 1. Приветствие
# def greet(name):
#     answer = 'Привет, ' + name + '!'
#     return answer

# name = input('Введите имя: ')
# print(greet(name))

# 2. Найти площадь
# def rectangle_area(width, height):
#     result = width * height
#     return result

# width = int(input('Введите ширину: '))
# height = int(input('Введите высоту: '))
# print (rectangle_area(width, height))

# 3. Найти самое большое число
# def max_of_three(a, b, c):
#     if a > b and a > c:
#         return a
#     if b > a and b > c:
#         return b
#     return c

# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# c = int(input('Введите число c: '))
# print(max_of_three(a, b, c))

# 4. Числа Фибоначчи
# def fib(n):
#     a = 0
#     b = 1
#     numbers = []
#     for _ in range(n):
#         numbers.append(a)
#         a, b = b, a+b
#     return ', '.join(map(str, numbers))

# n = int(input('Введите искомое число: '))
# print(fib(n))

# 5. Простое число
# def is_prime(n):
#     for a in range(2, n): #  шаг 1. n = 14, a = 2
#         if n % a == 0: # если N делится хотя бы на любое A, то это хуйня
#             return 'Число хуйня ебаная, перезагадай'
#     return 'Число простое'

# a = int(input('Введите число: '))
# print(is_prime(n = a))

# 6. Сумма цифр числа
# def sum_digits(num): # 159 -> 15 /  101 -> 2
#     result = 0
#     while num > 0:
#         result += num % 10
#         num //= 10 # num = 159//10
#     return result



# num = int(input('Введите число: '))
# print(sum_digits(num))

# 7. Степень числа (рекурсия)
# def power(base, exponent):
#     result = base # base=5, exp = 3, 5^3 = 5 * 5 * 5
#     for a in range(exponent-1):
#         result *= base
#     return result

# def power(base, exponent):
#     if exponent == 1:
#         return base
#     return base * power(base,  exponent-1)

# base = int(input('Введите число: '))
# exponent = int(input('Введите cтепень: '))
# print(power(base, exponent))

# 8. Палиндром
# def is_palindrome(text):
#     text = "".join(x.lower() for x in text if x.isalpha()) # оставляем только буквы в lower()
#     print(text)
#     return text == text[::-1] # 

# def is_palindrome(text):
#     l = 0
#     r = len(text) - 1
#     while l <= r:
#         while not text[l].lower().isalpha():
#             l += 1
#         while not text[r].lower().isalpha():
#             r -= 1
#         if text[l].lower() != text[r].lower():
#             return False
#         l += 1
#         r -= 1
#     return True

# text = str(input('Введите текст: '))
# print(is_palindrome('А роза упала на лапу Азора'))

# 9. Двоичный перевод
# def to_binary(num):
#     result = ''
#     while num > 0:
#         result = str(num % 2) + result
#         num = num // 2
#     return result
        
# num = int(input('Введите число: '))
# print(to_binary(num))

