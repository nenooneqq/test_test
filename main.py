#Итоговое задание
'''Реализовать функции: total_revenue(purchases), items_by_category(purchases),
expensive_purchases(purchases, min_price), average_price_by_category(purchases),
most_frequent_category(purchases)'''

purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(purchases: list)->int:
    result = 0
    for elem in purchases:
        result += elem["price"] * elem["quantity"]
    return result



def items_by_category(purchases: list)->dict:
    result = dict()
    for elem in purchases:
        if result.get(elem['category']):
            result[elem['category']].add(elem['item'])
        else:
            result[elem['category']] = set()
            result[elem['category']].add(elem['item'])
    return result



def expensive_purchases(purchases: list, min_price: float):
    return [elem for elem in purchases if elem['price'] >= min_price]



def average_price_by_category(purchases):
    result = dict()
    for elem in purchases:
        if result.get(elem['category']):
            result[elem['category']].add(elem['price'])
        else:
            result[elem['category']] = set()
            result[elem['category']].add(elem['price'])
    return {i : (sum(value)/len(value)) for i, value in result.items()}



def most_frequent_category(purchases):
    result = dict()
    for elem in purchases:
        if result.get(elem['category']):
            result[elem['category']] += elem['quantity']
        else:
            result[elem['category']] = elem['quantity']
    return max(result, key = result.get)

print(f'Общая выручка: {total_revenue(purchases)}')
print(f'Товары по категориям: {items_by_category(purchases)}')
print(f'Покупки дороже 1.0: {expensive_purchases(purchases, 1)}')
print(f'Средняя цена по категориям: {average_price_by_category(purchases)}')
print(f'Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}')












