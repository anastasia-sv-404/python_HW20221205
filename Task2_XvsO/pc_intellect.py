import model
import random


def pc_intellect(position_to_use: list) -> int:
    win_set = model.get_win_index_set()
    mark = model.get_mark()
    other_side_mark = model.other_side_mark()
    if position_to_use[4].isdigit():
        return 5
    else:
        corners = [0, 2, 6, 8]
        random.shuffle(corners)
        for i in win_set:
            if position_to_use[i[0]] == position_to_use[i[1]] == mark and position_to_use[i[2]].isdigit():
                return i[2] + 1
            if position_to_use[i[1]] == position_to_use[i[2]] == mark and position_to_use[i[0]].isdigit():
                return i[0] + 1
            if position_to_use[i[0]] == position_to_use[i[2]] == mark and position_to_use[i[1]].isdigit():
                return i[1] + 1
        for i in win_set:
            if position_to_use[i[0]] == position_to_use[i[1]] == other_side_mark and position_to_use[i[2]].isdigit():
                return i[2] + 1
            if position_to_use[i[1]] == position_to_use[i[2]] == other_side_mark and position_to_use[i[0]].isdigit():
                return i[0] + 1
            if position_to_use[i[0]] == position_to_use[i[2]] == other_side_mark and position_to_use[i[1]].isdigit():
                return i[1] + 1
        for corner in corners:
            if position_to_use[corner].isdigit():
                return corner + 1
        while True:
            position = random.randint(0, 8)
            if position_to_use[position].isdigit():
                return position + 1

