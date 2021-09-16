with open('file2.txt', 'r', encoding='utf-8') as file:
    useful = [f'{line}\t{count.strip()} - {len(count.split())} words'
              for line, count in enumerate(file, 1)]
    print(*useful, f'Total lines - {len(useful)}', sep='\n')
