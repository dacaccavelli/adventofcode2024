
# example_search = ['MMMSXXMASM',
# 'MSAMXMSMSA',
# 'AMXSXMAAMM',
# 'MSAMASMSMX',
# 'XMASAMXAMM',
# 'XXAMMXXAMA',
# 'SMSMSASXSS',
# 'SAXAMASAAA',
# 'MAMMMXMMMM',
# 'MXMXAXMASX',
# ]

with open('data/day_4.txt', 'r') as f:
    example_search = f.readlines()

total = 0

def check_direction(row_count: int, char_count: int, iteration: int, direction: list[int, int] = [0, 0]):
    term = 'XMAS'
    current_letter = example_search[row_count][char_count]

    if iteration == 3 and current_letter == term[3]:
        global total
        total += 1
        print(f'{row_count, char_count}: {current_letter}')
        return

    try:
        new_row_count = row_count+direction[0]
        new_char_count = char_count+direction[1]
        if new_row_count < 0 or new_row_count > len(example_search)-1 or new_char_count < 0 or new_char_count > len(example_search)-1:
            return
        if current_letter == term[iteration]:
            check_direction(new_row_count, new_char_count, iteration + 1, direction)
    except Exception as e:
        print(e)


combinations = [
    [-1,-1],
    [-1,0],
    [-1,1],
    [0,-1],
    [0,1],
    [1,-1],
    [1,0],
    [1,1]]

for row_count, row in enumerate(example_search):
    for char_count, char in enumerate(row):
        for direction in combinations:
            check_direction(row_count, char_count, 0, direction)

print(total)

# print(len(search_array))