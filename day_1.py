list_1 = []
list_2 = []

with open('data/day_1.txt', 'r') as f:
    for line in f:
        first, second = line.split('   ')
        list_1.append(int(first))
        list_2.append(int(second))

list_1.sort()
list_2.sort()
total = 0
for i, value in enumerate(list_1):
    count = list_2.count(value)
    # print(f'{value} appears {count} times')
    total += count * value

print(total)
