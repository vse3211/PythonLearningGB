print('Instruction:')
print('Input seconds 1-inf for convert to time')
print('Input 0 to exit')
seconds = 1
while seconds > 0:
    seconds = int(input('Enter seconds: '))

    h = 0
    m = 0
    s = seconds % 60

    result = seconds // 60
    while result >= 60:
        h += 1
        result -= 60
    else:
        m = result

    print(f'{h:02}:{m:02}:{s:02}')
