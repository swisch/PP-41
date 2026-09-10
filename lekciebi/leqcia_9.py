# def first_even(): # gamocxadeba
#     listi = [1, 2, 3, 4, 5, 6,5]
#     # listi_2 = []
#     for num in listi:
#         if num % 2 == 0:
#             # listi_2.append(num) #[2, 4, 6]
#             print(num)
#     # print(listi_2[2]) # aq ukve shevsebulia listi 
# #             break

            
# # first_even() # gamodzaxeba
# # ...
# # DRY = Dont repeat yourself 
# # kiss - keep it simple stupid 

# # -----------------------------------------------------------------------------------------------------

# # parameters - გადაეცემა ფუნქციას და არის უბრალოდ placeholder რომ ფუნქციას გადავცე რეალური მნიშვნელობა შემდგომ
# # arguments  -  რეალური მნიშვნელობა

# listi = [2, 3, 4, 5, 6]

# def find_first_even(numbers_listi_cvladi):  # numbers_listi_cvladi -> parametri
#     for number in numbers_listi_cvladi:
#         if number % 2 == 0:
#             print(number)

         
# find_first_even(listi)
# find_first_even([4, 76, 2, 5, 8])

# ----------------------------------------------------------------------------------------------------

# print vs return

# def even_number(numbers):
#     for n in numbers:
#         if n % 2 == 0:
#             return n
# # print(even_number([1, 2, 3, 4]))
# return_number = even_number((1, 4, 6, 2))

# def sum():
#     return return_number ** 5 
# result = sum()
# print(result)

# --------------------------------------------------------------------------------------------------


# def lower_case(string_data):
#     print("es aris printi")
#     return string_data.lower()
    

# data = lower_case("daNNNNNNta")
# print(data)


# --------------------------------------------------------------------
# ???????????????????????????????????????????????

# def add(nebismieri):
#     total = sum(nebismieri) # es sum() aris pythonsh =ichashenebuli
#     return total

# result = add([3, 5, 6])

# def division(zeda_funqcia):  # func = add
#     # function_variable = func_name([3, 5, 6])
#     return zeda_funqcia / 6

# print(division(result))

# --------------------------------------------------------------------

# def search_number(numbers, target):
#     for element in numbers:
#         if element == target:
#             return f"found {element}"
#     return "not found"

# tuple_nums = ('5', '6', "str")
# user_input = input("Enter element to find: ")
# result = search_number(tuple_nums, user_input)
# print(result)


# --------------------------------------------------------------------

# module - patara, , library - 

import random

def guess_the_number():
    number = random.randint(1, 10)
    # print(number)
    guess = int(input("Guess "))

    if guess == number:
        print("YES")
    else:
        print(f"not right {number}")


# pirveli function -> random ricxvze rom daaabrunos
# meore function - user input 


def main():
    # pirveli function
    # meore function
    guess_the_number()


main()
# if __name__ == "__main__":
#     main()
# ----------------------------------------------------------------

