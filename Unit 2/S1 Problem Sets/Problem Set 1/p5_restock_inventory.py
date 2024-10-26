def restock_inventory(current_inventory, restock_list):
    for key, value in restock_list.items():
        if key in current_inventory:
            current_inventory[key] += value
        else:
            current_inventory[key] = value
            
    return current_inventory

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

print(restock_inventory(current_inventory, restock_list))
