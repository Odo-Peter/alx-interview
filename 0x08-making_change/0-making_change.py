#!/usr/bin/python3
"""
Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
"""


def makeChange(coins, total):
    """Make changes
    """
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)
    count = 0

    for i in range(len(coins)):
        while total > 0:
            if total // coins[i] > 0:
                count += 1
                total -= coins[i]
            else:
                break

    return -1 if total > 0 else count
