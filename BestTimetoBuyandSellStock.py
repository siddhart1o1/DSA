prices = [7, 6, 4, 3, 1]


def solve(prices):
    small = prices[0]
    max = prices[0]
    maxindex = 0
    smallindex = 0
    profit = 0
    for i in range(len(prices)):
        if(prices[i] < small):
            small = prices[i]
            smallindex = i
            if(smallindex >= maxindex):
                max = prices[i]
                smallindex = i
        if(prices[i] > max):
            max = prices[i]
        if(max - small > profit):
            profit = max - small

    return profit


# better soln
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price

    return max_profit


solve(prices)
