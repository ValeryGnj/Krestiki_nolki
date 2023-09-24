from tkinter import *
import random, time

def win(n):
    global game
    # проверяем на выигрыш одного из игроков

    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтали
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикали
        (0, 4, 8), (2, 4, 6)  # диагонали
    )
    for pos in win_combination:
        if game[pos[0]] == n and game[pos[1]] == n and game[pos[2]] == n:
            return win

def game_stop():
    global game_left
    for item in game_left:
        buttons[item].config(bg='blue', state='disabled')

def push(b):
    pass
    global game, game_left, turn

    game[b] = 'X'
    buttons[b].config(text='X', bg='blue', state='disabled')
    game_left.remove(b)
    if b == 4 and turn == 0:
        t = random.choice(game_left)
    elif b != 4 and turn == 0:
        t = 4
    if turn > 0:
        t = 8 - b
    if t not in game_left:
        try:
            t = random.choice(game_left)
        except IndexError:
            label['text'] = 'Игра окончена!'
            game_stop()
    game[t] = '0'
    time.sleep(0.3)
    buttons[t].config(text='0', bg='blue', state='disabled')
    if win('X'):
        label['text'] = 'Вы победили!!!'
        game_stop()
    elif win('0'):
        label['text'] = 'Вы проиграли!!!'
        game_stop()
    else:
        if len(game_left) > 1:
            game_left.remove(t)
        else:
            label['text'] = 'Игра окончена!'
            game_stop()
        turn += 1


game = [None] * 9
game_left = list(range(9))
turn = 0

# отрисовка окна
root = Tk()
# надпись
label = Label(width=20, text='Игра крестики-нолики!!!', font=('arial', 20, 'bold'))

# кнопки
buttons = [Button(width=5, height=2, font=('Arial', 28, 'bold'), bg='green', command=lambda x=i: push(x))
           for i in range(9)]
# надпись, аголовок размещается в первой строке (row=0) и занимает все три столбца (columnspan=3)
label.grid(row=0, column=0, columnspan=3)
# кнопки размещаются с помощью генератора, но с учетом смещения строк. Значение row для кнопок вычисляется как (i // 3)
# + 1, что означает, что кнопки будут размещены в строках с индексами от 1 до 3. Условие if также учитывает ограничение
# на значения row и column, чтобы кнопки размещались только в пределах сетки размером 3x3.
# row, col = 1, 0
[buttons[i].grid(row=(i // 3) + 1, column=i % 3) for i in range(9) if i // 3 < 3 and i % 3 < 3]

root.mainloop()
