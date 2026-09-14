# lekcia - 1 
# print(), переменные, типы данных str, int, float, bool
# name = "Armen"
# age = 40
# city = "Tbilisi"

# print(name)
# print(age)
# print(city)
# #------
# name = "Armen"
# print(name)
# print("Hello", name)
# print("Welcome", name)
#--------
# str — строка
#--------
# означает string — строка, то есть текст
# type()

# name = "Armen"

# print(type(name))
# <class 'str'>
#-----------
# int — целые числа - int означает integer — целое число.age = 40
#---------
# С int можно выполнять математические операции:
# clients = 40000
# year = 2026
# temperature = -5
# a = 10
# b = 5

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a ** b)
#----------
# float — дробные числа
# float означает floating point number — число с плавающей точкой, то есть дробное число.
#---------
# height = 1.80

# print(type(height))
# <class 'float'>

#bool — логический тип
# has_car = True
# is_student = False
# has_car = True

# print(type(has_car))
# <class 'bool'>

# name = "Armen"  # str
# age = 40        # int
# height = 1.8    # float
# has_car = True  # bool
#--------------------

# # Заголовок
# title = "===== МОЯ АНКЕТА ====="

# # Информация
# name = "Armen"
# age = 40
# height = 1.80
# city = "Tbilisi"
# profession = "Engineer"
# has_car = True


# # Вывод информации
# print(title)

# print("Имя:", name)
# print("Возраст:", age)
# print("Рост:", height)
# print("Город:", city)
# print("Профессия:", profession)
# print("Есть машина:", has_car)

#-------------------

# Урок 2. input(), преобразование типов и арифметические операции

# input() — ввод данных

# name = input("Введите имя: ")

# print(name)

#------------------
# სქემა
# input()
#    ↓
# пользователь вводит Armen
#    ↓
# "Armen"
#    ↓
# name = "Armen"
#    ↓
# print(name)
#-------------------

# name = input("Введите имя: ")
# city = input("Введите город: ")

# print("Имя:", name)
# print("Город:", city)

#------------------- 2. Важное правило: input() возвращает str

# Пользователь вводит: 40 -- Но Python покажет: 40  <class 'str'> Потому что input() всегда возвращает строку str.

# 3. Почему это важно : number1 = input("Первое число: ") number2 = input("Второе число: ") # print(number1 + number2)  Но получим: 1020
# "10" + "20"
#      ↓
#    "1020"
#--------------
# 4. int() — превращаем строку в целое число
# number = int(input("Введите число: "))
# input()
#    ↓
# "10"
#    ↓
# int("10")
#    ↓
# 10
#    ↓
# number = 10

# number1 = int(input("Первое число: "))
# number2 = int(input("Второе число: "))

# print(number1 + number2)
#Результат: 20

#--------------
# 6. float() — дробные числа
#--------------

#height = float(input("Введите рост: "))
# height = float(input("Введите рост: "))

# print(height)
# print(type(height))

# 7. Когда использовать int(), а когда float()
# clients = int(input("Количество клиентов: "))
# price = float(input("Цена: "))

#-------------
# 8. str() — преобразование в строку
#------------

# age = 40

# text_age = str(age)

# print(text_age)
# print(type(text_age))

#--------------
# 9. Основные преобразования
#-------------
# int()
# float()
# str()
# bool()
#------
# number = int("100")
# price = float("25.5")
# text = str(100)
# 10. Арифметические операторы
# a = 10
# b = 3
# print(a + b) Сложение +
# print(a - b) Вычитание -
# print(a * b) Умножение *
# print(a / b) Деление /
# 11. Целочисленное деление //
# print(10 // 3)
# 12. Остаток от деления %
# print(10 % 3)
# 10 = 3 × 3 + 1  # 1 — остаток.
# print(8 % 2) # --- 0 Потому что 8 делится на 2 без остатка. проверяем чётность: number % 2
# 13. Возведение в степень **
# print(2 ** 3) # ---- 2 × 2 × 2
# 14. Все арифметические операторы
# Оператор	Что делает	Пример	Результат
# +	сложение	10 + 3	13
# -	вычитание	10 - 3	7
# *	умножение	10 * 3	30
# /	деление	10 / 2	5.0
# //	целочисленное деление	10 // 3	3
# %	остаток	10 % 3	1
# **	степень	2 ** 3	8

