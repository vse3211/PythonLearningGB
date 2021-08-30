lst = ['1', 2, 3.5, [4, 5], (70, 32), True, {6: 7, 8: 9}]

for item in lst:
    print(f"Content: {item}; Type: {type(item)}")
    # Я изначально хотел использовать проверку на тип через type(item) == type([]) и == type({}), но программа мне
    # посоветовала использовать isinstance(), так что я его использую :)
    if isinstance(item, list) or isinstance(item, dict) or isinstance(item, set) or isinstance(item, tuple):
        for item2 in item:
            print(f"{' ' * 4}Content: {item2}; Type: {type(item2)}")
    # Хотел использовать рекурсию с функциями, но т.к. функций на этом уроке мы еще "не знаем" - в коде их нет
    # Могут конечно быть списки в списках и т.д., но без функций я не знаю как оптимально это реализовать
