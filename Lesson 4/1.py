from sys import argv


def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f'Salary - {time * rate + bonus}')
    except ValueError:
        print('Введите все 3 числа без пустой строки и символа')


salary()