# 19. Мини-программа по урокам 1–2

# name = input("Введите имя: ")
# age = int(input("Введите возраст: "))
# height = float(input("Введите рост: "))
# city = input("Введите город: ")

# next_age = age + 1

# print()
# print("===== АНКЕТА =====")
# print("Имя:", name)
# print("Возраст:", age)
# print("Рост:", height)
# print("Город:", city)
# print("Возраст через год:", next_age)

#-------------
# Урок 3 — Строки str и методы строк
#--------------

# Главная цель урока — научиться получать текст, изменять его, очищать и проверять его длину.


# upper() - upper() превращает все буквы строки в заглавные.
# lower() - lower() делает все буквы маленькими.
# capitalize() - capitalize() делает первую букву строки большой, а остальные — маленькими.
# title() - title() делает первую букву каждого слова большой.
# strip()
# replace()
# len()

#--------------
# 2. Метод .upper()
#--------------

# name = "Armen"

# print(name.upper()) # ARMEN

# "Armen"
#    ↓
# .upper()
#    ↓
# "ARMEN"

#--------------
# 3. Метод .lower()
#--------------

# name = "ARMEN"
# print(name.lower()) # armen

#--------------
# 4. Метод .capitalize()
# --------------
# name = "armen"
# print(name.capitalize()) # Armen

#   -----------
# full_name = "armen darbinian"

# print(full_name)

# ============================================================
# УРОК 3 — СТРОКИ str И МЕТОДЫ СТРОК
# ============================================================

# full_name = "armen darbinian"

# print(full_name)
# print(full_name.title())

# Результат:
# armen darbinian
# Armen Darbinian


# --------------------
# 5. Метод .title()
# --------------------

# Делает первую букву каждого слова заглавной.

# full_name = "armen darbinian"

# print(full_name.title())

# Результат:
# Armen Darbinian


# --------------------
# 6. Метод .strip()
# --------------------

# Удаляет пробелы в начале и в конце строки.

# name = "     Armen     "

# print(name)
# print(name.strip())

# Было:
# "     Armen     "

# Стало:
# "Armen"


# --------------------
# 7. Метод .replace()
# --------------------

# Заменяет один текст другим.

# text = "I like Java"

# print(text.replace("Java", "Python"))

# Результат:
# I like Python


# --------------------
# 8. Функция len()
# --------------------

# len() показывает количество символов.

# name = "Armen"

# print(len(name))

# Результат:
# 5


# Можно комбинировать методы:

# name = input("Введите имя: ")

# name = name.strip().title()

# print("Welcome", name)


# ============================================================
# УРОК 4 — УСЛОВИЯ if / elif / else
# ============================================================

# Условные операторы позволяют программе принимать решения.


# --------------------
# 1. if
# --------------------

# age = 20

# if age >= 18:
#     print("Совершеннолетний")


# --------------------
# 2. if / else
# --------------------

# age = 15

# if age >= 18:
#     print("Совершеннолетний")
# else:
#     print("Несовершеннолетний")


# --------------------
# 3. if / elif / else
# --------------------

# score = 85

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("F")


# --------------------
# Операторы сравнения
# --------------------

# ==    равно
# !=    не равно
# >     больше
# <     меньше
# >=    больше или равно
# <=    меньше или равно


# --------------------
# Логические операторы
# --------------------

# and
# or
# not


# age = 25
# has_license = True

