"""
Understand:
- Write function, max_profit(), with parameter prices (list of integers).
- Return the maximum profit (choose a single day to buy stock and a later day to sell)
Plan:
- Intialize max_profit to 0.
- Nested iterate through indeces of prices via for loops.
    - Initalize profit difference between buy_day and sell_day (sell increments first)
        - If current_profit > max_profit, 
            - Initialize max_profit as current_profit.
- Return max_profit.
Implement:
"""
def max_profit(prices):
    max_profit = 0

    for buy in range(0, len(prices)-1):
        for sell in range(buy+1, len(prices)):
            current_profit = prices[sell] - prices[buy]
            if current_profit > max_profit:
                max_profit = current_profit

    return max_profit


prices = [7,1,5,3,6,4]
print(max_profit(prices))

prices = [7,6,4,3,1]
print(max_profit(prices))
