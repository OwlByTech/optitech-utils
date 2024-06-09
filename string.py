import json

# Carga el archivo JSON
with open('standards.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Recorre cada objeto en la lista y convierte 'paragraph' a string
for item in data:
    if 'paragraph' in item:
        item['paragraph'] = str(item['paragraph'])

# Guarda el JSON modificado en un nuevo archivo o sobrescribe el existente
with open('standards.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Todos los valores de 'paragraph' han sido convertidos a string.")
