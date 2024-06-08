import json

with open('json/combined_data.json', 'r', encoding='utf-8') as file:
    lines = file.readlines()

modified_lines = [line.rstrip() + ',' for line in lines]

with open('file.json', 'w', encoding='utf-8') as file:
    file.write('\n'.join(modified_lines))

print("ok")
