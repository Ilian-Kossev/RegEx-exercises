import re

text = input().lower() # text = input()
word = input().lower()  # word = input()
pattern = rf'\b{word}\b'
word_count = len(re.findall(pattern, text))
# word_count = len(re.findall(pattern, text, flags=re.IGNORECASE))
print(word_count)
