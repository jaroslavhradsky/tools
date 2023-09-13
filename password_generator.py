'''
File: password_generator.py
Author: Jaro Hradsky
Date: 2023-09-12
Description: Simple password generator. It generates 10 passwords of requested length and follows some rules
    - Password must contain at least one upper character
    - Password must contain at least one lower character
    - Password must contain at least one digit
    - Password must contain at least one symbol (some symbols are not allow, i.e. back slash)
    - Password must begin with a letter
'''

import string, random
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = '!#$%&()*+,-./:;<=>?@[]^_`{|}~'
possible_characters = (uppercase + lowercase) * 5 + digits * 3 + symbols 

def generate_password(length=64):
    password = []
    password.append(random.choice(uppercase)) # Ensure it contains uppercase
    password.append(random.choice(lowercase)) # Ensure it contains lower
    password.append(random.choice(digits)) # Ensure it contains digits
    password.append(random.choice(symbols)) # Ensure it contains symbols
    password += [random.choice(possible_characters) for _ in range(length-5)] # Generate the rest   
    random.shuffle(password) # Shuffle 
    return random.choice(lowercase+uppercase) + ''.join(password) # Ensure the first character is a letter

for i in range(10):
    print(generate_password(100))
