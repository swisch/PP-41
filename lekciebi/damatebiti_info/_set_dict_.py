# --------------
# Data Structures (სტრუქტურები
# ------------
# tuple არის მონაცემთა სტრუქტურა,
# რომელიც ინახავს ელემენტებს გარკვეული თანმიმდევრობით.
# tuple არის immutable - შექმნის შემდეგ მისი შეცვლა შეუძლებელია.
# list
# tuple
# set
# dict

# list არის მონაცემთა სტრუქტურა,
# რომელშიც შეგვიძლია რამდენიმე ელემენტის შენახვა.

# list არის mutable,
# ანუ შექმნის შემდეგ მისი შეცვლა შესაძლებელია.

# students = ["Nika", "Ana", "Giorgi"]

# append() სიის ბოლოში ამატებს ახალ ელემენტს.
# students.append("Luka")

# print(students)

# list поддерживает индексы:
# students = ["Nika", "Ana", "Giorgi"]

# print(students[0])
# print(students[1])
#И допускает дубликаты: И допускает дубликаты:
# tuple — кортеж : tuple нельзя изменить после создания. Официальная документация Python определяет tuple как immutable sequence — неизменяемую последовательность
# #numbers = (10, 20, 30)


# numbers[0] = 100 получит: TypeError


# tuple არის მონაცემთა სტრუქტურა,
# რომელიც რამდენიმე ელემენტს ინახავს.

# tuple არის immutable,
# ანუ შექმნის შემდეგ მისი ელემენტების შეცვლა შეუძლებელია.

# numbers = (10, 20, 30)

# ინდექსის გამოყენებით შეგვიძლია ელემენტის მიღება.
# print(numbers[0])

# მაგრამ ელემენტის შეცვლა შეუძლებელია.
# numbers[0] = 100  # TypeError
# Например, есть координаты:
# location = (41.7151, 44.8271) Если мы не хотим случайно менять эти значения, tuple может быть логичнее списка.
# 4. Очень важная особенность одного элемента
# number = (10)

# print(type(number)) 
# Это не tuple.

# Это:

# <class 'int'>

# Чтобы создать tuple из одного элемента, нужна запятая:

# number = (10,)

# print(type(number))
# Теперь: <class 'tuple'>
# თუ tuple-ში მხოლოდ ერთი ელემენტია,
# ელემენტის შემდეგ აუცილებლად უნდა დავწეროთ მძიმე.

# number = (10,)

# print(type(number)

# Tuple unpacking
# student = ("Armen", 40, "Tbilisi")

# name, age, city = student

# print(name)
# print(age)
# print(city)
# Здесь происходит распаковка:
# "Armen"   -> name
# 40        -> age
# "Tbilisi" -> city
# # tuple unpacking ნიშნავს tuple-ის ელემენტების
# # ცალკეულ ცვლადებში გადანაწილებას.

# student = ("Armen", 40, "Tbilisi")

# name, age, city = student

# print(name)
# print(age)
# print(city)
# set — множество
# # set არის მონაცემთა სტრუქტურა,
# # რომელიც ინახავს უნიკალურ ელემენტებს.

# # set-ში დუბლირებული მნიშვნელობები არ ინახება.

# numbers = {10, 20, 20, 30, 30}

# print(numbers)
# 7. Удаление дубликатов с помощью set
# # გვაქვს list, რომელშიც არის დუბლირებული მნიშვნელობები.
# numbers = [10, 20, 20, 30, 30, 40]

# # set() list-ს გარდაქმნის set-ად.
# # რადგან set დუბლირებულ ელემენტებს არ ინახავს,
# # განმეორებული რიცხვები წაიშლება.
# unique_numbers = set(numbers)

# print(unique_numbers)

# 8. Добавление в set — add()
# numbers.append(40)
# numbers.add(40)

# numbers = {10, 20, 30}

# numbers.add(40)

# print(numbers)

# numbers = {10, 20, 30}

# numbers.add(40)

# print(numbers)
# Если сделать: numbers.add(20) нового второго 20 не появится.

# 9. Удаление из set

# numbers = {10, 20, 30}

# numbers.remove(20)

# print(numbers)

# Если: numbers.remove(100)  -  KeyError
# Есть другой метод numbers.discard(100) Он не выдаст ошибку, если элемента нет.

# 10. Математические операции set
# Допустим: 
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# Union — объединение
# print(a | b)
# Получаем элементы из обоих множеств:
# {1, 2, 3, 4, 5, 6}
# print(a.union(b))
# Intersection — пересечение
# print(a & b)
# print(a.intersection(b))
# Difference — разница
# print(a - b)
# Symmetric Difference
# print(a ^ b)
# Результат:
# {1, 2, 5, 6}
# То есть элементы, которые есть только в одном из множеств, но не одновременно в обоих. Эти операции (|, &, -, ^) являются стандартными операциями Python set

# internet_clients = {
#     "Nika",
#     "Ana",
#     "Giorgi",
#     "Luka"
# }

# tv_clients = {
#     "Ana",
#     "Giorgi",
#     "Dato"
# }

# Хотим узнать клиентов, у которых есть и Internet, и TV:

# both_services = internet_clients & tv_clients

# print(both_services)

# both_services = internet_clients & tv_clients

# print(both_services)
# {"Ana", "Giorgi"}

# #----------------
# # Internet სერვისის მომხმარებლები
# internet_clients = {
#     "Nika",
#     "Ana",
#     "Giorgi",
#     "Luka"
# }

# # TV სერვისის მომხმარებლები
# tv_clients = {
#     "Ana",
#     "Giorgi",
#     "Dato"
# }

# # intersection-ის გამოყენებით ვპოულობთ მომხმარებლებს,
# # რომლებსაც ერთდროულად აქვთ Internet და TV სერვისი.
# both_services = internet_clients & tv_clients

# print(both_services)

# 12. dict
# student = {
#     "name": "Armen",
#     "age": 40,
#     "city": "Tbilisi"
# }

# В отличие от списка и tuple, мы обращаемся не по обычному числовому индексу, а по ключу: print(student["name"])
# Словарь представляет данные как пары key: value, причём ключи внутри словаря уникальны.

И ещё очень важная ловушка: a = {} Это: dict
Пустой set создаётся так: a = set()
Это отдельно подчёркивает официальная документация Python.