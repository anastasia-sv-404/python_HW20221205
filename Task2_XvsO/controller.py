import model
import view
import pc_intellect
from random import randint as rnd


def who_is_first():
    first_player_name = ''
    first_player = rnd(1, 2)
    if first_player == 1:
        first_player_name = 'HUMAN'
    else:
        first_player_name = 'PC'
    return first_player_name


def human_step():
    position_to_use = model.get_position()
    field = view.human_position_input(position_to_use)
    position_to_use[field - 1] = model.get_mark()
    model.set_position(position_to_use)
    if model.win_check() == 'Победа!':
        view.print_other(model.win_check())
        exit()
    if model.draw_check() == 'Ничья!':
        view.print_other(model.draw_check())
        exit()
    model.switch_mark()


def pc_step():
    position_to_use = model.get_position()
    field = pc_intellect.pc_intellect(position_to_use)
    view.print_PC_step(field)
    position_to_use[field - 1] = model.get_mark()
    model.set_position(position_to_use)
    if model.win_check() == 'Победа!':
        view.print_other(model.win_check())
        exit()
    if model.draw_check() == 'Ничья!':
        view.print_other(model.draw_check())
        exit()
    model.switch_mark()


def game():
    if model.get_first_player() == 'HUMAN':
        view.print_playing_field(model.get_position())
        human_step()
        pc_step()
    else:
        pc_step()
        view.print_playing_field(model.get_position())
        human_step()


def start():
    first_player_name = who_is_first()
    model.set_first_player(first_player_name)
    view.print_name(first_player_name)
    while True:
        game()
