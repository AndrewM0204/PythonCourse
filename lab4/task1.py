# TODO решите задачу
import json


def task(input_path: str) -> float:
    with open(input_path) as f:
        data = json.load(f)
    sum_of_products = 0
    for d in data:
        sum_of_products += d["score"] * d["weight"]
    return round(sum_of_products, 3)





print(task("input.json"))
