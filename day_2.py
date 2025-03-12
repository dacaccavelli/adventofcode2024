from copy import deepcopy


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
        # if len(levels) < 10:
        #     levels.append(line.split(' '))
        levels.append(line.split(' '))

for level in levels:
    for i, value in enumerate(level):
        level[i] = int(value.replace("\n",""))


def level_checker(level: list[int]):

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


        print(level[i+1], value_list)
        if level[i+1] not in value_list:
            return False



safe_count = 0
for level in levels:
    if level_checker(level):
        safe_count += 1


print(safe_count)