# if age >= 18 and has_license:
#     print("Можно управлять автомобилем")


# --------------------
# Проверка чётности
# --------------------

# number = int(input("Введите число: "))

# if number % 2 == 0:
#     print("Чётное")
# else:
#     print("Нечётное")


# ============================================================
# УРОК 5 — ОБРАБОТКА ОШИБОК try / except
# ============================================================

# try позволяет выполнить потенциально опасный код.
# except перехватывает ошибку.


# --------------------
# ValueError
# --------------------

# try:
#     age = int(input("Введите возраст: "))
#     print(age)
# except ValueError:
#     print("Нужно ввести целое число")


# --------------------
# ZeroDivisionError
# --------------------

# try:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))

#     print(a / b)

# except ValueError:
#     print("Введите числа")

# except ZeroDivisionError:
#     print("На ноль делить нельзя")


# --------------------
# else
# --------------------

# try:
#     number = int(input("Введите число: "))
# except ValueError:
#     print("Ошибка")
# else:
#     print("Вы ввели:", number)


# --------------------
# finally
# --------------------

# try:
#     number = int(input("Введите число: "))
# except ValueError:
#     print("Ошибка")
# finally:
#     print("Программа завершена")


# --------------------
# raise
# --------------------

# raise позволяет самостоятельно вызвать ошибку.

# number = int(input("Введите число: "))

# if number > 100:
#     raise ValueError("Число не должно быть больше 100")


# ============================================================
# УРОК 6 — ЦИКЛЫ while И for
# ============================================================

# Циклы позволяют повторять код.


# --------------------
# while
# --------------------

# number = 1

# while number <= 5:
#     print(number)
#     number += 1


# --------------------
# while True
# --------------------

# while True:
#     number = int(input("Введите 0 для выхода: "))

#     if number == 0:
#         break


# --------------------
# for
# --------------------

# for i in range(5):
#     print(i)

# Результат:
# 0
# 1
# 2
# 3
# 4


# --------------------
# range(start, stop, step)
# --------------------

# for i in range(1, 11, 2):
#     print(i)


# --------------------
# Перебор строки
# --------------------

# text = "Python"

# for letter in text:
#     print(letter)


# --------------------
# break
# --------------------

# for i in range(10):
#     if i == 5:
#         break
#     print(i)


# --------------------
# continue
# --------------------

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)


# --------------------
# Вложенные циклы
# --------------------

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)


# ============================================================
# УРОК 7 — СПИСКИ list
# ============================================================

# list — изменяемая коллекция данных.

# numbers = [10, 20, 30, 40]

# print(numbers)


# --------------------
# Индексы
# --------------------

# print(numbers[0])
# print(numbers[1])

# Индексация начинается с 0.


# --------------------
# append()
# --------------------

# numbers.append(50)


# --------------------
# extend()
# --------------------

# numbers.extend([60, 70])


# --------------------
# insert()
# --------------------

# numbers.insert(1, 15)


# --------------------
# remove()
# --------------------

# numbers.remove(30)


# --------------------
# pop()
# --------------------

# numbers.pop()


# --------------------
# index()
# --------------------

# print(numbers.index(20))


# --------------------
# count()
# --------------------

# numbers = [1, 2, 2, 3]

# print(numbers.count(2))


# --------------------
# sort()
# --------------------

# numbers = [5, 1, 4, 2]

# numbers.sort()

# print(numbers)


# --------------------
# Удаление дубликатов вручную
# --------------------

# numbers = [1, 2, 2, 3, 3, 4]

# new_list = []

# for number in numbers:
#     if number not in new_list:
#         new_list.append(number)

# print(new_list)


# ============================================================
# УРОК 8 — СЛОВАРИ dict
# ============================================================

# dict хранит данные в формате:
#
# key : value
# ключ : значение


# student = {
#     "name": "Armen",
#     "age": 40,
#     "city": "Tbilisi"
# }

# print(student)


