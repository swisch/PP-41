# while condition: -> True

# count = 1
# while count <= 7:
#     print(count)
#     count += 1

# while True:
#     print("hello")

# ----------------------------------------------------------------


# კოლექცია - list, tuple, dictionary, set

# list - ["el1", 2, 6.8, True] - განსაზღვრuლი წყობის - შეცვლადი

# text = "stringi arisraghaca"
# print(text.split(" "))


# my_list = [1, 3, 5,  2, 3, 4, 5, "meeqvse", True]
# # print(type(my_list))
# print(my_list)


# # list comprehensions
# arr = [i for i in range(0, 9)]
# print(arr)
# # for i in range()

# my_list_2 = list(range(10))
# print(my_list_2)

# --------------------------------------------------------------------

# array vs list 

# ---------------------------------------------------------------------

# listi = [1, 2, 3, 'string']
# print(listi)

# append - elementis damateba
# listi.append(5)
# print(listi)

# # extend
# listi.extend([2, 3, 4])
# print(listi)

# listi = [1, 2,  3, 2, 'string']

# insert(index, value)
# listi.insert(2, "mnishvneloba")
# print(listi)

# remove(value)

# listi.remove(2)
# print(listi)

# listi = [1, 2,  3, 2, 'string']
# pop()
# listi.pop() # defaultad shlis bolo elements 
# print(listi)

# tu carielia mashin bolo elements shlis da tu rames vwers=t es aris index
# index-ebi marcxnidan marjvniv aris minusebit - bolo elementi aris -1,
# bolos wina -2 da ase shemdeg

# listi.pop(3) 
# print(listi)



# listi = [1, 2,  3, 2, 'string']
# # index(value)
# print(listi.index(2))


# print(listi.count(20))


# ----------------------------------------------------

# num_listi = [4, 6, 2, 8, 9]
# num_listi.sort() # zrdadobit
# print(num_listi)

# num_listi.sort(reverse=True) # kldebadoba
# print(num_listi)

# num_listi.reverse()
# print(num_listi)

# # klebadobit dalageba sort+reverse
# num_listi.sort()
# num_listi.reverse()
# print(num_listi)


# num_listi = [4, 6, 2, 8, 9]
# num_listi.clear()
# print(num_listi)


# carieli = []
# carieli.append(1)
# print(carieli)


# num_listi = [4, 6, 2, 8, 9]
# copy_arr = num_listi.copy()
# print(copy_arr)


list_numbers = [3, 5, 7, 89]
# total = sum(list_numbers)
# print(total)


# total = 0
# for num in list_numbers:
#     total += num
#     # print(total)

# print(total)
# average = total // len(list_numbers)
# print(average)


# ---------------------------------------------

list_numbers = [3, 5, 7, 89]
print(40 in list_numbers)
print(3 in list_numbers)

print(40 not in list_numbers)

# ---------------------------------------------------------------------

# elementis dzieba

# fruits = ['apple', 'pear', 'cherry', 'banana']
# target = input("enter fruit to find: ").strip().lower()

# for i in range(len(fruits)):
#     if fruits[i].lower() == target:
#         print(f"element found at index {i}")
#         break
# else:
#     print("element not found")


fruits = ['apple', 'pear', 'cherry', 'banana']
fruits.sort()
print(fruits)