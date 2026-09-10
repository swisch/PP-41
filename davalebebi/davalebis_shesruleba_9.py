# დავალება 1 - დაწერეთ ფუნქცია find_max(), რომელიც არგუმენტად იღებს რიცხვების სიას და აბრუნებს სიიდან ყველაზე დიდ რიცხვს.

# def find_max(numbers):
#     max_number = numbers[0] # სიის პირველ ელემენტს დროებით ვთვლით ყველაზე დიდ რიცხვად

#     for number in numbers: # for ციკლის საშუალებით სათითაოდ გადავუვლით numbers სიაში არსებულ ყველა რიცხვს
#         if max_number < number: # თუ მიმდინარე number უფრო დიდია, ვიდრე max_number 
#             max_number = number # max_number-ში ვინახავთ ახალ, უფრო დიდ რიცხვს

#     return max_number


# numbers = [2, 8, 4, 1, 7] # ვქმნით რიცხვების სიას

# result = find_max(numbers)

# print(f"ყველაზე დიდი რიცხვია: {result}")

# -------------------------------------------

# დავალება 2 - დაწერეთ ფუნქცია sum_of_evens(ნომრები), რომელიც აბრუნებს ყველა ლუწი რიცხვის ჯამს მთელი რიცხვების სიიდან.

# def sum_of_evens(numbers):
#     total = 0 # ვქმნით total ცვლადს და საწყის მნიშვნელობად ვაძლევთ 0-ს , ამ ცვლადში ეტაპობრივად შევინახავთ ლუწი რიცხვების ჯამს

#     for number in numbers: # for ციკლით სათითაოდ გადავუვლით numbers სიაში არსებულ ყველა რიცხვს
#         if number % 2 == 0:  # ვამოწმებთ, არის თუ არა რიცხვი ლუწი
#             total = total + number # მის მნიშვნელობას ვუმატებთ total-ს

#     return total # როდესაც ციკლი დასრულდება, total-ში იქნება ყველა ლუწი რიცხვის ჯამი return-ით მიღებულ შედეგს ვაბრუნებთ ფუნქციიდან


# result = sum_of_evens([1, 2, 3, 4, 5]) # ფუნქციას არგუმენტად გადავცემთ რიცხვების სიას, ფუნქციის დაბრუნებულ შედეგს ვინახავთ result ცვლადში
# print(result)

# დავალება 3 - დაწერეთ ფუნქცია count_occurrences (), რომელიც აბრუნებს რამდენჯერ გამოჩნდება მითითებული ელემენტი  სიაში.

# def count_occurrences(numbers, target): # ფუნქციას აქვს ორი პარამეტრი: numbers - რიცხვების სია და target - ელემენტი, რომლის რაოდენობაც უნდა დავითვალოთ
#     count = 0 # ვქმნით count ცვლადს.

#     for number in numbers: # for ციკლით სათითაოდ გადავუვლით numbers სიაში არსებულ ყველა ელემენტს
#         if number == target: # ვამოწმებთ, უდრის თუ არა მიმდინარე number იმ ელემენტს, რომელსაც ვეძებთ - target-ს
#             count = count + 1 # თუ number და target ტოლია, count-ს ვუმატებთ 1-ს

#     return count # როდესაც for ციკლი დასრულდება, count-ში იქნება target-ის გამოჩენის რაოდენობა. return-ით მიღებულ შედეგს ვაბრუნებთ ფუნქციიდან


# result = count_occurrences([1, 2, 2, 3, 2], 2) # ფუნქციას გადავცემთ ორ არგუმენტს: [1, 2, 2, 3, 2] - სია, რომელშიც ვეძებთ და 2 - ელემენტი, რომლის რაოდენობაც უნდა დავითვალოთ
# print(result)

#----------------------------------------------

# დავალება 4 - დაწერეთ პროგრამა, რომელიც ითვლის სტუდენტის საბოლოო შეფასებას მათი გამოცდის ქულების მიხედვით, შემდეგ დაყოფს ქულებს ერთ-ერთ შემდეგ კატეგორიად:

