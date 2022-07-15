import re

pattern = r'\d+'
input_line = input()
all_nums = []
while input_line:
    found_nums = re.findall(pattern, input_line)
    all_nums += found_nums
    input_line = input()
print(*all_nums, end=' ')

