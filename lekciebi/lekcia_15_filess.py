# files
# with open(location, mode):
# /, \\, r'\'

# read 
# def read_mode():
#     with open("C:/Users/PC/Desktop/test.txt", "r") as file:
#         content = file.read()
#         print(content)
# # read_mode()


# # xazis wakitxva 
# with open("C:/Users/PC/Desktop/test.txt") as file:
#     line_1 = file.readline()
#     line_2 = file.readline()
#     print(line_2)


# with open("C:/Users/PC/Desktop/test.txt", "r") as file:
#     line = file.readline()
#     while line:
#         print(line, end='')
        # line = file.readline()


# r+ wakitxvac da chawerac shemidzlia
# with open("C:/Users/PC/Desktop/test.txt", "r+") as file:
    # content = file.read()
    # print('Before Writing ', content)

    # file.seek(0)
    # file.write("New data axali danamati jadhgaj")

    # file.seek(0)
    # print("after readinf ", file.read())




# def write_in_existing_file():
#     try:
#         with open("C:/Users/PC/Desktop/test.txt", "w") as f:
#             f.write("n")
#         print("200 ok")
#     except FileNotFoundError:
#         print("file not found")
#     except Exception:
#         print("error")
# write_in_existing_file()


# def write_in_existing_file():
#     try:
#         with open("C:/Users/PC/Desktop/ani.txt", "w") as f:
#             f.write("es file ar arsevobda")
#         print("200 ok")
#     except FileNotFoundError:
#         print("file not found")
#     except Exception:
#         print("error")
# write_in_existing_file()



# def append_mode():
#     try:
#         with open("C:/Users/PC/Desktop/test.txt", "a") as f:
#             f.write("this will be added \n")
#         print("200 0k")
#     except Exception as e:
#         print(e)
# append_mode()


# ramdenime xazis wakitxva
# with open("C:/Users/PC/Desktop/test.txt", "r") as file:
#     data = file.readlines() # list
#     print(data)


# ramdenime xazis damateba
# data = ['pirveli\n', 'meore',"mesame"]
# with open("C:/Users/PC/Desktop/test.txt", "w") as f:
#     f.writelines(data)


# chasvma konkretul poziciaze
# def insert_line():
#     try:
#         with open("C:/Users/PC/Desktop/test.txt", 'r') as f:
#             lines = f.readlines()   # listia

#         # listze vaketeb moqmedebas da mere tavidan chavwer
#         lines.insert(1, "\n this is inserted\n")

#         # tavidan unda chavwero updated listi rom sheinaxos
#         with open("C:/Users/PC/Desktop/test.txt", "w") as file:
#             file.writelines(lines) 

#     except FileNotFoundError:
#         print("not fpund ")

# insert_line()




# delete - r + listi modify + w

# with open("C:/Users/PC/Desktop/test.txt", "r") as f:
#     lines = f.readlines()

# del lines[0]

# with open("C:/Users/PC/Desktop/test.txt", "w") as f:
#    f.writelines(lines)



file = open("C:/Users/PC/Desktop/test.txt", "r")
print(file.read())
file.close()

print(file.read())