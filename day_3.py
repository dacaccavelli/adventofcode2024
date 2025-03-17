import re


do_dont_pattern = re.compile(r"do\(\).*?don't\(\)") # Non-Greedy Matching: The *? ensures that the pattern matches the smallest possible portion of the string between do() and don't().
mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
# pattern = re.compile("mul")

file_content_str: str = ''
with open('data/day_3.txt', 'r') as f:

    file_content = f.readlines()
    file_content_str = '\t'.join([line.strip() for line in file_content])
    first = file_content_str.find('do()')
    last = file_content_str.rfind("don't()") + 7
    file_content_str = file_content_str[first:last]

do_dont_result = do_dont_pattern.findall(file_content_str)


total = 0
for substring in do_dont_result:
    result = mul_pattern.findall(substring)

    for match in result:
        num1, num2 = match
        num1 = int(num1)
        num2 = int(num2)
        total += num1 * num2


print(total)