# --------------------
# Получение значения
# --------------------

# print(student["name"])


# --------------------
# Добавление значения
# --------------------

# student["profession"] = "Engineer"


# --------------------
# Изменение значения
# --------------------

# student["age"] = 41


# --------------------
# keys()
# --------------------

# print(student.keys())


# --------------------
# values()
# --------------------

# print(student.values())


# --------------------
# items()
# --------------------

# print(student.items())


# --------------------
# Перебор словаря
# --------------------

# for key, value in student.items():
#     print(key, value)


# --------------------
# Подсчёт частоты
# --------------------

# words = ["python", "java", "python", "php", "python"]

# counter = {}

# for word in words:
#     if word in counter:
#         counter[word] += 1
#     else:
#         counter[word] = 1

# print(counter)


# ============================================================
# УРОК 9 — ФУНКЦИИ
# ============================================================

# Функция создаётся через def.


# def hello():
#     print("Hello")


# hello()


# --------------------
# Параметры
# --------------------

# def hello(name):
#     print("Hello", name)


# hello("Armen")


# --------------------
# return
# --------------------

# def add(a, b):
#     return a + b


# result = add(10, 20)

# print(result)


# --------------------
# print VS return
# --------------------

# print() показывает результат на экране.
# return возвращает результат из функции.


# --------------------
# DRY
# --------------------

# Don't Repeat Yourself
# Не повторяй один и тот же код.


# --------------------
# KISS
# --------------------

# Keep It Simple
# Код должен быть максимально простым и понятным.


# ============================================================
# УРОК 10 — АРГУМЕНТЫ ФУНКЦИЙ
# ============================================================

# --------------------
# Позиционные аргументы
# --------------------

# def user(name, age):
#     print(name, age)


# user("Armen", 40)


# --------------------
# Именованные аргументы
# --------------------

# user(age=40, name="Armen")


# --------------------
# Default argument
# --------------------

# def hello(name="Guest"):
#     print("Hello", name)


# hello()
# hello("Armen")


# --------------------
# *args
# --------------------

# *args собирает позиционные аргументы в tuple.

# def total(*args):
#     print(args)


# total(10, 20, 30)


# --------------------
# **kwargs
# --------------------

# **kwargs собирает именованные аргументы в dict.

# def info(**kwargs):
#     print(kwargs)


# info(name="Armen", age=40, city="Tbilisi")


# --------------------
# kwargs.items()
# --------------------

# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)


# info(name="Armen", age=40)


# ============================================================
# УРОК 11 — lambda, map, filter, zip, reduce
# ============================================================

# lambda — маленькая анонимная функция.


# add = lambda a, b: a + b

# print(add(5, 7))


# --------------------
# map()
# --------------------

# map применяет функцию к каждому элементу.

# numbers = [1, 2, 3, 4]

# result = list(map(lambda x: x ** 2, numbers))

# print(result)

# [1, 4, 9, 16]


# --------------------
# filter()
# --------------------

# numbers = [1, 2, 3, 4, 5]

# result = list(filter(lambda x: x % 2 != 0, numbers))

# print(result)

# [1, 3, 5]


# --------------------
# zip()
# --------------------

# names = ["Nika", "Ana", "Giorgi"]
# ages = [20, 25, 30]

# result = list(zip(names, ages))

# print(result)


# --------------------
# reduce()
# --------------------

# from functools import reduce

# numbers = [1, 2, 3, 4]

# result = reduce(lambda x, y: x + y, numbers)

# print(result)


# --------------------
# LEGB
# --------------------

# L = Local
# E = Enclosing
# G = Global
# B = Built-in


# --------------------
# Рекурсия
# --------------------

# def factorial(n):
#     if n == 1:
#         return 1

#     return n * factorial(n - 1)


# print(factorial(5))


# --------------------
# Type hints
# --------------------

# def add(a: int, b: int) -> int:
#     return a + b


