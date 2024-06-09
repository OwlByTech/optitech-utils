import json

with open('standards.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for item in data:
    if 'paragraph' in item:
        item['paragraph'] = str(item['paragraph'])

with open('standards.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("parsed")
