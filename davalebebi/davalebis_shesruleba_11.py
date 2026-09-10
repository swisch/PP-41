# =========================================
# დავალება 1 map() და lambda-ს გამოყენებით ლისტის თითოეული ელემენტი ავიყვანოთ კვადრატში


# numbers = []

# while len(numbers) < 5: # სანამ ლისტში 5 სწორი რიცხვი არ იქნება, პროგრამა გააგრძელებს მომხმარებლისგან რიცხვების მოთხოვნას.
#     try:
        
#         number = int(
#             input(f"შეიყვანეთ რიცხვი {len(numbers) + 1}/5: ") # len(numbers) ითვლის რამდენი რიცხვია უკვე ლისტში. + 1 გვიჩვენებს რომელი რიცხვი უნდა შეიყვანოს მომხმარებელმა.
#         )

#         numbers.append(number) # სწორად შეყვანილ რიცხვს ვამატებთ ლისტში.

#     except ValueError:
        
#         print("შეიყვანეთ ციფრი, არა ტექსტი. სცადეთ თავიდან.") # თუ მომხმარებელი რიცხვის ნაცვლად ტექსტს შეიყვანს, არასწორი მნიშვნელობა ლისტში არ დაემატება და 5 რიცხვის დათვლაშიც არ ჩაითვლება.


# try:
   
#     squared_numbers = list(map(lambda number: number ** 2, numbers)) # map() ლისტის თითოეულ ელემენტს გადასცემს lambda ფუნქციას. lambda თითოეულ რიცხვს აიყვანს კვადრატში.

#     print("შეყვანილი რიცხვები:", numbers)
#     print("კვადრატები:", squared_numbers)

# except Exception as error: # შეცდომის დამუშავება, თუ რაიმე მოულოდნელი შეცდომა მოხდება.
#     print("შეცდომა:", error)


# =========================================
# დავალება 2 - filter() და lambda-ს გამოყენებით დავაბრუნოთ მხოლოდ კენტი რიცხვები

# =========================================

# numbers = []

# while len(numbers) < 9: # სანამ ლისტში 9 სწორი რიცხვი არ იქნება, პროგრამა გააგრძელებს მომხმარებლისგან რიცხვების მოთხოვნას.
#     try:
        
#         number = int(
#             input(f"შეიყვანეთ რიცხვი {len(numbers) + 1}/9: ") # len(numbers) ითვლის რამდენი რიცხვია უკვე ლისტში. + 1 გვიჩვენებს რომელი რიცხვი უნდა შეიყვანოს მომხმარებელმა.
#         )

#         numbers.append(number) # სწორად შეყვანილ რიცხვს ვამატებთ ლისტში.

#     except ValueError:
        
#         print("შეიყვანეთ ციფრი, არა ტექსტი. სცადეთ თავიდან.") # თუ მომხმარებელი რიცხვის ნაცვლად ტექსტს შეიყვანს, არასწორი მნიშვნელობა ლისტში არ დაემატება და 5 რიცხვის დათვლაშიც არ ჩაითვლება.

# try:
#     number % 2 != 0 # ამოწმებს, არის თუ არა რიცხვი კენტი. თუ შედეგი არის True, filter() დატოვებს ელემენტს. თუ შედეგი არის False, filter() ამოიღებს ელემენტს.
#     odd_numbers = list(
#         filter(lambda number: number % 2 != 0, numbers))
    

#     print("შეყვანილი რიცხვები:", numbers)
#     print("კენტი რიცხვები:", odd_numbers)

# except Exception as error:
#     print("შეცდომა:", error)


# =========================================
# დავალება 3 map(), filter(), zip(), reduce()
# =========================================

# map() - სინტაქსი: map(function, collection)
# map() ფუნქციას იყენებს კოლექციის თითოეულ ელემენტზე ფუნქციის გასატარებლად.
# მაგალითი:

# numbers = [1, 2, 3]
# result = list(map(lambda x: x * 2, numbers)) #
# print(result) # შედეგი: [2, 4, 6]


# filter() - # სინტაქსი: filter(function, collection)
# filter() ამოწმებს თითოეულ ელემენტს. თუ ფუნქცია აბრუნებს True-ს, ელემენტი რჩება. თუ ფუნქცია აბრუნებს False-ს, ელემენტი იფილტრება.

# მაგალითი:
# numbers = [1, 2, 3, 4]
# result = list(filter(lambda x: x > 2, numbers))
# print(result) # შედეგი: [3, 4]


