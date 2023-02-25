#!/usr/bin/python3
"""Making change module
"""


def makeChange(coins, total):
    """Finds the minimum number of coins needed to make change
    """
    if (total <= 0):
        return 0
    coin_arr = [float('inf') for i in range(total + 1)]
    coin_arr[0] = 0
    for coin in coins:
        for x in range(len(coin_arr)):
            if coin <= x:
                coin_arr[x] = min(coin_arr[x], 1 + coin_arr[x - coin])
    return coin_arr[total] if coin_arr[total] != float('inf') else -1
