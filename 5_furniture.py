import re

# (\d+\.)*\d+\!\d+
pattern = r'^>>(?P<furniture>[A-Z a-z]+)<<(?P<price>\d+\.?\d*)!(?P<quantity>\d+)$'
bought_furniture = {}
command = input()
while not command == 'Purchase':
    matches = re.finditer(pattern, command)
    for match in matches:
        bought_furniture[match.groupdict()['furniture']] = float(match.groupdict()['price'])
        bought_furniture[match.groupdict()['furniture']] *= int(match.groupdict()['quantity'])

    command = input()

total_money_spent = 0
print('Bought furniture:')
for key, value in bought_furniture.items():
    print(key)
    total_money_spent += value
print(f'Total money spend: {total_money_spent:.2f}')

#judge - 75/100



