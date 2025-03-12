from copy import deepcopy
from typing import Optional


example_levels = [
[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9]
]

levels = []

with open('data/day_2.txt', 'r') as f:
    for line in f:
        levels.append(line.split(' '))

for level in levels:
    for i, value in enumerate(level):
        level[i] = int(value.replace("\n",""))


def level_checker(level: list[int], second_try: Optional[bool] = False):

    increasing = True
    if level[0] - level[1] > 0:
        increasing = False


    for i, value in enumerate(level):
        if i == len(level) - 1:
            return True

        if increasing:
            value_list = [
                value + 1,
                value + 2,
                value + 3]
        else:
            value_list = [
                value - 1,
                value - 2,
                value - 3]


        if level[i+1] not in value_list:
            if second_try:
                return False

            remove_first_term = deepcopy(level)
            del remove_first_term[i - 1]
            try_first = level_checker(remove_first_term, True)

            remove_second_term = deepcopy(level)
            del remove_second_term[i]
            try_second = level_checker(remove_second_term, True)

            remove_third_term = deepcopy(level)
            del remove_third_term[i + 1]
            try_third = level_checker(remove_third_term, True)


            if try_first or try_second or try_third:
                return True
            else:
                return False



safe_count = 0
for level in levels:
    if level_checker(level):
        safe_count += 1


print(safe_count)
