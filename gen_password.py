# Имеет длину больше 10 символов
# Не имеет простой последовательности цифр или символов (12345, qwerty)
# Строчные и заглавные буквы на разных языках
# Содержит прочие знаки (!, +, -, № …)

import random
import string

number = int(input('количество паролей?'+ "\n"))
length = int(input('длина пароля?'+ "\n"))

def generate_password(length):
    if length < 10:
        raise ValueError('Длина пароля должна быть не менее 10 символов')

    chars = string.ascii_letters + string.digits + string.punctuation
    
    while True:
        password = ''.join(random.choice(chars) for _ in range(length))
        
        if (any(char.isdigit() for char in password) and
            any(char.islower() for char in password) and
            any(char.isupper() for char in password) and
            any(char in '!+-@#$?<>*' for char in password)):
            return password

def check_password_strength(password):
    if len(password) < 10:
        print('Должен быть длиннее 10 символов')
        return 'Слабый'
    if not any(char.isdigit() for char in password):
        print('Должен содержать хотя бы одну цифру')
        return 'Слабый'
    if not any(char.islower() for char in password):
        print('Должен содержать хотя бы одну строчную букву')
        return 'Слабый'
    if not any(char.isupper() for char in password):
        print('Должен содержать хотя бы одну заглавную букву')
        return 'Слабый'
    if not any(char in string.punctuation for char in password):
        print('Должен содержать хотя бы один специальный символ')
        return 'Слабый'
    return 'Надежный'

for _ in range(number):
    password = generate_password(length)
    check = check_password_strength(password)
    print(password, check)
    
input("Введите свой пароль для проверки на надежность: ")
print(check_password_strength(password))