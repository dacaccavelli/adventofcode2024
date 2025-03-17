
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

with open('data/day_4.txt', 'r', encoding="utf-8") as f:
    example_search = f.readlines()

total = 0

for row_count, row in enumerate(example_search):
    for char_count, char in enumerate(row):
        if example_search[row_count][char_count] == 'A':
            try:
                if row_count == 0 or char_count == 0:
                    continue
                first_pair = {example_search[row_count-1][char_count-1], example_search[row_count+1][char_count+1]}
                second_pair = {example_search[row_count-1][char_count+1], example_search[row_count+1][char_count-1]}
                if 'S' in first_pair and 'S' in second_pair and 'M' in first_pair and 'M' in second_pair:
                    total += 1
            except Exception as e:
                print(e)

print(total)
