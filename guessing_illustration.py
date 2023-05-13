from tkinter import *
from time import *
from random import *
global l_2, l_3, l_4, l_much, l_little, l_digit, namber
l_2, l_3, l_4, l_much, l_little, l_digit, namber, y, x = 0, 0, 0, 0, 0, 0, 0, 0, 0
too_little_diap = ['Так не интересно :) Давай больше', 'Больше!', 'Маловато будет, быстро закончим', 'Можно и побольше взять']
too_much =['Слишком много!', 'Много!', 'Эх, слишком много', 'Давай еще раз, слишком много', 'Может еще раз? Много']
too_little = ['Слишком мало!', 'Мало!','Не, мало, давай еще', 'Маловато', 'Мало. Надо еще']
enough = ['Ура, ты угадал.', 'Ура, это оно.', 'Получилось! Ты угадал.', 'Превосходно, это оно!', 'Супер! Ты угадал.']

def nott():
    global label_not, label_enough, label_restart, digit, btn_restart, btn_not
    label_enough.destroy()
    label_restart.destroy()
    btn_not.destroy()
    btn_restart.destroy()
    label_not.grid()

def restart():
    global btn_not, btn_restart, label_digit, label_enough, diap, btn_2, name, digit, label_7, btn_not, btn_restart, label_restart\
        , label_5, btn_1
    label_5.destroy()
    label_5 = Label(win, text='Принято!', font=('Times new roman', 12), bg = 'green', foreground='white')
    label_restart.destroy()
    btn_restart.destroy()
    btn_not.destroy()
    label_restart = Label(win, text='Хочешь сыграть еще раз? :)', font=('Times new roman', 12), bg = '#F08080', foreground='white', bd=2)
    btn_restart = Button(win, text='Да', command=restart)
    btn_not = Button(win, text='Нет', command= nott)
    label_7.destroy()
    label_7 = Label(win, text='Введите число', font=('Times new roman', 12), bg = '#F08080', foreground='white')
    digit.destroy()
    digit = Entry(win)
    label_enough.destroy()
    label_enough = Label(win, text=choice(enough)+f' Это загаданное число', font=('Times new roman', 12), bg = 'green', foreground='white')
    diap = Label(win, text = 'Выберете диапазон:', font=('Times new roman', 12), bg = '#F08080', foreground='white')
    diap.grid(row = 2, column=0, sticky='w')
    btn_2.destroy()
    btn_2 = Button(win, text='Клик', command=game, bg='#F3F69D')
    name = Entry(win)
    name.grid(row=3, column=0)
    btn_1 = Button(win, text='Клик', command=rand, bg='#F3F69D')
    btn_1.grid(row=4, column=0)

def game():
    global number, l_little, l_much, l_digit, label_digit, label_enough, label_little, label_much, btn_restart, btn_not
    if l_little == 1:
        label_little.destroy()
        label_little = Label(win, text=choice(too_little), font=('Times new roman', 12), bg = 'red', foreground='white')
        l_little = 0
    elif l_much == 1:
        label_much.destroy()
        label_much = Label(win, text=choice(too_much), font=('Times new roman', 12), bg = 'red', foreground='white')
        l_much = 0
    elif l_digit == 1:
        label_digit.destroy()
        label_digit = Label(win, text='Одну цифру, пожалуйста :)', font=('Times new roman', 12), bg = 'red', foreground='white')
        l_digit = 0
    if digit.get().isdigit() == False:
        label_digit.grid()
        l_digit = 1
    elif int(digit.get()) < number:
        l_little = 1
        label_little.grid()
    elif int(digit.get()) > number:
        l_much = 1
        label_much.grid()
    elif int(digit.get()) == number:
        label_enough.grid()
        btn_2.config(state='disabled')
        label_restart.grid()
        btn_restart.grid()
        btn_not.grid()

def btn_game(value):
    global btn_1
    diap.destroy()
    name.destroy()
    btn_1.destroy()
    global number, label_6, label_7
    minus = value[1]
    value = value[0]
    x = int(value[0])
    y = int(value[1])
    if minus == 1:
        x *= -1
        y *= -1
    if x > y:
        label_6 = Label(win, text=f'Загадано число от {y} до {x}', font=('Times new roman', 12), bg = '#F08080', foreground='white')
        number = randint(y, x)
        label_6.grid(row=6)
    else:
        label_6 = Label(win, text=f'Загадано число от {x} до {y}', font=('Times new roman', 12), bg = '#F08080', foreground='white')
        number = randint(x, y)
        label_6.grid(row=6)
    label_7.grid(row=7)
    digit.grid(row=8)
    btn_2.grid(row=9)

