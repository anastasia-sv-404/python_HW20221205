def print_playing_field(position: list):
    print()
    print(f'{position[0]}  {position[1]}  {position[2]}')
    print('_________')
    print(f'{position[3]}  {position[4]}  {position[5]}')
    print('_________')
    print(f'{position[6]}  {position[7]}  {position[8]}')
    print()


def human_position_input(position: list) -> int:
    while True:
        try:
            item = int(input(f'Введите номер ячейки: '))
            if 1 <= item <= 9 and position[item-1].isdigit:
                return item
            else:
                print('Введите номер другой ячейки: ячейка занята или введено неверное значение')
        except:
            print('Введено неверное значение')

def print_name(value):
    print(f'Первым ходит {value}')

def print_PC_step(step: int):
    print(f'PC выбрал для хода ячейку {step}')

def print_other(value):
    print(value)