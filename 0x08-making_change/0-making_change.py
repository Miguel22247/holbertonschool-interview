#!/usr/bin/python3
"""given a pile of coins of different values determine the fewest coins"""


def makeChange(coins, total):
    """determine the fewest number of coins"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    i, number_coins = (0, 0)
    len_coins = len(coins)
    cpy_total = total

    while(i < len_coins and cpy_total > 0):
        if (cpy_total - coins[i]) >= 0:
            cpy_total -= coins[i]
            number_coins += 1
        else:
            i += 1

    checker = cpy_total > 0 and number_coins > 0
    if checker or number == 0:
        return -1
    else:
        return number_coins
