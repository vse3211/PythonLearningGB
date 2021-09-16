def sort_numbers(lst, num):
    my_list = lst
    new_number = int(num)
    i = 0
    for n in my_list:
        if new_number <= n:
            i += 1
        else:
            break
    my_list.insert(i, new_number)
    return my_list


def my_func(a, b, c):
    nums = [b, c]
    res = [a]
    for n in nums:
        res = sort_numbers(res, n)
    print(f'{res[0]}, {res[1]}')


my_func(int(input('Введите число A:')), int(input('Введите число B:')), int(input('Введите число C:')))
