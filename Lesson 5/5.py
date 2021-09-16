from random import randint

with open('file5.txt', 'w', encoding='utf-8') as file:
    my_list = [randint(1, 100) for _ in range(100)]
    file.write(' '.join(map(str, my_list)))

print(f'Sum of elements: {sum(my_list)}')
