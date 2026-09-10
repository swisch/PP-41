# # @decorator_name
# # function_1

# import time
# # original function + decorator -> shecvlil function

# def decorator_name(func):
#     def wrapper():
#         current_time = time.time()
#         print(f"current time: {current_time}")
#         func()
#         print(f"executed: {time.time() - current_time}")

#     return wrapper

# @decorator_name
# def rame():
#     print("hello world")

# rame()
# # decorator(rame)

# # decoratori amaze aghar vrceldeba 

# def meore():
#     print("bl;abla")
# meore()



# # -----------------------------------------------------------------------------

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("function started")
#         result = func(*args, **kwargs)
#         print("function finished")
#         return result

#     return wrapper

# @decorator_name
# def function_name(x, y):
#     print("arguments", x, y)

# # function_name('x', 'y')

# function_name('x', 'y')

# ----------------------------------------------------------------------------------

# decorator - function romelsac vwert rogorc chveulebriv functions
# def decorator_name(func):
#     def wrapper(*args, **kwargs):
#         # function body
#     return wrapper

# @decorator_name   #  -> es gavrceldeba mxolod chemi_function-ze imis qvemot aghar
# def chemi_function():

# # ----------------------------------------------------------------------------------

# def decorator_first(func):
#     def wrapper():
#         print("Function start")
#         func()

#     wrapper.version = 1
#     wrapper.developer = 'DEV'

#     return wrapper

# @decorator_first
# def hello():
#     print('function hello ', hello.developer)
# hello()

# print(hello.developer)
# print(hello.version)


# # ----------------------------------------------------------------------------------

# nested function
# import math

# recursion -> 

def math_operation(x):
    def power():
        return x ** x
    print(power())

math_operation(5)

# -------------------------------------------------------------------------------------------

def student_portal(student_name, grades):   # grades list

    # grade validator - 100ze meti ara
    def validate_grade():
        try:
            if not grades: # tu list carielia
                raise ValueError("Grade can not be empty")

            for g in grades:
                if g > 100 or g < 0:
                    raise ValueError("grade can not be negative or > 100")

            # return 
        except ValueError as e:
            print(f"Validation Error: {e}")
            # return 

    def calculate_total():
        try:
            return sum(grades)
        except TypeError:
            print("Error: grade must be numeric")

    def average_grade(total):
        try:
            return total / len(grades)
        except ZeroDivisionError:
            print("Division By 0")

    def get_grade(average):
        try:
            if average >= 90:
                return 'A'
            elif average >= 80:
                return 'B'
            else:
                return 'F'
        except TypeError:
            print("average grade must be number")


    print('Student', student_name)
    total = calculate_total()

    average = average_grade(total)
    grade = get_grade(average)

    print("total ", total)
    print(f"average  {average:.0f}")   # math.round(54.78)
    print("grade ", grade)

# student_portal("student_name", [54, 67, 89])
if __name__ == "__main__":
    student_portal("student_name", [54, 67, 89])
    

print( __name__ == "__main__") 


