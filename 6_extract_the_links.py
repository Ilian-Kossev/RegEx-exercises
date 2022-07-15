import re

pattern = r'(www\.[A-Z a-z 0-9]+(\-[A-Z a-z0-9]+)*(\.[a-z]+)+)'
text = input()
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())