def rand():
    global l_2, l_3, l_4, label_2, label_3, label_4
    value = name.get()
    minus = 0
    if '-' in value:
            value = value.replace('-', '')
            minus = 1
    value = value.split()
    if l_3 == 1:
            label_3.destroy()
            label_3 = Label(win, text='Введите цифры, пожалуйста', font=('Times new roman', 12), bg = 'red', foreground='white')
            l_3 = 0
    elif l_2 == 1:
            label_2.destroy()
            label_2 = Label(win, text='Введите еще раз, нужно две цифры', font=('Times new roman', 12), bg = 'red', foreground='white')
            l_2 = 0
    elif l_4 == 1:
        label_4.destroy()
        label_4 = Label(win, text=choice(too_little_diap), font=('Times new roman', 12), bg = 'red', foreground='white')
        l_4 = 0
    if len(value) > 2 or len(value) == 1:
        label_2.grid(row = 5, column=0)
        l_2 = 1
    elif value[0].isdigit() == False or value[1].isdigit() == False:
        label_3.grid(row = 5, column=0)
        l_3 = 1
    elif abs(int(value[0]) - int(value[1])) < 50:
        label_4.grid(row = 5, column=0)
        l_4 = 1
    else:
        label_5.grid()
        btn_game([value, minus])
    

win = Tk() # создание главного окна
#photo = PhotoImage(file='logo.png')
win.config(background='#F08080') # изменение цвета окна
#win.iconphoto(False, photo) # импортирование фото
win.title('Игра угадайка') # меняет название
win.geometry("500x300+400+100") # меняет размер окна, +400 +100 обозначает насколько мы сдвинем окно относительно левого верхнего края. Первая горизонтально, второе вертикально
win.resizable(False, False) # запрещает растягивать по ширине и высоте


digit = Entry(win)
label_1 = Label(win, text = 'Это программа угадайка.\nТы задашь диапазон чисел.\nСреди этих чисел я загадаю число, а ты будешь угадывать :).',
                bg = '#F08080', foreground='white',
                font=('Times new roman', 12, 'bold'), pady=10, relief=RAISED, bd=2, justify=CENTER)
label_2 = Label(win, text='Введите еще раз, нужно две цифры', font=('Times new roman', 12), bg = 'red', foreground='white')
label_3 = Label(win, text='Введите цифры, пожалуйста', font=('Times new roman', 12), bg = 'red', foreground='white')
label_4 = Label(win, text=choice(too_little_diap), font=('Times new roman', 12), bg = 'red', foreground='white')
label_5 = Label(win, text='Принято!', font=('Times new roman', 12), bg = 'green', foreground='white')
label_much = Label(win, text=choice(too_much), font=('Times new roman', 12), bg = 'red', foreground='white')
label_little = Label(win, text=choice(too_little), font=('Times new roman', 12), bg = 'red', foreground='white')
label_enough = Label(win, text=choice(enough)+f' Это загаданное число', font=('Times new roman', 12), bg = 'green', foreground='white')
label_digit = Label(win, text='Только цифры пожалуйста :)', font=('Times new roman', 12), bg = 'red', foreground='white')
label_7 = Label(win, text='Введите число', font=('Times new roman', 12), bg = '#F08080', foreground='white')
label_not = Label(win, text='Хорошо, возвращайся :)', font=('Times new roman', 16), bg = '#F08080', foreground='white')
label_restart = Label(win, text='Хочешь сыграть еще раз? :)', font=('Times new roman', 12), bg = '#F08080', foreground='white', bd=2)
btn_restart = Button(win, text='Да', command=restart)
btn_not = Button(win, text='Нет', command= nott)
#btn_1 = Button(win, text='Готов', font=('Times new roman', 12, 'bold'), relief=RAISED, bd=2, activebackground='red')
diap = Label(win, text = 'Выберете диапазон:', font=('Times new roman', 12), bg = '#F08080', foreground='white')
diap.grid(row = 2, column=0, sticky='w')
name = Entry(win)
name.grid(row=3, column=0)
btn_1 = Button(win, text='Клик', command=rand, bg='#F3F69D')
btn_1.grid(row=4, column=0)
label_1.grid(row=0, column=0)#columnspan=5, sticky='nswe', rowspan=5)
btn_2 = Button(win, text='Клик', command=game, bg='#F3F69D')

win.grid_columnconfigure(0, minsize=500)

win.mainloop() # вызывает окно
