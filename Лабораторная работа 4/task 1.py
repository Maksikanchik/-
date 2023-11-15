import json
def task() -> float:
    filename = 'input.json'
    with open(filename) as file:
        data = json.load(file)
    summa = 0
    for i in data:
        k = i['score']
        l = i['weight']
        summa += k * l
    return round(summa, 3)



print(task())