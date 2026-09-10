# cvladi = "informacia"
# print(cvladi[::-1]) # string slicing 

# # string rac gaqvs eg gadaiyvano listad 
# # reverse -> list -> string

# # -----------------------------------------------------------------------------

# # ricxvi = 1243
# # str_ricxvi = str(ricxvi)
# # print(len(str_ricxvi))

# # list -> ordered , shecvladi 

# # --------------------------------------------------------------------------

# # dictionary - leqsikoni - dict
# # {key:value, key:value}
# # key unda iyos unikaluri
# # key - str, float, int, bool - hash rac aris 
# # value nebismieri shemidzlia ro iyos 

# cvladi = 'name'
# mnishvneloba = 'value'

# my_dict = {cvladi:"ani", 
#            "age":mnishvneloba, 
#            "city": "rame"
# }

# print(my_dict)

# -------------------------------------------------------------------------

# # dict()
# dict_2 = dict(name="ani", age=44, city='bla')
# print(dict_2)

# # ---------------------------------------------------------------------------

# # dicctionary comprehensions

# squared_numbers = {x : x ** 2 for x in range(1, 4)}
# # print(squared_numbers)

# # -----------------------------------------------------------------

# # my_dict = {'name': 'ani', 'age': 123, 'city': 'rame'} 

# # keys = my_dict.keys()
# # print(list(keys))

# # values = my_dict.values()
# # print(list(values))

# # my_dict = {'name': 'ani', 'age': 123, 'city': 'rame'} 

# # get()
# # age_value = my_dict.get("ages", "ver ipova shesabamisi") 
# # print(age_value)

# # print(my_dict['name'])

# # ----------------------------------------------------------------------
# # items = my_dict.items()
# # print(list(items))

# # my_dict = {'name': 'ani', 'age': 123, 'city': 'rame'} 
# # name = my_dict.pop('name')
# # print(my_dict)

# # name = my_dict.pop('names', 'not specified')
# # print(name)
# # print(my_dict)

# # ---------------------------------------------------

# my_dict = {'name': 'ani', 'age': 123, 'city': 'rame'} 
# my_dict['city'] = "axali qalaqi" # update
# print(my_dict)

# my_dict['axali'] = "axali data" # damaateba
# print(my_dict)

# # ------------------------------------------------------------------
# # nested
# nested_dicts = {
#     "person": {
#         "name":"ani",
#         "age":444
#     },
#     "address":{
#         "city":"tbilisi",
#         "code":123
#     }
# }
# print(nested_dicts["person"]["age"])

# # --------------------------------------------------------

# TUPLES - (), shereulad elementebis shenaxva, ucvleli koleqcia, ordered

# t1 = (1, "str", 5, True)
# print(t1)
# print(t1[0])


# t2 = "pirveli", "meore" # packing
# print(type(t2))

# t3 = tuple([1, 2, 3, 4] )
# print(t3)

# t4 = tuple("puythom")
# print(t4)

# single_element = (2, ) # ert e;lementiani tuples unda mdzime 
# print(type(single_element))

# t5 = tuple(s for s in range(6))
# print(t5)


my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple + (4, )
print(new_tuple)

my_tuple = my_tuple[1:3] + (87, ) + my_tuple[2:]
print(my_tuple)

# --------------------------------------------------------------------------

# sets - shecvladi, ar aqvt gansazghvruli wyoba  {}
# setshi duplikatebi "ar gamoaqvs"

# 
my_set = {1, 2, 2, 2, 3, "str", "str 2", 4, 5}
print(my_set)

my_set.add(509)
print(my_set)

my_set.update([12, 2], {3, 6})
print(my_set)

my_set.remove(509)
print(my_set)

# ----------------------------------------

set_a = {1, 2, 3}
set_b = {2, 4, 5}

gaertianeba = set_a | set_b
print(gaertianeba)

tanakveta = set_a & set_b
print(tanakveta)

sxvaoba = set_a - set_b
print(sxvaoba)



# ----------------------------------------------------------------------------------

# ლისტი - შერეულად შენახვა, განსაზღვრული წყობა, შეცვლადი, დუპლიკატები შემიძლია- []
# სეტი - შერეულად შენახვა, არ აქვს განსაზღვრული წყობა, შეცვლადი, დუპლიკატების დამატენა შემიძლია მაგრამ
# მაინც ერთხელ აჩვენს - {} - set()
# დიქტი - {გასაღები:მნიშვნელობა} - გასაღები არის უნიკალური და ველიუ ნებისმიერი შეიძლება იყოს
# გასაღები უნდა იყოს უცვლელი მონაცემთა ტიპი - განსაზღვრული წყობა აქვს  - {}
# tuples - შერეული შენახვა, განსაზღვრული წყობა, შეუცვლელი, დუპლიკატებიც შემიძლია  ()


set_1 = {1, 2}
set_2 = {2, 1}
print(set_2 == set_1)

