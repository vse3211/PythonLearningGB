lst = []
while True:
    value = input('Enter number to add or "exit" to exit: ')
    if value.isdigit():
        lst.append(value)
    else:
        break
print(lst)
print(f'({len(lst)})\n')
i = 0

while i < len(lst):
    def replace():
        v1 = lst[i]
        v2 = lst[i + 1]
        lst[i] = v2
        lst[i + 1] = v1

    if len(lst) % 2 == 0 and i <= len(lst) - 2:
        replace()
    elif len(lst) % 2 != 0 and i <= len(lst) - 3:
        replace()
    else:
        break
    i += 1

print(f'\n{lst}\n({len(lst)})')
