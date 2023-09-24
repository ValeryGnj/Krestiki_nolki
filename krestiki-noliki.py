# сторона поля
board_side = 3
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_board():
    # формируем и выводим игровое поле
    print('_' * 4 * board_side)
    for i in range(board_side):
        print((' ' * 3 + '|') * 3)
        print('', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(('_' * 3 + '|') * 3)


def game_step(index, char):
    # совершаем ход
    if index > 9 or index < 1 or board[index - 1] in ('X', 'O'):
        return False
    board[index - 1] = char
    return True


def check_win():

    # проверяем на выигрыш одного из игроков
    win = False

    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтали
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикали
        (0, 4, 8), (2, 4, 6)  # диагонали
                       )
    for pos in win_combination:
        if board[pos[0]] == board[pos[1]] == board[pos[2]]:
            win = board[pos[0]]

    return win


def start_game():
    # текущий игрок
    current_player = 'X'
    # номер шага
    step = 1
    draw_board()
    while step < 9 and check_win() == False:
        index = input('ходит игрок ' + current_player + '.Введите номер поля если (0 - выход):')
        if index == '0':
            break

        # если получилось сделать ход
        if game_step(int(index), current_player):
            print('удачный ход')
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()
            # увеличиваем номер хода

        else:
            print('Неверный ход. Повторите!')
        step += 1

    if step == 9:
        print('Игра окончена, ничья!')
    elif check_win() != False:
        print('Выиграл игрок ' + check_win())



# начинаем игру
start_game()
print('Well come to "крестики-нолики!!!"')
