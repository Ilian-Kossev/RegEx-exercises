import re

pattern = r'\s(?P<emails>(?P<user>[A-Za-z0-9]+[A-Za-z0-9\.\-\_]+)\@(?P<domain>[A-Za-z]+[A-Za-z\-]*(\.[A-Za-z]+)+[A-Za-z\-]*))'
text = input()
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group('emails'))