my_list = [7, 5, 3, 3, 2]

while True:
    num = int(input('Enter number: '))
    if num == -1:
        break
    else:
        for i in range(len(my_list) + 1):
            if (i >= len(my_list) and num <= my_list[len(my_list) - 1]) or (num > my_list[i]) or (my_list[i] >= num and (i + 1 < len(my_list) and my_list[i + 1] < num)):
                my_list.insert(i, num)
                print(my_list)
                break
