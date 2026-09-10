# modules, venv , requirements.txt
# modules , library(modules)

# virtualuri garemo -> install -> 

# string module
# import string 
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

import random
import string
import mypy

def generate_strong_password(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for char in range(length):
        password += random.choice(characters)

    return password

def main():
    length = int(input("Enter your pass length: "))

    if length < 8:
        print("password must be at least 8 chars" )

    else:
        result = generate_strong_password(length)
        print('Generated password ' + result)

main()




# ---------------------------------------------------------------------------------------------------------------

for _ in range(7):
    print("hello")
