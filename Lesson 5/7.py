import json

with open('file7.json', 'w', encoding='utf-8') as js_file:
    with open('file7.txt', encoding='utf-8') as file:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in file}
        result = [profit, {'average_profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                   len([int(i) for i in profit.values() if int(i) > 0]))}]
        json.dump(result, js_file, ensure_ascii=False, indent=4)
