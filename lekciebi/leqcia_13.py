# numbers = [1, 2, 3 , 4, 3, 4]
# filter_numbers = list(filter(lambda number: number != 3, numbers))
# print(filter_numbers )

# # --------------------------------------------------------------
# # ReGex - regular expressions 
# # pattern 

# import re 
# gmail = "ani@gmail.com"
# user = input("enter your gmail: ")

# pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
# if re.match(pattern, user):
#     print("Valid")
# else:
#     print('Not valid' )


# # ---------------------------------------------------------------------------------------------------


# import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(bool(x))


# ---------------------------------------------------------------------------------------------------------


# generator - yield 

# def number():
#     return [1, 2, 3, 4, 5]


# def get_number():
#     for x in range(5):
#         yield x

# number = get_number()
# print(next(number)) # I
# print(next(number)) # II
# print(next(number)) # III
# print(next(number)) # IV



# def mil_loops():
#     for num in range(1_000_000):
#         yield num

# generatorr = mil_loops()
# print(next(mil_loops()))

# lazy evaluation


# def power(n):
#     for i in range(1, n + 1):
#         yield i ** 2

# for result in power(5):
#     print(result)
