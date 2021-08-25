st = 1
print('Input 0 to exit')
while st > 0:
    st = int(input('Enter looong number: '))
    i = st
    bigger = 0
    while i > 0:
        if i % 10 > bigger:
            bigger = i % 10
        i = i // 10
    print(bigger)
