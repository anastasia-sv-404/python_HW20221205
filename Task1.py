# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""

#В описанном решении человек выиграет, только если:
# 1. будет ходить первым
# 2. с самого первого и на каждом ходе будет забирать конфеты в количестве Х % 29
# В противном случае выиграет ПК.


import functions_Task1

candy_number_input = 150
max_number_of_candies_by_step = 28

who_will_be_first = functions_Task1.who_is_first()
print(f'the first player is {who_will_be_first}')

while candy_number_input > 0:
    if who_will_be_first == 'HUMAN':
        candy_by_step_human = functions_Task1.get_candies_by_human(candy_number_input, max_number_of_candies_by_step)
        candy_number_input = candy_number_input - candy_by_step_human
        print(f'there are {candy_number_input} candies left')

        if candy_number_input == 0:
            print('HUMAN WINS!')
            break

        candy_by_step_PC = functions_Task1.winners_step(candy_number_input, max_number_of_candies_by_step)
        print(f'second player gets {candy_by_step_PC} candies')
        candy_number_input = candy_number_input - candy_by_step_PC
        print(f'there are {candy_number_input} candies left')

        if candy_number_input == 0:
            print('PC WINS!')
            break

    else:
        candy_by_step_PC = functions_Task1.winners_step(candy_number_input, max_number_of_candies_by_step)
        print(f'PC gets {candy_by_step_PC} candies')
        candy_number_input = candy_number_input - candy_by_step_PC
        print(f'there are {candy_number_input} candies left')

        if candy_number_input == 0:
            print('PC WINS!')
            break

        candy_by_step_human = functions_Task1.get_candies_by_human(candy_number_input, max_number_of_candies_by_step)
        candy_number_input = candy_number_input - candy_by_step_human
        print(f'there are {candy_number_input} candies left')

        if candy_number_input == 0:
            print('HUMAN WINS!')
            break