# coding: utf-8

print('*** Programme pour creer un fichier texte ***')
print('version 1.0.0', end='\n')

file_name = input('Entrez du fichier à creer: ')
content = input('Entrez le contenu du fichier: ')

if not file_name.endswith('.txt'):
    file_name = file_name + '.txt'

with open(file_name, 'w') as file:
    file.write(content)
    print(f"Le fichier {file_name} a ete cree avec success")

