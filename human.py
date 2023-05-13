from random import *
import os

def game():
    an_word = []
    in_letter = ''
    c = 0
    word_list = ['год', 'день', 'рыба', 'волк', 'птица', 'лиса', 'дом', 'мяч', 'крик', 'дерево', 'собака', 'кошка', 'охрана', 'неделя', 'глобус',
                 'клоун', 'тигр', 'способ', 'пион', 'цитрус', 'акробат', 'вермишель', 'ягода', 'палка', 'крючек', 'поцелуй', 'обида', 'любовь', 
                 'цирк', 'мрачный', 'юла', 'макароны', 'пюре', 'котлета', 'покупка', 'магазин', 'мурка', 'картина', 'цветок', 'фотография', 
                 'игрушка', 'плакат', 'скрепка', 'моль', 'мысль', 'роза', 'трава', 'экран', 'открытка', 'наклейка', 'рука', 'нога', 'голова', 
                 'лампа', 'хвост', 'волосы', 'нож', 'рот', 'зубы', 'глаза', 'карандаш', 'лист', 'духи', 'доска', 'подушка', 'скотч', 'мозг', 
                 'счастье', 'грусть', 'коробка', 'ваза', 'миска', 'кружка', 'ложка', 'вилка', 'хомяк', 'провод', 'веревка', 'зеркало', 'ключи',
                 'бутон', 'стебель', 'город', 'село', 'игра', 'ручка', 'стерка', 'мышка', 'бочка', 'вода', 'огонь', 'сон', 'яблоко', 'апельсин', 
                 'карта', 'страна', 'район', 'краска', 'лодка', 'корабль', 'газон', 'море', 'океан', 'обувь', 'одежда', 'кирпич', 'квартира', 
                 'комната', 'телевизор', 'тишина', 'работа', 'крем', 'мазь', 'укус', 'оса', 'пчела', 'шмель', 'воробей', 'бумага', 'крылья', 
                 'кубик', 'стих', 'кровать', 'тумба', 'краска', 'скрепка', 'арбуз', 'клубника', 'сливки', 'клавиатура', 'дорога', 'клумба']
    word = choice(word_list)
    del word_list[word_list.index(word)]
    print(' |-т---\n | О   \n |/|\  \n |/ \  \n |     \n')
    for i in range(len(word)):
        an_word.append('_ ')
    print(" ".join(an_word))
    print('\nСлово загадано.')
    while c < 11:
        print('Введите букву: ')
        letter = input().lower()
        if len(letter.split()[0]) > 1:
            if letter == word:
                print('Ты выиграл!')
                n = input('Хочешь попробовать еще раз? "да"/"нет" ')
                if n in ['lf', 'lf ', 'да', 'да ']:
                    print("\033[H\033[J")
                    return game()
                else:
                    print('Возвращайтесь!')
                    n = input()
                    return n
            else:
                print('Не то слово!')
                c += 1
                if c == 1:
                    print('       \n   О   \n       \n       \n       \n')
                    print(" ".join(an_word))
                    print(f'Првоеренные буквы {in_letter} ')
                elif c == 2:
                    print('       \n   О   \n   |   \n       \n       \n')
                    print(" ".join(an_word))
                    print(f'Првоеренные буквы {in_letter} ')
                elif c == 3:
                    print('       \n   О   \n   |\  \n       \n       \n')
                    print(" ".join(an_word))
                    print(f'Првоеренные буквы {in_letter} ')
                elif c == 4:
                    print('       \n   О   \n  /|\  \n       \n       \n')
                    print(" ".join(an_word))
                    print(f'Првоеренные буквы {in_letter} ')
                elif c == 5:
                    print('       \n   О   \n  /|\  \n  /    \n       \n')
                    print(" ".join(an_word))
                    print(f'Првоеренные буквы {in_letter} ')
                elif c == 6:
                    print('       \n   О   \n  /|\  \n  / \  \n       \n')
                    print(" ".join(an_word))
                    print(f'Првоеренные буквы {in_letter} ')
                elif c ==7:
                    print(' |     \n | О   \n |/|\  \n |/ \  \n |     \n')
                    print(" ".join(an_word))
                    print(f'Првоеренные буквы {in_letter} ')
                elif c == 8:
                    print(' |-----\n | О   \n |/|\  \n |/ \  \n |     \n')
                    print(" ".join(an_word))
                    print(f'Првоеренные буквы {in_letter} ')
                elif c == 9:
                    print(' |-----\n | О   \n |/|\  \n |/ \  \n | П   \n')
                    print(" ".join(an_word))
                    print(f'Првоеренные буквы {in_letter} ')
                elif c == 10:
                    print(' |-т---\n | О   \n |/|\  \n |/ \  \n | П   \n')
                    print(" ".join(an_word))
                    print(f'Првоеренные буквы {in_letter} ')
                elif c == 11:
                    print(' |-т---\n | О   \n |/|\  \n |/ \  \n |     \n')
                    print(" ".join(an_word))
                    print(f'Првоеренные буквы {in_letter} ')
                    n = input(f'Ты проиграл :(\nЭто было слово "{word}"\nХочешь попробовать еще раз? "да"/"нет" ')
                    if n in ['lf', 'lf ', 'да', 'да ']:
                        os.system('cls||clear')
                        return game()
                    else:
                        print('Возвращайтесь!')
                        n = input()
                        return n
        elif letter in word:
            in_letter += ' ' + letter
            for i in range(len(word)):
                if word[i] == letter:
                    an_word[i] = letter
            print(" ".join(an_word))
            print(f'Првоеренные буквы {in_letter} ')
            if "".join(an_word) == word:
                print('Ты выиграл!')
                n = input('Хочешь попробовать еще раз? "да"/"нет" ')
                if n in ['lf', 'lf ', 'да', 'да ']:
                    os.system('cls||clear')
                    return game()
                else:
                    print('Возвращайтесь!')
                    n = input()
                    return n
        else:
            print('Нет такой буквы!')
            in_letter += ' ' + letter
            c += 1
            if c == 1:
                print('       \n   О   \n       \n       \n       \n')
                print(" ".join(an_word))
                print(f'Првоеренные буквы {in_letter} ')
            elif c == 2:                    
                print('       \n   О   \n   |   \n       \n       \n')
                print(" ".join(an_word))
                print(f'Првоеренные буквы {in_letter} ')
            elif c == 3:
                print('       \n   О   \n   |\  \n       \n       \n')
                print(" ".join(an_word))
                print(f'Првоеренные буквы {in_letter} ')
            elif c == 4:
                print('       \n   О   \n  /|\  \n       \n       \n')
                print(" ".join(an_word))
                print(f'Првоеренные буквы {in_letter} ')
            elif c == 5:
                print('       \n   О   \n  /|\  \n  /    \n       \n')
                print(" ".join(an_word))
                print(f'Првоеренные буквы {in_letter} ')
            elif c == 6:
                print('       \n   О   \n  /|\  \n  / \  \n       \n')
                print(" ".join(an_word))
                print(f'Првоеренные буквы {in_letter} ')
            elif c ==7:
                print(' |     \n | О   \n |/|\  \n |/ \  \n |     \n')
                print(" ".join(an_word))
                print(f'Првоеренные буквы {in_letter} ')
            elif c == 8:
                print(' |-----\n | О   \n |/|\  \n |/ \  \n |     \n')
                print(" ".join(an_word))
                print(f'Првоеренные буквы {in_letter} ')
            elif c == 9:
                print(' |-----\n | О   \n |/|\  \n |/ \  \n | П   \n')
                print(" ".join(an_word))
                print(f'Првоеренные буквы {in_letter} ')
            elif c == 10:
                print(' |-т---\n | О   \n |/|\  \n |/ \  \n | П   \n')
                print(" ".join(an_word))
                print(f'Првоеренные буквы {in_letter} ')
            elif c == 11:
                print(' |-т---\n | О   \n |/|\  \n |/ \  \n |     \n')
                print(" ".join(an_word))
                print(f'Првоеренные буквы {in_letter} ')
                print(f'Првоеренные буквы {in_letter} ')
                n = input(f'Ты проиграл :(\nЭто было слово "{word}"\nХочешь попробовать еще раз? "да"/"нет" ')
                if n in ['lf', 'lf ', 'да', 'да ']:
                    os.system('cls||clear')
                    return game()
                else:
                    print('Возвращайтесь!')
                    n = input()
                    return n

print('Привет, это игра "Висельник". Я загадываю слово, а ты угадываешь, называя буквы.\nЗа кажду неверную букву я буду рисоваться тело человечка и виселицу. Когда будет нарисовано все ты проиграешь.\nЕсли ты угадаешь все буквы, до того как все будет нарисовано, ты выиграл!\n')
print('Можно также ввести слово, если ты уже догадываешься :). Но учти что буквы не будут засчитаны, если они есть, а если слово будет неправильным количество попыток уменьшится!!!\n')
input('Нажми enter, чтобы начать ')
game()

