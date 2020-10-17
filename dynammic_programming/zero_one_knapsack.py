"""This module contains my solution to the 0-1 Knapsack problem.
Problem Statement:

"""

from pprint import pprint
from collections import namedtuple

# Bottom Up Solution
# The weight variable represents a row in the matrix and num_items represents a column
# Time complexity: O(n * m), where 'n' is the number of items and 'm' is the maximum weight
# space complexity: O(n * m)
def knapsack_bottom_up(items, max_weight):
    total_items = len(items)
    memo = [[None] * (total_items + 1) for num in range(max_weight + 1)]
    for weight in range(max_weight + 1):
        for num_items in range(total_items + 1):
            # Base Cases: Weight is 0 or no items to choose from
            if weight == 0 or num_items == 0:
                memo[weight][num_items] = 0
            # Case 1: The current item's weight is greater than the remaining weight, so pass
            # on choosing this item
            elif items[num_items - 1].weight > weight:
                memo[weight][num_items] = memo[weight][num_items - 1]
            # Case 2: Take the greater between the result of passing on this item or
            # choosing this item
            else:
                item = items[num_items - 1]
                memo[weight][num_items] = max(
                    memo[weight][num_items - 1],
                    memo[weight - item.weight][num_items - 1] + item.value,
                )
    return memo[max_weight][total_items]


# Top Down Solution
def knapsack_top_down(items, max_weight):
    index = len(items) - 1
    running_total = 0
    memo = [[None] * (max_weight + 1) for num in range(len(items) + 1)]
    return find_max_item_value(items, max_weight, index, running_total, memo)


def find_max_item_value(items, remaining_weight, index, running_total, memo):
    # Check for memoized value
    if memo[remaining_weight][index + 1] is not None:
        return memo[remaining_weight][index + 1]

    # Base Cases: Weight is 0 or no items to choose from
    if remaining_weight == 0 or index < 0:
        memo[remaining_weight][index + 1] = running_total
        return memo[remaining_weight][index + 1]

    current_item = items[index]
    result_one = find_max_item_value(
        items, remaining_weight, index - 1, running_total, memo
    )

    # Case 1: If this item's weight falls within the remaining weight, take the greater between the
    # result of passing on this item or choosing this item
    if current_item.weight <= remaining_weight:
        result_two = find_max_item_value(
            items,
            remaining_weight - current_item.weight,
            index - 1,
            running_total + current_item.value,
            memo,
        )
        memo[remaining_weight][index + 1] = max(result_one, result_two)
    # Case 2: The item's weight turned out to be greater than the remaining weight, so just return
    # the result of passing on choosing this item.
    memo[remaining_weight][index + 1] = result_one
    return memo[remaining_weight][index + 1]


# Test Cases
Item = namedtuple("Item", ["weight", "value"])


def test_bottom_up():
    expected = 100
    max_weight = 5
    items = [Item(5, 60), Item(1, 30), Item(2, 70), Item(3, 30)]
    actual = knapsack_bottom_up(items, max_weight)
    pprint(f"Items: {items}, Max Weight: {max_weight}")
    print(f"Expected: {expected}, Actual: {actual}\n")


def test_top_down():
    expected = 100
    max_weight = 5
    items = [Item(5, 60), Item(1, 30), Item(2, 70), Item(3, 30)]
    actual = knapsack_bottom_up(items, max_weight)
    actual = knapsack_bottom_up(items, max_weight)
    pprint(f"Items: {items}, Max Weight: {max_weight}")
    print(f"Expected: {expected}, Actual: {actual}")


test_bottom_up()
test_top_down()
