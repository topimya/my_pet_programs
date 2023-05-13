from time import sleep

def ang(sdvig):
    sleep(1)
    stroka = input('Введите строку: ')
    while sdvig > 26:
        sdvig -= 26
    for c in stroka:
        if 32 <= ord(c) <= 64 or 91 <= ord(c) <= 96 or 123 <= ord(c) <= 127:
            print(c, end ='')
        else:
            buk = ord(c) + sdvig
            if (buk < 97 and c.islower()) or (buk < 65 and c.isupper()):
                buk += 26
            elif (buk > 90 and c.isupper()) or (buk > 122 and c.islower()):
                buk -= 26
            print(chr(buk), end ='')
    print('\nХотите еще раз? "да"/"нет" ')
    asw = input()
    if asw in ['lf', 'lf ', 'да', 'да ']:
        while True:
            n = input('\nВведите "д" или "ш": ')
            if n in ['l', 'l ', 'д', 'д ', 'i', 'i ', 'ш', 'ш ']:
                cezar(n)
                break
            else:
                print('Повторите, пожалуйста.')
    else:
        return print('Возвращайтесь! :)')   

def rus(sdvig):
    sleep(1)
    stroka = input('Введите строку.\n!!!Подалуйста исключите "ё" иначе резуьтат может быть не корректным!!!\n')
    while sdvig > 32:
        sdvig -= 32
    for c in stroka:
        if 32 <= ord(c) <= 64 or 91 <= ord(c) <= 96 or 123 <= ord(c) <= 127:
            print(c, end ='')
        else:
            buk = ord(c) + sdvig
            if (buk < 1072 and c.islower()) or (buk < 1040 and c.isupper()):
                buk += 32
            elif (buk > 1103 and c.islower()) or (buk > 1071 and c.isupper()):
                buk -= 32
            print(chr(buk), end ='')
    print('\nХотите еще раз? "да"/"нет" ')
    asw = input()
    if asw in ['lf', 'lf ', 'да', 'да ']:
        while True:
            n = input('\nВведите "д" или "ш": ')
            if n in ['l', 'l ', 'д', 'д ', 'i', 'i ', 'ш', 'ш ']:
                cezar(n)
                break
            else:
                print('Повторите, пожалуйста.')
    else:
        return print('Возвращайтесь! :)')   

def cezar(znak):
    while True:
        sdvig = input('Введите шаг сдвига: ').split()
        if sdvig[0].isdigit() == False:
            print('Введите положительное число, пожалуйста.')
        elif len(sdvig) != 1:
            print('Введите одно число, пожалуйста.')
        elif int(sdvig[0]) <= 0:
            print('Введите положительное число, пожалуйста.')
        else:
            break
    if n in ['l', 'l ', 'д', 'д ']:
        sdvig[0] = int(sdvig[0]) * (-1)
    sleep(1)
    print('Выберети язык.\nВведите "рус" или "англ": ')
    while True:
        s = input()
        if s in ['fyuk', 'fyuk ', 'англ', 'англ ']:
            ang(int(sdvig[0]))
            return
        elif s in ['hec', 'hec ', 'рус', 'рус ']:
            rus(int(sdvig[0]))
            return
        else:
            print('Повторите, пожалуйста.')

print('Привет, я программа шифровки и дешифровки шифра Цезаря.\nВы можете ввести строку на английском или русском.\nВыберете дишифровать или шифровать.')
sleep(2)
while True:
    n = input('\nВведите "д" или "ш": ')
    sleep(1)
    if n in ['l', 'l ', 'д', 'д ', 'i', 'i ', 'ш', 'ш ']:
        cezar(n)
        break
    else:
        print('Повторите, пожалуйста.')
    