# ============================================================
# УРОК 12 — ДЕКОРАТОРЫ
# ============================================================

# Декоратор позволяет добавить функциональность другой функции.


# def decorator(func):

#     def wrapper():
#         print("До функции")

#         func()

#         print("После функции")

#     return wrapper


# @decorator
# def hello():
#     print("Hello")


# hello()


# --------------------
# wrapper(*args, **kwargs)
# --------------------

# def decorator(func):

#     def wrapper(*args, **kwargs):

#         print("Start")

#         result = func(*args, **kwargs)

#         print("Finish")

#         return result

#     return wrapper


# --------------------
# Измерение времени
# --------------------

# import time


# def execution_time(func):

#     def wrapper(*args, **kwargs):

#         start = time.time()

#         result = func(*args, **kwargs)

#         end = time.time()

#         print("Time:", end - start)

#         return result

#     return wrapper


# ============================================================
# УРОК 13 — REGEX
# ============================================================

# Regex — регулярные выражения.
# Используется модуль re.


# import re


# --------------------
# Проверка Gmail
# --------------------

# email = input("Email: ")

# pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"

# if re.match(pattern, email):
#     print("Correct Gmail")
# else:
#     print("Incorrect Gmail")


# --------------------
# dir(str)
# --------------------

# print(dir(str))

# Показывает доступные методы и атрибуты класса str.


# ============================================================
# УРОК 14 — ГЕНЕРАТОРЫ И random
# ============================================================

# Генератор создаёт значения постепенно,
# а не хранит все значения сразу.


# --------------------
# yield
# --------------------

# def numbers():
#     yield 1
#     yield 2
#     yield 3


# for number in numbers():
#     print(number)


# --------------------
# random
# --------------------

# import random


# print(random.randint(1, 10))


# --------------------
# random.choice()
# --------------------

# letters = ["A", "B", "C", "D"]

# print(random.choice(letters))


# --------------------
# Генерация пароля
# --------------------

# import random
# import string


# password = ""

# symbols = string.ascii_letters + string.digits + string.punctuation

# for i in range(12):
#     password += random.choice(symbols)

# print(password)


# ============================================================
# УРОК 15 — ФАЙЛЫ
# ============================================================

# --------------------
# Запись файла
# --------------------

# file = open("test.txt", "w")

# file.write("Hello Python")

# file.close()


# --------------------
# Чтение файла
# --------------------

# file = open("test.txt", "r")

# text = file.read()

# print(text)

# file.close()


# --------------------
# Правильнее использовать with
# --------------------

# with open("test.txt", "r") as file:
#     text = file.read()

# print(text)


# --------------------
# Подсчёт символов
# --------------------

# print(len(text))


# --------------------
# Подсчёт слов
# --------------------

# words = text.split()

# print(len(words))


# --------------------
# Подсчёт строк
# --------------------

# lines = text.splitlines()

# print(len(lines))


# ============================================================
# УРОК 16 — CSV И РАБОТА С ФАЙЛАМИ
# ============================================================

# CSV = Comma-Separated Values


# import csv


# --------------------
# Запись CSV
# --------------------

# with open("students.csv", "w", newline="", encoding="utf-8") as file:

#     writer = csv.writer(file)

#     writer.writerow(["Name", "Age"])
#     writer.writerow(["Armen", 40])
#     writer.writerow(["Nika", 25])


# --------------------
# Чтение CSV
# --------------------

# with open("students.csv", "r", encoding="utf-8") as file:

#     reader = csv.reader(file)

#     for row in reader:
#         print(row)


# ============================================================
# УРОК 17 — ВВЕДЕНИЕ В OOP
# ============================================================

# OOP = Object-Oriented Programming
# Объектно-ориентированное программирование.


# --------------------
# class
# --------------------

# class Student:
#     pass


# --------------------
# Создание объекта
# --------------------

# student1 = Student()


