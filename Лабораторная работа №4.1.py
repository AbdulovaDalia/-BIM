import json

def task() -> float:

    with open('input.json', 'r') as file:
        data = json.load(file)

    total_product_sum = 0.0

    for item in data:

        product = item['score'] * item['weight']
        total_product_sum += product

    return round(total_product_sum, 3)

print(task())