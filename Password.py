from random import *
from time import sleep

def game(number):
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = "!#$%&*+-=?@^_"
    all_chars = []
    password = ''
    digit, big, small, char = 0, 0, 0, 0
    print('Требуемое количество символов в пароле:')
    while True:
        length = input().split()
        if length[0].isdigit() == False:
            print('Введите цифру, пожалуйста:')
        elif len(length) > 1:
            print('Введите одну цифру пожалуйста:')
        else:
            break
    print('Включать цифры в пароли? да/нет:')
    if input() in ['да', 'да ', 'lf', 'lf ']:
        digit = 1
        all_chars.append(digits)
    print('Включать в пароль прописные буквы? да/нет:')
    if input() in ['да', 'да ', 'lf', 'lf ']:
        big = 1
        all_chars.append(uppercase_letters)
    print('Включать в пароль строчне буквы? да/нет:')
    if input() in ['да', 'да ', 'lf', 'lf ']:
        small = 1
        all_chars.append(lowercase_letters)
    print('Включать в пароль знаки? да/нет:')
    if input() in ['да', 'да ', 'lf', 'lf ']:
        char = 1
        all_chars.append(punctuation)        
    if digit == 0 and big == 0 and small == 0 and char == 0:
        print('Нет символов для поролей')
    else:
        for i in range(int(number[0])):
            for j in range(int(length[0])):
                stri = choice(all_chars)
                password += stri[randint(0, len(stri) - 1)]
            sleep(1)
            print(password)
            password = ''
    sleep(1)
    print('\nХотите сгенерировать еще раз? да/нет: ')
    if input() in ['да', 'да ', 'lf', 'lf ']:
        sleep(1)
        game(pr_number())
    else:
        return print('Хорошо, возвращайтесь')
        

        
        
        

def pr_number():
    print('Введите сколько паролей хотите сгенерировать: ')
    while True:
        number = input().split()
        if number[0].isdigit() == False:
            print('Введите число, пожалуйста:\n')
        elif len(number) > 1:
            print('Введите одну цифру пожалуйста:')
        else:
            print('Принято.')
            sleep(1)
            return number


print('Привет, я генератор безопасных паролей :).\n')
sleep(1)
game(pr_number())

