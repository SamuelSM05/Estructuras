inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25,
}

lista=[]
for product, quantity in inventory.items():
    lista.append(product.capitalize())
    print(f"{product.capitalize()}: {quantity} unidades")
    
print(lista)
    