# def calculate_average(grades): #  ამ ფუნქციის მიზანია მიიღოს შეფასებების სია და გამოთვალოს საშუალო ქულა.
#     total = 0 # ცვლადში ვინახავთ შეფასებების ჯამს.

#     for grade in grades: # ციკლი სათითაოდ იღებს თითოეულ შეფასებას
#         total = total + grade # ქულების ჯამის გამოთვლა

#     average = total / len(grades) # გამოთვლილი ჯამი გაყოფილი შეყვანილის შეფასების რაოდენობაზე

#     return average


# def determine_grade(average_score): # ეს ფუნქცია იღებს საშუალო ქულას და განსაზღვრავს შესაბამის შეფასებას.

#     if average_score >= 90:
#         return "A"

#     elif average_score >= 80:
#         return "B"

#     elif average_score >= 70:
#         return "C"

#     elif average_score >= 60:
#         return "D"

#     else:
#         return "F"


# def determine_level(average_score): # ეს ფუნქცია საშუალო ქულის მიხედვით განსაზღვრავს შედეგის დონეს

#     if average_score >= 90:
#         return "მაქსიმალური შედეგი"

#     elif average_score >= 60:
#         return "საშუალო შედეგი"

#     else:
#         return "მინიმალური შედეგი"


# def get_student_result(grades): # აქ ერთი ფუნქცია იყენებს სხვა ფუნქციების შედეგებს.
#     average = calculate_average(grades)
#     grade = determine_grade(average)
#     level = determine_level(average)

#     return average, grade, level # ფუნქცია ერთდროულად აბრუნებს სამ შედეგს.


# while True: # აქ წერია სტუდენტის სახელის შეყვანა და შემოწმება
#     name = input("შეიყვანეთ სახელი : ").strip().capitalize() # ვასწორებთ სახელს სწორ ფორმაში

#     if name.isalpha(): # ამოწმებს, შედგება თუ არა ტექსტი მხოლოდ ასოებისგან
#         break # თუ სახელი სწორია
#     else: # თუ არა მაშინ მოითხოვს სწორ ფორმას.
#         print("სახელი არასწორად არის შეყვანილი")
#         print("შეიყვანეთ სახელი სწორად")


# while True: # იგივე პროცედურაა რაც ზევით იყო
#     surname = input("შეიყვანეთ გვარი : ").strip().capitalize()

#     if surname.isalpha():
#         break
#     else:
#         print("გვარი არასწორად არის შეყვანილი")
#         print("შეიყვანეთ გვარი სწორად")


# while True: # შეფასებების რაოდენობის შეყვანა
#     try:
#         count = int(input("შეიყვანეთ შეფასებების რაოდენობა : "))

#         if count <= 0: # თუ რაოდენობა არასწორი ფორმატშია ამოაგდებს შეცდომას და მოითხოვს სწორ შედეგს.
#             raise ValueError

#         break

#     except ValueError:
#         print("შეცდომა! შეიყვანეთ დადებითი მთელი რიცხვი")


# grades = []

# while len(grades) < count: # შეფასებების სიაში დამატება
#     try:
#         grade = int(input("შეიყვანეთ შედეგი : "))

#         if grade < 0 or grade > 100: # შედეგის შემოწმება 0-100
#             raise ValueError

#         grades.append(grade) # append() მხოლოდ მაშინ შესრულდება, თუ შეფასება სწორია.

#     except ValueError:
#         print("შეცდომა! შეიყვანეთ რიცხვი 0-დან 100-მდე")


# average, grade, level = get_student_result(grades) # საბოლოო შედეგის მიღება


# print("===== სტუდენტის შედეგი =====")
# print(f"სახელი: {name}")
# print(f"გვარი: {surname}")
# print(f"ნიშნები: {grades}")
# print(f"საშუალო ქულა: {average}")
# print(f"შეფასება: {grade}")
# print(f"შეფასების დონე: {level}")
# print("============================")