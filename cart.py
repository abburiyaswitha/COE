def calculate_total(cart):
    filtered_cart={}
    for item,price in cart.items():
        if price > 20000:
            filtered_cart[item] = price
    total=sum(filtered_cart.values())
    if total > 50000:
        total *= 0.85
    elif total >= 20000 and total <= 50000:
        total *= 0.90
    return total
cart={
    'laptop':50000,
    'headphones':2000,
    'mouse':35000,
    'keyboard':1500,
    'monitor':8000,
    'Usb drive':1000
}
print(f"Cart items:{cart}")
print(f"Total price after discount:{calculate_total(cart)}")