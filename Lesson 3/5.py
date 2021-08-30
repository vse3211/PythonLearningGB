def get_nums(s):
    lst = str(s).split(' ')
    res = []
    for i in lst:
        if str(i) == 'q':
            return res
        elif i != '' and i != None:
            res.append(int(i))
    return res


def get_summ(lst):
    res = 0
    for i in lst:
        res += i
    return res


print(f'Result: {get_summ(get_nums(input("Введите числа через пробел и q для завершения: ")))}')
