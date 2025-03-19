from copy import deepcopy


# example_updates = ['47|53',
# '97|13',
# '97|61',
# '97|47',
# '75|29',
# '61|13',
# '75|53',
# '29|13',
# '97|29',
# '53|29',
# '61|53',
# '97|53',
# '61|29',
# '47|13',
# '75|47',
# '97|75',
# '47|61',
# '75|61',
# '47|29',
# '75|13',
# '53|13',
# '',
# '75,47,61,53,29',
# '97,61,53,29,13',
# '75,29,13',
# '75,97,47,61,53',
# '61,13,29',
# '97,13,75,29,47'
# ]

with open('data/day_5.txt', 'r', encoding="utf-8") as f:
    file_content = f.readlines()

total = 0
updates = False
rules_dict: dict[int, list[int]] = dict()
for line in file_content:
    if len(line) <= 1:
        updates = True
        continue

    if not updates:
        before, after = line.split('|')
        before = int(before)
        after = int(after)
        if before in rules_dict:
            rules_dict[before].append(after)
        else:
            rules_dict[before] = [after]
    else:
        failed_line = False
        past_pages = []
        updated_pages = [int(x) for x in line.split(',')]
        # TODO: looks like the old indexes are being used for each new iteration, probably due to updating the item being iterated over.
        # TODO: I attempted to fix this with the deepcopy, but its still not the right answer, giving up for now
        copy_pages = deepcopy(updated_pages)
        for old_index, page in enumerate(updated_pages):
            if int(page) in rules_dict:
                for new_index, past_page in enumerate(past_pages):
                    if past_page in rules_dict[int(page)]:
                        failed_line = True
                        copy_index = copy_pages.index(page)
                        past_page_index = copy_pages.index(past_page)
                        copy_pages.insert(past_page_index, copy_pages.pop(copy_index))
                        print(copy_pages)

            past_pages.append(page)
        if failed_line:
            print(copy_pages)
            total += copy_pages[int((len(copy_pages)-1)/2)]

print(total)

# 5259 is too high
# 4729 is too high