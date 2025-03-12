
import re


pattern = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
# pattern = re.compile("mul")

with open('data/day_3.txt', 'r') as f:
    file_content = f.read()

# example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

result = pattern.findall(file_content)

total = 0
for match in result:
    num1, num2 = match
    num1 = int(num1)
    num2 = int(num2)
    total += num1 * num2


print(total)