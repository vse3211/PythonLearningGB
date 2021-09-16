rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три'}

with open('file4n.txt', 'w', encoding='utf-8') as new_file:
    with open('file4.txt', encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], rus.get(line.split()[0])) for line in my_file])