# --------------------
# __init__
# --------------------

# class Student:

#     def __init__(self, name, age):

#         self.name = name
#         self.age = age


# student1 = Student("Armen", 40)

# print(student1.name)
# print(student1.age)


# --------------------
# Метод класса
# --------------------

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_info(self):
#         print(self.name, self.age)


# student1 = Student("Armen", 40)

# student1.show_info()


# --------------------
# self
# --------------------

# self — ссылка на конкретный объект.

# student1.name
# student2.name

# У каждого объекта свои данные.


# ============================================================
# УРОК 18 — ОСНОВНЫЕ ПРИНЦИПЫ OOP
# ============================================================

# 4 основных принципа:

# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction


# ============================================================
# 1. ENCAPSULATION — ИНКАПСУЛЯЦИЯ
# ============================================================

# Скрытие внутренних данных объекта.


# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def show_balance(self):
#         print(self.__balance)


# account = BankAccount(1000)

# account.show_balance()


# __balance
#
# двойное подчёркивание означает,
# что атрибут не предназначен для прямого доступа извне.


# ============================================================
# 2. INHERITANCE — НАСЛЕДОВАНИЕ
# ============================================================

# Родительский класс:

# class Animal:

#     def speak(self):
#         print("Animal sound")


# Дочерний класс:

# class Dog(Animal):

#     def bark(self):
#         print("Woof")


# dog = Dog()

# dog.speak()
# dog.bark()


# Схема:
#
# Animal
#   ↓
#  Dog


# --------------------
# super()
# --------------------

# class Animal:

#     def __init__(self, name):
#         self.name = name


# class Dog(Animal):

#     def __init__(self, name, breed):

#         super().__init__(name)

#         self.breed = breed


# dog = Dog("Rex", "Labrador")

# print(dog.name)
# print(dog.breed)


# ============================================================
# 3. POLYMORPHISM — ПОЛИМОРФИЗМ
# ============================================================

# Один метод может работать по-разному
# в разных классах.


# class Animal:

#     def speak(self):
#         print("Animal sound")


# class Dog(Animal):

#     def speak(self):
#         print("Woof")


# class Cat(Animal):

#     def speak(self):
#         print("Meow")


# animals = [
#     Dog(),
#     Cat()
# ]


# for animal in animals:
#     animal.speak()


# Один вызов:

# animal.speak()

# Но результат зависит от типа объекта.


# ============================================================
# 4. ABSTRACTION — АБСТРАКЦИЯ
# ============================================================

# Абстракция означает:
#
# пользователь знает ЧТО делает объект,
# но ему не обязательно знать КАК это реализовано внутри.


# Простой пример:

# class Car:

#     def start(self):
#         print("Car started")


# car = Car()

# car.start()


# Пользователь вызывает start(),
# но ему не нужно знать внутреннюю работу двигателя.


# ============================================================
# УРОК 19 — НАСЛЕДОВАНИЕ, OVERRIDING И ПОЛИМОРФИЗМ
# ============================================================

# В уроке 19 закрепляем:

# Inheritance
# Method Overriding
# Polymorphism
# super()
# Multiple Inheritance


# ============================================================
# 1. РОДИТЕЛЬСКИЙ КЛАСС Employee
# ============================================================


# class Employee:

#     def __init__(self, name, salary):

#         self.name = name
#         self.salary = salary


#     def show_info(self):

#         print("Name:", self.name)
#         print("Salary:", self.salary)


#     def calculate_salary(self):

#         return self.salary


# ============================================================
# 2. Developer НАСЛЕДУЕТ Employee
# ============================================================


# class Developer(Employee):

#     def __init__(self, name, salary, programming_language):

#         super().__init__(name, salary)

#         self.programming_language = programming_language


#     def calculate_salary(self):

#         return self.salary + 500


# ============================================================
# 3. Manager
# ============================================================


# class Manager(Employee):

