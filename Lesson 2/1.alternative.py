# Check value type
def checkType(i):
    if isinstance(i, list) or isinstance(i, dict) or isinstance(i, set) or isinstance(i, tuple):
        return True
    else:
        return False


# Parse List & Dictionary
def ParseLD(i, count=4):
    for i2 in i:
        if checkType(i2):
            print(f"{' ' * (count - 4)}{'-' * 4}| Type: {type(i2)} >")
            ParseLD(i2, count + 4)
        else:
            print(f"{' ' * (count - 4)}{'-' * 4}| Content: {i2}; Type: {type(i2)}")


lst = ['1', 2, 3.5, [4, [5, {10, 11}, False]], (70, 32), True, {6: 7, 8: 9}]

for item in lst:
    if checkType(item):
        ParseLD(item)
    else:
        print(f"| Content: {item}; Type: {type(item)}")
