def my_func(x, y):
    return x ** y


def my_func2(x, y):
    __x = x
    for i in range(y - 1):
        x = x * __x
    return x


_x = int(input('Enter x: '))
_y = int(input('Enter y: '))

print(f'** : {my_func(_x, _y)}')
print(f'for: {my_func2(_x, _y)}')
