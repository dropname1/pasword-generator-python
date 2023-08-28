from random import randint
import array as arr
import time 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# def application():
#     app = QApplication(sys.argv)
#     window = QMainWindow()

#     window.setWindowTitle('Genlet - генератор паролей')
#     window.setGeometry(60,60,1000,1000)

#     window.show()
#     sys.exit(app.exec_())


# application()

passwords = []
password = ''

symbols = ['@','!','#','$','%','^','*','(','/','+','_','-']
letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

def standart_password (amount_passwords = 1, password_length = 8, is_simbols = True, is_up_letters = True, is_low_letters = True): 
    is_numbers = True   
    while amount_passwords > 0: 
        current_password_length = password_length
        password = ''
        while current_password_length > 0:
            if is_numbers and current_password_length > 0: 
                password += str(randint(0,9))
                current_password_length = current_password_length - 1

            if is_simbols and password_length > 0: 
                password += symbols[randint(0,len(symbols)-1)]
                current_password_length = current_password_length - 1

            if is_low_letters and current_password_length > 0: 
                password += letters[randint(0,len(letters)-1)]
                current_password_length = current_password_length - 1

            if is_up_letters and current_password_length > 0: 
                password += letters[randint(0,len(letters)-1)].upper()
                current_password_length = current_password_length - 1
        passwords.append(password)
        amount_passwords = amount_passwords - 1

def standart_plus_password (amount_passwords = 1, password_length = 8, is_simbols = True, is_up_letters = True, is_low_letters = True , is_numbers = True):
    password_step = 2
    while amount_passwords > 0: 
        current_password_length = password_length
        password = ''
        while current_password_length > 0:
            for i in range(password_step):
                if is_numbers and current_password_length > 0: 
                    password += str(randint(0,9))
                    current_password_length = current_password_length - 1

            for i in range(password_step):
                if is_simbols and current_password_length > 0: 
                    password += symbols[randint(0,len(symbols)-1)]
                    current_password_length = current_password_length - 1

            for i in range(password_step):
                if is_low_letters and current_password_length > 0: 
                    password += letters[randint(0,len(letters)-1)]
                    current_password_length = current_password_length - 1

            for i in range(password_step):
                if is_up_letters and current_password_length > 0: 
                    password += letters[randint(0,len(letters)-1)].upper()
                    current_password_length = current_password_length - 1

        passwords.append(password)
        amount_passwords = amount_passwords - 1

def random_style_password (amount_passwords = 1, password_length = 8, is_simbols = True, is_up_letters = True, is_low_letters = True , is_numbers = True):
    position = ['number','symbol','uppercase_letter','lowercase_letter']
    while amount_passwords > 0: 
        current_password_length = password_length
        password = ''
        while current_password_length > 0:
            random_num = randint(0,len(position)-1)
            if position[random_num] == 'number': 
                password += str(randint(0,9))

            elif position[random_num] == 'symbol': 
                password += symbols[randint(0,len(symbols)-1)]

            elif position[random_num] == 'lowercase_letter': 
                password += letters[randint(0,len(letters)-1)]

            elif position[random_num] == 'uppercase_letter': 
                password += letters[randint(0,len(letters)-1)].upper()
            current_password_length = current_password_length - 1
        passwords.append(password)
        amount_passwords = amount_passwords - 1

def random_plus_style_password (amount_passwords = 1, password_length = 8, is_simbols = True, is_up_letters = True, is_low_letters = True , is_numbers = True):
    password_count = 0

    priority_positions = {
    'number' : 0,
    'symbol' : 0,
    'uppercase_letter' : 0,
    'lowercase_letter' : 0,
    }
    while amount_passwords > 0: 
        current_password_length = password_length
        password = ''
        while current_password_length > 0:
            priority_positions['number'] = randint(0,100)
            priority_positions['symbol'] = randint(0,80)
            priority_positions['lowercase_letter'] = randint(0,80)
            priority_positions['uppercase_letter']= randint(0,100)

            max = priority_positions['number']
            max_key = 'number'

            for key in priority_positions:
                if max < priority_positions[key]:
                    max = priority_positions[key]
                    max_key = key

            if max_key == 'number': 
                password += str(randint(0,9))
            elif max_key == 'symbol': 
                password += symbols[randint(0,len(symbols)-1)]
            elif max_key == 'lowercase_letter': 
                password += letters[randint(0,len(letters)-1)]
            elif max_key == 'uppercase_letter': 
                password += letters[randint(0,len(letters)-1)].upper()
            current_password_length = current_password_length - 1

        passwod_has = {
                'has_simbol' : None,
                'has_number' : None,
                'has_lower_letter' : None,
                'has_upper_letter' : None,
            }

        for password_item in password:

            for symbols_item in symbols:
                if symbols_item == password_item:
                    passwod_has['has_simbol'] = True

            for number_item in [0,1,2,3,4,5,6,7,8,9]:
                if str(number_item) == password_item:
                    passwod_has['has_number'] = True

            for lower_letter_item in letters:
                if lower_letter_item == password_item:
                    passwod_has['has_lower_letter'] = True

            for upper_letter_item in letters:
                if upper_letter_item.upper() == password_item:
                    passwod_has['has_upper_letter'] = True

        count = 0
        for item in passwod_has:
            if passwod_has[item] == True:
                count = count + 1
        if count == len(passwod_has):
            password_count = password_count + 1
            passwords.append(password)
        else:
            password_count = password_count + 1
            amount_passwords = amount_passwords + 1
        amount_passwords = amount_passwords - 1

def password_questions():
    length = int(input('Длинна пароля: '))
    symbol = input('Нужны символы в пароле ? (да/нет): ')
    upper = input('Нужны заглавные буквы в пароле ? (да/нет): ')
    letter = input('Нужны строчные буквы в пароле ? (да/нет): ')
    setting = input('Сгенирировать стандартный пароль (напишите: с) или настраиваемый (напишите: н) ?: ')

    if symbol == 'да':
        symbol = True
    else: 
        symbol = False

    if upper == 'да':
        upper = True
    else: 
        upper = False

    if letter == 'да':
        letter = True
    else: 
        letter = False

    if setting == 'с':
        standart_password (1,length,symbol,upper,letter)
        print("_________________________")
        time.sleep(0,5)
        print(passwords)
        print("_________________________")
    elif setting == 'н':
        amount = int(input('Количестово паролей: '))
        style = input('Выбирите стиль генерации пароля: \n 1) Cтандарт-плюс (напишите с+) \n 2) "Position style" (напишите п-с) \n 3)"Position style plus" (напишите п-с+)')

        if style == 'с+':
            standart_plus_password(amount,length,symbol,upper,letter)
        elif style == 'п-с':
            random_style_password(amount,length,symbol,upper,letter)
        elif style == 'п-с+':
            random_plus_style_password(amount,length,symbol,upper,letter)

        print("_________________________")
        time.sleep(0.5)
        print(passwords)
        print("_________________________")

password_questions()