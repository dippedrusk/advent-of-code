import re

with open('input', 'r', encoding='utf-8') as f:
    text = f.read()

total = 0
for str1, str2 in re.findall(r'mul\((\d+),(\d+)\)', text):
    num1, num2 = int(str1), int(str2)
    total += num1 * num2

print(total)

with open('input', 'r', encoding='utf-8') as f:
    text = f.read()

total = 0
enabled = True
for match in re.findall(r"don't|do|mul\(\d+,\d+\)", text):
    if match == 'do':
        enabled = True
    elif match == "don't":
        enabled = False
    elif enabled:
        split = match[4:-1].split(',')
        num1, num2 = int(split[0]), int(split[1])
        total += num1 * num2


print(total)
