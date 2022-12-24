position = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
win_index_set = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8),
                 (2, 4, 6))  # кортеж кортежей, нет возможности внести изменения
first_player = ''
mark = 'X'


def set_first_player(first_player_name: str):
    global first_player
    first_player = first_player_name


def get_first_player():
    global first_player
    return first_player


def get_position():
    global position
    return position


def set_position(position_new: list):
    global position
    position = position_new


def set_mark(player_mark):
    global mark
    mark = player_mark


def get_mark():
    global mark
    return mark


def win_check():  # проверка на выигрыш
    global win_index_set
    global position
    win = 'Победа!'
    for point in win_index_set:
        if position[point[0]] == position[point[1]] == position[point[2]]:
            return win


def draw_check():  # проверка на ничью (победной комбинации нет, все ячейки заполнены отметками Х или О)
    global position
    draw = 'Ничья!'
    for i in position:
        if i.isdigit():
            return False
    else:
        return draw


def switch_mark():
    global mark
    if mark == 'X':
        mark = 'O'
    else:
        mark = 'X'


def get_win_index_set():
    global win_index_set
    return win_index_set


def other_side_mark():
    global mark
    if mark == 'O':
        other_side_mark = 'X'
        return other_side_mark
    else:
        other_side_mark = 'O'
        return other_side_mark
