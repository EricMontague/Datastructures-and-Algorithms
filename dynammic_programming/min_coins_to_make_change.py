"""This module contains algorithms to solve the dynamic programming
Problem - Min Coins to Make Change.

The problem statement can be found here - https://leetcode.com/problems/coin-change/


Recurrence Relation
---------------------
f(c, A) = 0, if A == 0
f(c, A) = 1 + min(f(c, A - c[i])), for all 'i' from 0 to c - 1 where c[i] <= A


- In English, this says, that if you are given an amount of 0,
the minimum number of coins you need to use to make change is 0
- For the recursive case, you need to try all possible combinations to make change
with each coin as long as that coin is less than or equal to the remaining amount
- Take the minimum of all possible paths as your answer
"""

# Bottom Up Solution
# time complexity: O(n * m), where 'n' is the total and 'm' is the length of coins
# space comexplity: O(n)


def min_coins_to_make_change(coins, total):
    if not coins:
        return 0
    memo = [float("inf")] * (total + 1)
    memo[0] = 0
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                memo[amount] = min(memo[amount], 1 + memo[amount - coin])
    if memo[-1] == float("inf"):
        return -1
    return memo[-1]


# Top down solution with Recursion
# time complexity: O(n * m), where 'n' is the amount and 'm' is the length of coins
# space comexplity: O(n)
def coinChange(coins, amount):
    if not coins:
        return 0
    memo = [-1] * (amount + 1)
    min_coins = make_change(coins, amount, memo)
    if min_coins == float("inf"):
        return -1
    return min_coins


def make_change(coins, remaining_amount, memo):
    if remaining_amount == 0:
        min_coins = 0
    elif memo[remaining_amount] >= 0:
        return memo[remaining_amount]
    else:
        min_coins = float("inf")
        for coin in coins:
            if coin <= remaining_amount:
                result = make_change(coins, remaining_amount - coin, memo)
                min_coins = min(min_coins, result + 1)
    memo[remaining_amount] = min_coins
    return memo[remaining_amount]