# zip() -  სინტაქსი: zip(collection_1, collection_2)
# zip() აერთიანებს კოლექციების ელემენტებს შესაბამისი ინდექსების მიხედვით.

# მაგალითი:
# names = ["Ani", "Luka"]
# scores = [90, 80]
# result = list(zip(names, scores))
# print(result) # შედეგი: [("Ani", 90), ("Luka", 80)]
# 


# reduce() - reduce() უნდა შემოვიტანოთ functools მოდულიდან: from functools import reduce

# სინტაქსი: reduce(function, collection) - reduce() ეტაპობრივად აერთიანებს ელემენტებს და საბოლოოდ აბრუნებს ერთ მნიშვნელობას.

# მაგალითი:
# numbers = [1, 2, 3, 4]
# result = reduce(lambda x, y: x + y, numbers)
# print(result) # შედეგი: 10

# მუშაობის პრინციპი:
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10



# =========================================
# დავალება 4 - რიცხვების კვადრატების ჯამი

# =========================================

# from functools import reduce

# numbers = [1, 2, 3, 4] #სტატიკურად განსაზღვრული რიცხვების ლისტი.

# try:
#     sum_of_squares = reduce(lambda result, number: result + number, # reduce() შეკრებს მიღებულ რიცხვებს result = 1 + 2 = 3, result = 3 + 3 = 6, (1. result = 6 + 4 = 10 (result = 1,  number = 4   → 5)), (2. result = 5,  number = 9   → 14), (3. result = 14, number = 16  → 30 )
#                             map(lambda number: number ** 2, numbers)) # map() თითოეულ რიცხვს აიყვანს კვადრატში: map = (1, 4, 9, 16)  

#     print("ციფრები:", numbers)
#     print("კვადრატების ჯამი:", sum_of_squares)

# except Exception as error:
#     print("შეცდომა:", error)


# =========================================
# დავალება 5
# map() + random + lambda
# =========================================

# import random

# scores = [10, 20, 30, 40, 50]

# try:
    
#     random_number = random.randint(1, 100) # randint(1, 100) აგენერირებს შემთხვევით რიცხვს 1-დან 100-მდე, ორივე ჩათვლით.
#     new_scores = list(map(lambda score: score + random_number, scores)) # map() თითოეულ score ელემენტს გადასცემს lambda-ს. lambda მიმდინარე ქულას უმატებს random_number-ს

#     print("რიცხვები:", scores)
#     print("შემთხვევითი რიცხვი:", random_number)
#     print("ჯამი : რიცხვი + შემთხვევითი რიცხვი:", new_scores)

# except Exception as error:
#     print("შეცდომა:", error)


# =========================================
# დავალება 6 :  5 შემთხვევითი რიცხვი + ინდექსის შეყვანა
# =========================================

# import random


# def get_random_number():
#     numbers = []

#     for i in range(5): # ვაგენერირებთ 5 შემთხვევით მთელ რიცხვს და ვამატებთ ლისტში.
#         numbers.append(random.randint(1, 100))

#     print("Generated list:", numbers)

#     while True:
#         try:
#             index = int(input("შეიყვანეთ ინდექსი 1-დან 5-მდე: ")) # მომხმარებელს შემოაქვს რიცხვი 1-დან 5-მდე.

            
#             # 
#             if index < 1 or index > 5: # ვამოწმებთ, არის თუ არა შეყვანილი რიცხვი 1-დან 5-მდე. თუ არა, 
#                 raise IndexError # ვაგზავნით IndexError-ს.
#             print("ციფრი:", numbers[index - 1]) # Python-ში ლისტის ინდექსები იწყება 0-დან. მომხმარებელი კი ითვლის 1-დან. ამიტომ შეყვანილ რიცხვს ვაკლებთ 1-ს:

#             break

#         except ValueError:
            
#             print("შეიყვანეთ ციფრი, არა ტექსტი. სცადეთ თავიდან.") # თუ მომხმარებელი რიცხვის ნაცვლად ტექსტს შეიყვანს.

#         except IndexError:
            
#             # დიაპაზონის გარეთ არსებულ რიცხვს.
#             print("შეიყვანეთ რიცხვი 1-დან 5-მდე. სცადეთ თავიდან.") # თუ შეიყვანილი რიცხვი ცდება 1-დან 5-მდე დიაპაზონს.


# get_random_number()

# =========================================
# დავალება 7
# საკუთარი raise მაგალითებით
# =========================================


