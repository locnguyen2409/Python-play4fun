def adjust_prices(items, percent):
    adjusted = []
    for entry in items:
        new_price = entry['price'] * (1 + percent / 100)
        adjusted.append({'item': entry['item'], 'price': round(new_price, 2)})
    return adjusted

item_prices = [
    {'item': 'Apple', 'price': 0.5},
    {'item': 'Banana', 'price': 0.3},
    {'item': 'Orange', 'price': 0.7}
]
adjusted = adjust_prices(item_prices, -10)  # decrease 10%
print(adjusted)