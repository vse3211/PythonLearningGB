km = int(input('Введите начальную дистанцию пробежки: '))
percent = int(input('Введите процент увеличения дистанции за день 0-100: '))
result = km
day = 1
print(f'{day}-й день: {km}')

while result < 3:
    # Во время разработки сталкивался с бесконечным циклом, так что эта логика сделает вывод из цикла при возникновении
    # таких ситуаций, но вы при этом сможете наблюдать резальтат
    if km == 0 or percent == 0 or day > 150:
        print('Ошибка, выход из приложения...')
        break

    day += 1
    result += result * float(str(f'0.{percent}'))
    print(f'{day}-й день: {result}')