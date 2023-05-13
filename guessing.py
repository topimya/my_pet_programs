from random import *


def game(d):
    too_much =['Слишком много!', 'Много!', 'Эх, слишком много', 'Давай еще раз, слишком много', 'Может еще раз? Много']
    too_little = ['Слишком мало!', 'Мало!','Не, мало, давай еще', 'Маловато', 'Мало. Надо еще']
    enough = ['Ура, ты угадал', 'Ура, это оно', 'Получилось! Ты угадал', 'Превосходно, это оно!', 'Супер! Ты угадал']
    minus = d[1]
    d = d[0]
    x = int(d[0])
    y = int(d[1])
    if minus == 1:
        x *= -1
        y *= -1
    if x > y:
        number = randint(y, x)
        print(f'Загаданное число от {y} до {x}')
    else:
        number = randint(x, y)
        print(f'Загаданное число от {x} до {y}')
    while True:
        m1 = 0
        num1 = input()
        if '-' in num1:
            num1 = num1.replace('-', '')
            m1 = 1
        if num1.isdigit() == False:
            print('Это же не число :(')
            continue
        num1 = int(num1)
        if m1 == 1:
            num1 *=-1
        if num1 == number:
            print(choice(enough))
            break
        elif num1 > number:
            print(choice(too_much))
        else:
            print(choice(too_little))
    if input('Хочешь сыграть еще раз? Напиши "готов", если да:\n') in  ['готов', 'ujnjd', 'готов ', 'ujnjd ']:
        game(proverka())
    else:
        return print('Спасибо за игру! Возвращайся :)')


def proverka():
    too_little = ['Так не интересно :) Давай больше', 'Больше!', 'Маловато будет, быстро закончим', 'Можно и побольше взять']
    too_mach = ['Так долго сидеть мы не сможем :( Давай меньше', 'Много слишком, давай поменьше', 'Очень много, давай сделаем меньше', 'А надо было выбирать диапазон больше']
    print('Хотите выбрать максимальный диапазон?\nВведите "да" или "нет"')
    while True:
        diap = input()
        if diap in ['да', 'lf', 'да ', 'lf ']:
            diap = diapazon()
            break
        elif diap in ['нет', 'ytn', 'нет ', 'ytn ']:
            diap = 1000
            break
        else:
            print('Повторите, пожалуйста')
    print('Хорошо, тогда введи диапазон')
    while True:
        minus = 0
        d = input()
        if '-' in d:
            d = d.replace('-', '')
            minus = 1
        d = d.split()
        if len(d) > 2 or len(d) == 1:
            print('Так не пойдет, задай еще раз, нужно две цифры')
            minus = 0
        elif (d[0].isdigit() == False or d[1].isdigit() == False):
            print('Только цифры, пожалуйста :)')
            minus = 0
        elif abs(int(d[0]) - int(d[1])) <= 20:
            print(choice(too_little))
            minus = 0
        elif abs(int(d[0]) - int(d[1])) > diap:
            print(choice(too_mach))
            minus = 0
        else:
            return [d, minus]

def diapazon():
    print('Выберете диапазон:\n1 - до 2000\n2 - до 5000\n3 - до 10000\n4 - ввести самостоятельно')
    while True:
        d = input()
        if d.isdigit() == False:
            print('Введите цифру, пожалуйста:')
        elif d in ['1', '1 ']:
            return 2000
        elif d in ['2', '2 ']:
            return 5000
        elif d in ['3', '3 ']:
            return 10000
        elif d in ['4', '4 ']:
            print('Введите максимальный диапазон, введите одно число:')
            while True:
                d = input().split()
                if len(d) > 1:
                    print('Одну цифру, пожалуйста :)')
                elif d[0].isdigit() == False:
                    print('Введите цифру, пожалуйста:')
                elif int(d[0]) <= 20:
                    print('Давайте лучше побольше :)')
                else:
                    return int(d[0])
        elif len(d) > 1:
            print('Повторите, пожалуйста')


print('Это программа угадайка. Ты задашь диапазон чисел.\nСреди этих чисел я загадаю число, а ты будешь угадывать :).\nНапиши "готов", если хочешь начать')
if input().lower() in ['готов', 'ujnjd', 'готов ', 'ujnjd ']:
    game(proverka())
else:
    n ='нет'
    count = 0
    while n.lower() not in ['готов', 'ujnjd', 'готов ', 'ujnjd ']:
        count += 1
        print('Хорошо я подожду...')
        n = input('Напиши "готов"\n')
        if count == 3:
            print('Ты прям не хочешь?')
            if input('Напиши "да", если так\n') in ['да', 'lf','да ', 'lf ']:
                print('Хорошо, возвращайся :)')
                break
            else:
                print('Может тогда начнем? "готов"')
                if input().lower() in  ['готов', 'ujnjd', 'готов ', 'ujnjd ']:
                    game(proverka())
                    break
                else:
                    print('Хорошо, возвращайся :)')
                    break

    if count != 3:
        game(proverka())
