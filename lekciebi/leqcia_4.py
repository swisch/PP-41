# and, or, not

# print((5 == 5) and (2 < 4))  # False 
# # False and False -> False

# print((12 < 12) or (13 > 124)) # 
# # True or False

# print(not(12 != 12))   12 != 12 -> not False -> True

# -----------------------------------------------------------------------

# print((12 < 13) and (13 < 17))
# 12 < x < 17   ---> (x > 12) and (x < 17)

# ------------------------------------------------------------------------

# temp = int(input("enter Temp: "))

# if temp > 30:  # პირობა როცა ჭეშმარიტია -> if True:
#     print("more than 30")

# else: # პირობას არ გადავცემთ
#     print("< 30")

# ---------------------------------------------------------------

# num_1 = int(input('Num 1 '))
# num_2 = int(input('Num 2 '))
# operation = input("Operator: ") # "+"

# if operation == '+':
#     result = num_1 + num_2
#     print(f"{num_1} + {num_2} = {result}")

# elif operation == '-':
#     print(num_1 - num_2)

# elif operation == '**':
#     print(num_1 ** num_2)

# else:
#     print("Unknown operator")

# ------------------------------------------------

# score = 90

# if score >= 60: # 90 >=60  -> True 
#     print("Passed")

# elif score >= 90: # True
#     # Never reached!
#     print("Excellent")

# else:
#     print("ELSE")


# if True:   an if False:
# ------------------------------------------------

# nested conditionals - roca ramdenime if maqvs ertmanetshi "chadgmuli"
# age = 18
# has_id = False

# if age >= 18:  # if 18 >= 18: if True:
#     if has_id:
#         print("Legal Person")
#     else:
#         print("Age is Okay but does not have ID")

# else:  # age < 18
#     # print("age < 18")
#     if has_id:
#         print("id -> not age")
#     else:
#         print("not id and not age ")


# ------------------------------------------------------------------------------------------------

# age = 18
# has_id = True

# if age >= 18 and has_id:
#     print("Legal")

# elif age >= 18 and not(has_id):
#     print("age valid and NOT ID")

# elif age < 18 and has_id:
#     print('age invalid and ID okay')
# else:
#     print("not legal")

# ------------------------------------------------------------------------------------------------

text = input("enter text ").strip()
length = len(text)

if length > 10:
    result = text.lower()
else:
    result = text.upper()
    # title(), .capitalize(), strip()

print('Result', result)