#     def __init__(self, name, salary, team_size):

#         super().__init__(name, salary)

#         self.team_size = team_size


#     def calculate_salary(self):

#         return self.salary + self.team_size * 100


# ============================================================
# 4. Designer
# ============================================================


# class Designer(Employee):

#     def __init__(self, name, salary, design_tool):

#         super().__init__(name, salary)

#         self.design_tool = design_tool


#     def calculate_salary(self):

#         return self.salary + 300


# ============================================================
# 5. СОЗДАЁМ ОБЪЕКТЫ
# ============================================================


# developer = Developer(
#     "Nika",
#     3000,
#     "Python"
# )


# manager = Manager(
#     "Ana",
#     4000,
#     5
# )


# designer = Designer(
#     "Giorgi",
#     2500,
#     "Figma"
# )


# ============================================================
# 6. POLYMORPHISM
# ============================================================


# employees = [
#     developer,
#     manager,
#     designer
# ]


# for employee in employees:

#     employee.show_info()

#     print(
#         "Final salary:",
#         employee.calculate_salary()
#     )

#     print("----------------")


# Здесь происходит полиморфизм.


# employee.calculate_salary()
#
#            ↓
#
# Если employee = Developer
# вызывается Developer.calculate_salary()
#
# Если employee = Manager
# вызывается Manager.calculate_salary()
#
# Если employee = Designer
# вызывается Designer.calculate_salary()


# ============================================================
# METHOD OVERRIDING
# ============================================================

# В Employee существует:

# def calculate_salary(self):
#     return self.salary


# Но Developer создаёт свой метод:

# def calculate_salary(self):
#     return self.salary + 500


# Это называется:
#
# Method Overriding
#
# или:
#
# переопределение метода.


# ============================================================
# MULTIPLE INHERITANCE — МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ
# ============================================================

# Один класс может наследоваться
# от нескольких классов.


# class Device:

#     def __init__(self, brand, model):

#         self.brand = brand
#         self.model = model


#     def show_device_info(self):

#         print("Brand:", self.brand)
#         print("Model:", self.model)


# --------------------
# Camera
# --------------------

# class Camera:

#     def take_photo(self):

#         print("Photo taken")


# --------------------
# GPS
# --------------------

# class GPS:

#     def show_location(self):

#         print("Location found")


# --------------------
# Phone
# --------------------

# Phone получает возможности:
#
# Device
# Camera
# GPS


# class Phone(Device, Camera, GPS):

#     def __init__(self, brand, model):

#         super().__init__(brand, model)


# phone = Phone(
#     "Samsung",
#     "Galaxy"
# )


# phone.show_device_info()

# phone.take_photo()

# phone.show_location()


# ============================================================
# СХЕМА НАСЛЕДОВАНИЯ
# ============================================================

#               Device
#                 │
#                 │
#                 ▼
#               Phone
#              ↙     ↘
#         Camera     GPS


# Phone умеет использовать методы:

# show_device_info()
# take_photo()
# show_location()


# ============================================================
# ГЛАВНОЕ ИЗ УРОКА 19
# ============================================================

# 1. Наследование:

# class Developer(Employee):
#     ...


# Developer получает возможности Employee.


# ------------------------------------------------------------

# 2. super()

# super().__init__(name, salary)

# позволяет вызвать код родительского класса.


# ------------------------------------------------------------

# 3. Method Overriding

# Родитель:

# def calculate_salary(self):
#     ...


# Ребёнок:

# def calculate_salary(self):
#     ...


# Дочерний класс заменяет реализацию метода.


# ------------------------------------------------------------

# 4. Polymorphism

# for employee in employees:
#     employee.calculate_salary()


# Один и тот же код работает
# с Developer, Manager и Designer.


# ------------------------------------------------------------

# 5. Multiple Inheritance

# class Phone(Device, Camera, GPS):
#     ...


