with open('file.txt', 'w', encoding='utf-8') as file:
    while True:
        line = input('Input new string or empty to exit: ')
        if not line:
            break
        print(line, file=file)
