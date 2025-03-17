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
        print(len(line))
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
        for page in updated_pages:
            if not failed_line:
                if int(page) in rules_dict:
                    for past_page in past_pages:
                        if past_page in rules_dict[int(page)]:
                            failed_line = True


                past_pages.append(page)
        if not failed_line:
            total += updated_pages[int((len(updated_pages)-1)/2)]

print(total)
