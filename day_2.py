from copy import deepcopy


levels = []

with open('data/day_2.txt', 'r') as f:
    for line in f:
        # if len(levels) < 10:
        #     levels.append(line.split(' '))
        levels.append(line.split(' '))

for level in levels:
    for i, value in enumerate(level):
        level[i] = int(value.replace("\n",""))


def test_level(level: list[int], retry:bool = False):
    increase = False
    decrease = False

    def remove_fail(level: list, retry, index):
        if not retry:
            if index == len(level) -1:
                return True
            copy = deepcopy(level)
            copy.pop(index)
            if test_level(copy, True):
                return True
            else:
                copy = deepcopy(level)
                copy.pop(index-1)
                return test_level(copy, True)
        return False


    for i, value in enumerate(level[:-1]):
        next_value = level[i+1]

        if value == next_value:
            if remove_fail(level, retry, i+1):
                return True
            return False
        elif abs(value - next_value) > 3:
            if remove_fail(level, retry, i+1):
                return True
            return False
        elif value < next_value:
            if decrease:
                if remove_fail(level, retry, i+1):
                    return True
                return False
            increase = True
        else:
            if increase:
                if remove_fail(level, retry, i+1):
                    return True
                return False
            decrease = True
    return True


# print(test_level([75, 76, 80, 83, 85, 87, 92]))

safe_count = 0
for level in levels:
    response = test_level(level)
    print(level)
    print(response)
    print('-------------------')

    if response:
        safe_count += 1
    else:
        pass
print(safe_count)
