def profit(data):
    cost_price = data["cost_price"]
    sell_price = data["sell_price"]
    inventory = data["inventory"]
    
    total_cost = cost_price * inventory
    total_sales = sell_price * inventory
    
    total_profit = total_sales - total_cost
    
    return round(total_profit)


data = {
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
}
print(profit(data))  # Output: 14796