# Phone наследуется сразу
# от нескольких классов.


# ============================================================
# УРОКИ 17 → 18 → 19
# ============================================================

# Урок 17
#     ↓
# class
# object
# self
# __init__
# attributes
# methods

# Урок 18
# ============================================
# OOP - ობიექტო-ორიენტირებული პროგრამირება
# ============================================

# Encapsulation (ინკაფსულაცია)
# ინკაფსულაცია ნიშნავს კლასის მონაცემებისა და მეთოდების ერთ კლასში გაერთიანებას
# და საჭიროების შემთხვევაში მონაცემებზე პირდაპირი წვდომის შეზღუდვას.
# მაგალითად, private ატრიბუტის შექმნა შეგვიძლია __ გამოყენებით.

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.__owner = owner  # Private ატრიბუტი
#         self.__balance = balance
    
#     def deposit(self, amount):
#         """ფულის დეპოზიტი"""
#         if amount > 0:
#             self.__balance += amount
    
#     def get_balance(self):
#         """ბალანსის მიღება"""
#         return self.__balance


# # Inheritance (მემკვიდრეობა)
# # მემკვიდრეობა ნიშნავს, რომ შვილობილ კლასს შეუძლია მშობელი კლასის
# # ატრიბუტებისა და მეთოდების გამოყენება.
# # ეს საშუალებას გვაძლევს ერთი და იგივე კოდი თავიდან აღარ დავწეროთ.

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
#     def calculate_salary(self):
#         return self.salary

# class Manager(Employee):  # Manager იმკვიდრებს Employee-დან
#     def __init__(self, name, salary, bonus):
#         super().__init__(name, salary)
#         self.bonus = bonus
    
#     def calculate_salary(self):
#         return self.salary + self.bonus


# # Polymorphism (პოლიმორფიზმი)
# # პოლიმორფიზმი ნიშნავს, რომ სხვადასხვა კლასის ობიექტებს შეუძლიათ
# # ერთი და იგივე სახელის მეთოდის განსხვავებულად შესრულება.

# class Developer(Employee):
#     def calculate_salary(self):
#         return self.salary * 1.5  # დეველოპერი 50% ბონუსი

# class Seller(Employee):
#     def calculate_salary(self):
#         return self.salary * 1.2  # გამყიდველი 20% ბონუსი

# # გამოყენება
# employees = [
#     Manager("გიორგი", 1000, 200),
#     Developer("მარია", 1500),
#     Seller("დავით", 800)
# ]

# for emp in employees:
#     print(f"{emp.name}: {emp.calculate_salary()}")  # თითოეული განსხვავებულად


# # Abstraction (აბსტრაქცია)
# # აბსტრაქცია ნიშნავს, რომ მომხმარებელს ვაჩვენებთ მხოლოდ საჭირო ფუნქციებს,
# # ხოლო მათი შიდა მუშაობის დეტალებს ვმალავთ.

# class Car:
#     def __init__(self, model):
#         self.model = model
#         self.__engine_status = False
    
#     def start_engine(self):
#         """ძრავის დაწყება - მომხმარებელი არ იცის რა ხდება შიგნით"""
#         self.__engine_status = True
#         print(f"{self.model} ძრავა დაიწყო")
    
#     def stop_engine(self):
#         """ძრავის გაჩერება"""
#         self.__engine_status = False
#         print(f"{self.model} ძრავა გაჩერდა")
    
#     def drive(self):
#         """მოძრაობა"""
#         if self.__engine_status:
#             print(f"{self.model} მოძრაობს...")
#         else:
#             print("ჯერ დაიწყეთ ძრავა!")

# # გამოყენება
# my_car = Car("BMW")
# my_car.start_engine()
# my_car.drive()
# my_car.stop_engine()
# Урок 19
#     ↓
# Inheritance — практика
# super()
# Method Overriding
# Polymorphism — практика
# Multiple Inheritance
