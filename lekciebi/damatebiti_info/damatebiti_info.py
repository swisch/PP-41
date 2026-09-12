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

# full_name = full_name.title()

# print(full_name)