# def check_age():

#     try:
        
#         age = int(input("შეიყვანეთ ასაკი: ")) # მომხმარებელს შემოაქვს ასაკი.

        
#         if age < 0: # ვამოწმებთ ასაკს. თუ ასაკი უარყოფითია, ვაგზავნით ValueError-ს.
#             raise ValueError("ასაკი არ შეიძლება იყოს უარყოფითი")
#         if age > 120:
#             raise ValueError("ზედმეტად დიდი ასაკი")
#         if age < 18:
#             raise ValueError(
#                 "თქვენ უნდა იყოთ 18 წლის მეტი"
#             )

        
#         print("დაშვებული ასაკი") # ეს ხაზი შესრულდება მხოლოდ მაშინ, თუ არცერთი raise არ გაეშვა.

#     except ValueError as error:
        
#         print("შეცდომა:", error) # აქ მოვა როგორც int() შეცდომა, ასევე ჩვენი ხელით შექმნილი ValueError-ები.

#     except Exception as error:
        
#         print("Unexpected error:", error) # სხვა მოულოდნელი შეცდომების დამუშავება.


# check_age()


# # =========================================
# # დამატებითი დავალება
# # საბანკო სისტემა გამონაკლისებით
# # =========================================

user_balances = {
    "Armen": 1000,
    "Ani": 500
}


def check_balance(username):

    
    if username not in user_balances: # ვამოწმებთ, არსებობს თუ არა მომხმარებელი.
        raise ValueError("მომხმარებელი არ არსებობს")

    
    print("ბალანსი:", user_balances[username]) # ბალანსის ჩვენება მომხმარებლისთვის.


def deposit(username):

    if username not in user_balances:
        raise ValueError("მომხმარებელი არ არსებობს")
    amount = float(input("შეიყვანეთ დეპოზიტის თანხა: ")) # მომხმარებელი შეიყვანს დეპოზიტის თანხას.

    
    if amount <= 0: # დეპოზიტის თანხა უნდა იყოს 0-ზე მეტი.
        raise ValueError(
            "დეპოზიტი უნდა იყოს 0-ზე მეტი"
        )

    
    user_balances[username] += amount # მომხმარებლის ბალანსს ვუმატებთ თანხას.

    print("დეპოზიტი წარმატებით შესრულდა")
    print("ახალი ბალანსი:", user_balances[username])


def withdraw(username):

    if username not in user_balances:
        raise ValueError("მომხმარებელი არ არსებობს")

    
    amount = float(input("შეიყვანეთ გასატანი თანხა: ")) # მომხმარებელი შეიყვანს გასატან თანხას.
    if amount <= 0: # გასატანი თანხა უნდა იყოს 0-ზე მეტი.
        raise ValueError(
            "გასატანი თანხა უნდა იყოს 0-ზე მეტი")

    if amount > user_balances[username]: # ვამოწმებთ, აქვს თუ არა მომხმარებელს საკმარისი თანხა ანგარიშზე. თუ არა, ვაგზავნით ValueError-ს.
        raise ValueError("არასაკმარისი ბალანსი")

    user_balances[username] -= amount # ბალანსიდან ვაკლებთ მითითებულ თანხას.

    print("გამოტანა წარმატებით შესრულდა")
    print("ახალი ბალანსი:", user_balances[username])


def main():

    while True: # პროგრამა იმუშავებს მანამდე, სანამ მომხმარებელი არ აირჩევს Exit-ს.

        try:
            username = input(
                "შეიყვანეთ მომხმარებლის სახელი: "
            ).strip()

            if username not in user_balances: # მომხმარებლის არსებობის შემოწმება.
                raise ValueError(
                    "მომხმარებელი არ არსებობს"
                )

            print("\n1 - ბალანსის შემოწმება")
            print("2 - დეპოზიტი")
            print("3 - გამოტანა")
            print("4 - გასვლა")

            choice = input(
                "აირჩიეთ მოქმედების ნომერი: "
            )

            if choice == "1":
                check_balance(username)

            elif choice == "2":
                deposit(username)

            elif choice == "3":
                withdraw(username)

            elif choice == "4":
                print("გასვლა პროგრამიდან")

                
                break # break აჩერებს while True ციკლს.

            else:
                print("Invalid operation")

        except ValueError as error:
            print("შეცდომა:", error)

        except Exception as error:
            print("გაუმართავი შეცდომა:", error)


main()
