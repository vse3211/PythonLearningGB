with open('file3.txt', 'r', encoding='utf-8') as file:
    emp_dict = {line.split()[0]: float(line.split()[1]) for line in file}
    print(f'Average salary = {round(sum(emp_dict.values()) / len(emp_dict), 3)}\n'
          f'Employees with salary less than 20k {[i[0] for i in emp_dict.items() if i[1] < 20000]}')
