# დავალება 1 -- გაქვთ მოცებული ორი ლექსიკონი, 

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}

# new_dict = {}  # 

# for key, value in dict1.items(): #
#     new_dict[key] = value

# for key, value in dict2.items():

#     if key in new_dict:
#         new_dict[key] = [new_dict[key], value]
#     else:
#         new_dict[key] = value

# print(new_dict)

# --------------------------

# დავალება 2 : lst = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
# აღნიშნული ლისტიოსთვის შექმენით ლექსიკონი, რომელიც შეინახავს key-ში ლექსიკონის სტრინგს და value-დ მიიღებს მნიშვნელობას, რომელშიც შენახულია რამდენჯერ გვხვდება აღნიშნული სტრინგი ლისტში


# lst = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana'] # მოცემული ლისტი

# new_dict = {}  #

# for word in lst:
#     if word in new_dict:
#         new_dict[word] = new_dict[word] + 1
#     else:
#         new_dict[word] = 1

# print(new_dict)


# # დავალება 3 - მოცემული ლექსიკონისთვის შეამოწმეთ არსებობს თუ არა key my_dictში, თუ არა დაამატეთ მასში key : default_value წყვილი
# my_dict = {'a': 10, 'b': 20}

# key = 'c'
# default_value = 30

# if key not in my_dict:
#     my_dict[key] = default_value

# print(my_dict)

# დავალება 4 -  შექმენით ახალი ლექსიკონი, სადაც მოცემული ლექსიკონის გასაღებები გახდებიან მნიშვნელობები და პირიქით

# my_dict = {'a': 1, 'b': 2, 'c': 3}

# new_dict = {}

# # შევცვალეთ key და value ადგილებით
# for key, value in my_dict.items():
#     new_dict[value] = key

# print("შეცვლილი ლექსიკონი:", new_dict)


# old_dict = {}

# # გადაგვაქ ისევ პირველ პოზიციაზე
# for key, value in new_dict.items():
#     old_dict[value] = key

# print("საწყისი ლექსიკონი:", old_dict)

# # დავალება 5 - მოცემული ლექსიკონიდან წაშალეთ წყვილი, რომლისთვისაც მნიშვნელობა არის None

# my_dict = {'a': 1, 'b': None, 'c': 3, 'd': None}

# new_dict = {}

# for key, value in my_dict.items():
#     if value != None:
#         new_dict[key] = value

# print(new_dict)

# # დავალება 6 - მოცემულ ლისტზე დაყრდნობით, შექმენით ლექსიკონი, რომელშიც გასაღები იქნება მოცემული სტრინგების პირველი ასო და მნიშვნელობად მიიღებენ სტრინგებს, რომლებიც იწყებიან ამ ასოზე

# words = ['apple', 'banana', 'avocado', 'blueberry', 'cherry', 'carrot']

# new_dict = {} 

# for word in words:   # გავუშვით ციკლი
#     first_letter = word[0] #

#     if first_letter in new_dict:
#         new_dict[first_letter].append(word)
#     else:
#         new_dict[first_letter] = [word]

# print(new_dict)

# # დავალება 7 - დაასორტირეთ მოცემული ლექსიკონი მნიშვნელობების მიხედვით.

# my_dict = {'a': 5, 'b': 1, 'c': 8, 'd': 3}

# new_dict = {}

# while len(my_dict) > 0:
#     min_key = None
#     min_value = None

#     for key, value in my_dict.items():
#         if min_value == None or value < min_value:
#             min_value = value
#             min_key = key

#     new_dict[min_key] = min_value
#     my_dict.pop(min_key)

# print(new_dict)

