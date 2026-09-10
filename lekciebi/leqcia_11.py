# # lambda functions - anonimuri functions
# # operation = lambda a, b: a + b
# # print(operation(5, 7))


# # math_operations = {
# #     "add": lambda x, y: x + y,
# #     "divide": lambda x, y: x / y if y != 0 else 'division by 0'
# # }

# # print(math_operations["add"](3, 5))
# # print(math_operations["divide"](12, 0))


# # ---------------------------------------------------------------------

# # ფუნქცია(ფუნქცია, კოლექცია)
# # filter, zip, map, reduce

# # # map - map(function, koleqcia )
# # def to_uppercase(char):
# #     return char.upper()

# # char_list = ['a', 'b', 'c']
# # uppercase = map(to_uppercase, char_list)
# # print(tuple(uppercase)) # isev koleqciad unda daabrunot 


# # filter - filter(function, collection)
# # numbers = [3,4, 6, 7, 8, 9, 12]
# # even_numbers = filter(lambda x: x % 2 == 0, numbers)
# # print(list(even_numbers))


# # zip(collection, collection) 
# # listi_1 = ['1', '2', '3',]
# # listi_2 = ['6', '7', '8', "rame"]

# # zipped = zip(listi_1, listi_2)
# # print(list(zipped))


# # reduce(function, koleqcia)
# # pip install functools

# # from functools import reduce 

# # def add(x, y):
# #     return x + y

# # numbers = (4, 5, 6, 7, 8)
# # result = reduce(add, numbers)
# # print(result)


# # ---------------------------------------------------------------------

# # LEGB - local, enclose, global


# x = 'Global X'

# def outer_function():
#     x = "Enclosing X"

#     def inner_function():
#         x = 'Local X'
#         print(f'Inner function X {x}')
#     inner_function()

#     print(f"Outer function x {x}")

# outer_function()

# print(f'Global X  {x}')

# # --------------------------------------------------------------
# # Recusion 
# # factorial



# # def factorial(num):
# #     if num == 0 or num == 1:   # base case 
# #         return 1 
# #     else:
# #         return num * factorial(num - 1)
    
# # print(factorial(5))

# # 5 X factorial(4)
# # 5 X 4 X factorial(3)
# # 5 X 4 X 3 X factorial(2)
# # 5 X 4 X 3 X 2 X factorial(1) = 5 X 4 X 3 X 2 X 1 = 120



# # 0, 1 , 1, 2, 3, 5
# def fibonacci(n):
#     if n <= 1: # base case 
#         return n 
#     return fibonacci(n -1) + fibonacci(n - 2)

# # print(fibonacci(3))
# for i in range(6):
#     print(fibonacci(i), end='  ')


# ----------------------------------------------------------------------------------

# TYPE HINTING 
# name = "ANI" 
# age = 77
# price = 4.6
# is_blocked = True


# variable_name : type = value
# type hint
name: str = '58'
age: int = 55
price: float = 5.6
is_blocked: bool = True

print(name)



def function_power(a: int, b: int) -> int:
    return a + b

print(function_power(3, 4))
print(function_power('3', '4'))


# ---------------------------------------------------------------------

numbers: list[int] = [1, 2, 3, 4, 5]
print(numbers)

def test(numbers: set[int]):
    return sum(numbers)


from typing import List # es aris dzveli versia
numbers: List[int] = [1, 2, 3]


# zemot ubralod vutxrat ra types sheinaxavs da qvemot shevinaxot 
listi: list[int] 
listi = [1, 2, 3, 4, 5]


info: dict[str, int] = {
    "data": 43,
    "review": 65
}
print(info['data'])


# python - mtliani programa
# mypy -> programis tipebis chekavs 

def add(a: int, c: int) -> int:
    return a + c

result_1 = add(4 , 5)
result_2 = add('4', '5')

