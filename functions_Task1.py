from random import randint as rnd


def who_is_first():
    first_player_name = ''
    first_player = rnd(1, 2)
    if first_player == 1:
        first_player_name = 'HUMAN'
    else:
        first_player_name = 'PC'
    return first_player_name


def get_candies_by_human(candy_number_input, max_number_of_candies_by_step):
    candies_by_step = int(input('get your candies by this step:  '))
    if candies_by_step <= max_number_of_candies_by_step and candies_by_step <= candy_number_input:
        return candies_by_step
    else:
        print('you insert wrong number of candies, please, try again')
        return get_candies_by_human(candy_number_input, max_number_of_candies_by_step)


def get_candies_rnd(candy_number_input, max_number_of_candies_by_step):
    if candy_number_input >= max_number_of_candies_by_step:
        candies_by_step = rnd(1, max_number_of_candies_by_step)
    else:
        candies_by_step = rnd(1, candy_number_input)
    return candies_by_step


def winners_step(candy_number_input, max_number_of_candies_by_step):
    if candy_number_input >= max_number_of_candies_by_step + 1:
        if candy_number_input % (max_number_of_candies_by_step + 1) > 0:
            candies_by_step = candy_number_input % (max_number_of_candies_by_step + 1)
        else:
            candies_by_step = get_candies_rnd(candy_number_input, max_number_of_candies_by_step)
    else:
        candies_by_step = candy_number_input
    return candies_by_step
