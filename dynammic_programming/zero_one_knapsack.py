"""This module contains my solution to the 0-1 Knapsack problem.

Problem Statement: Given a list of items, each with a weight and a value,
put these items into a knapsack of capacity, W, such that the total value
of all items in the knapsack is maximized. You cannot break an item, either
pick the item or don't pick it (0-1 property)


"""

from pprint import pprint
from collections import namedtuple

# Bottom Up Solution
# The num_items variable represents a row in the matrix and weight represents a column
# Time complexity: O(n * m), where 'n' is the number of items and 'm' is the maximum weight
# space complexity: O(n * m)
def knapsack_bottom_up(items, max_weight):
    total_items = len(items)
    memo = [[None] * (max_weight + 1) for num in range(total_items + 1)]
    for num_items in range(total_items + 1):
        for weight in range(max_weight + 1):
            # Base Cases: Weight is 0 or no items to choose from
            if num_items == 0 or weight == 0:
                memo[num_items][weight] = 0
            # Case 1: The current item's weight is greater than the remaining weight, so pass
            # on choosing this item
            elif items[num_items - 1].weight > weight:
                memo[num_items][weight] = memo[num_items - 1][weight]
            # Case 2: Take the greater between the result of passing on this item or
            # choosing this item
            else:
                item = items[num_items - 1]
                memo[num_items][weight] = max(
                    memo[num_items - 1][weight],
                    memo[num_items - 1][weight - item.weight] + item.value,
                )
    return memo[total_items][max_weight]


# Top Down Solution
# Time complexity: O(n * m), where 'n' is the number of items and 'm' is the maximum weight
# space complexity: O(n * m)
def knapsack_top_down(items, max_weight):
    total_items = len(items)
    running_total = 0
    memo = [[None] * (max_weight + 1) for num in range(total_items + 1)]
    return find_max_item_value(items, max_weight, total_items, running_total, memo)


def find_max_item_value(items, remaining_weight, num_items, running_total, memo):
    # Check for memoized value
    if memo[num_items][remaining_weight] is not None:
        return memo[num_items][remaining_weight]

    # Base Cases: Weight is 0 or no items to choose from
    if remaining_weight == 0 or num_items == 0:
        result = running_total
    
    # Case 1: The item's weight turned out to be greater than the remaining weight, so pass on choosing
    # this item
    elif items[num_items - 1].weight > remaining_weight:
        result = find_max_item_value(
            items, remaining_weight, num_items - 1, running_total, memo
        )
    # Case 2: The item's weight falls within the remaining weight constraint, so take the greater between the
    # result of passing on this item or choosing this item
    else:
        temp1 = find_max_item_value(
            items, remaining_weight, num_items - 1, running_total, memo
        )
        temp2 = find_max_item_value(
            items,
            remaining_weight - items[num_items - 1].weight,
            num_items - 1,
            running_total + items[num_items - 1].value,
            memo,
        )
        result = max(temp1, temp2)

        
    memo[num_items][remaining_weight] = result
    return memo[num_items][remaining_weight]




# Follow up to the knap sack problem where you're asked to return the items that you
# placed in the knapsack along with their total value
def knapsack_bottom_up_return_items(items, max_weight):
    total_items = len(items)
    memo = [[None] * (max_weight + 1) for num in range(total_items + 1)]
    for num_items in range(total_items + 1):
        for weight in range(max_weight + 1):
            # Base Cases: Weight is 0 or no items to choose from
            if num_items == 0 or weight == 0:
                memo[num_items][weight] = 0
            # Case 1: The current item's weight is greater than the remaining weight, so pass
            # on choosing this item
            elif items[num_items - 1].weight > weight:
                memo[num_items][weight] = memo[num_items - 1][weight]
            # Case 2: Take the greater between the result of passing on this item or
            # choosing this item
            else:
                item = items[num_items - 1]
                memo[num_items][weight] = max(
                    memo[num_items - 1][weight],
                    memo[num_items - 1][weight - item.weight] + item.value,
                )
    items_chosen = find_chosen_items(memo, items, total_items, max_weight)
    return items_chosen, memo[total_items][max_weight]


def find_chosen_items(memo, items, total_items, max_weight):
    """Return the items that were chosen to be put in the knapsack."""
    chosen_items = []
    num_items = total_items
    weight = max_weight
    while num_items > 0 and weight > 0:
        current_item = items[num_items - 1]
        # You passed on this item either because the item was too large, or because passing on it gave you
        # a more maximal value than choosing it. Go back to the subproblem where you
        # had the same weight constraint, but one less item
        if current_item.weight > weight or current_item.value == memo[num_items - 1][weight]:
            num_items -= 1
        # You chose this item because it gave you a more maximal value than passing on it
        elif current_item.value + memo[num_items - 1][weight - current_item.weight] == memo[num_items][weight]:
            chosen_items.append(current_item)
            num_items -= 1
            weight -= current_item.weight
    return chosen_items



# A bottom up solution for the 0-1 knapsack problem that is optimized for space
# A tradeoff here is that you can no longer find which items that you chose
# The intuition behind this optimization is that whenever you need to get the result from a 
# prior subproblem, you always end up looking up the value in the prior row in the memo table.
# Since that's the case, you only need to store information for the previous row in the table
# and use that to fill up a list representing the current row in the table
def knapsack_bottom_up_space_optimized(items, max_weight):
    total_items = len(items)
    previous = [0] * (max_weight + 1)
    current = [None] * (max_weight + 1)
    for num_items in range(1, total_items + 1):
        current = [None] * (max_weight + 1)
        for weight in range(max_weight + 1):
            # Base Cases: Weight is 0 
            if weight == 0:
                current[weight] = 0
            # Case 1: The current item's weight is greater than the remaining weight, so pass
            # on choosing this item
            elif items[num_items - 1].weight > weight:
                current[weight] = previous[weight]
            # Case 2: Take the greater between the result of passing on this item or
            # choosing this item
            else:
                item = items[num_items - 1]
                current[weight] = max(
                    previous[weight],
                    previous[weight - item.weight] + item.value
                )
        previous = current
    return current[max_weight]

# Test Cases
Item = namedtuple("Item", ["weight", "value"])


def test_bottom_up():

    # Test case 1
    expected = 100
    max_weight = 5
    items = [Item(5, 60), Item(1, 30), Item(2, 70), Item(3, 30)]
    actual = knapsack_bottom_up(items, max_weight)
    pprint(f"Items: {items}, Max Weight: {max_weight}")
    print(f"Expected: {expected}, Actual: {actual}\n")


    # Test case 2
    expected = 220
    max_weight = 50
    items = [Item(10, 60), Item(20, 100), Item(30, 120)]
    actual = knapsack_bottom_up(items, max_weight)
    pprint(f"Items: {items}, Max Weight: {max_weight}")
    print(f"Expected: {expected}, Actual: {actual}\n")

def test_top_down():

    # Test case 1
    expected = 100
    max_weight = 5
    items = [Item(5, 60), Item(1, 30), Item(2, 70), Item(3, 30)]
    actual = knapsack_top_down(items, max_weight)
    pprint(f"Items: {items}, Max Weight: {max_weight}")
    print(f"Expected: {expected}, Actual: {actual}\n")


    # Test case 2
    expected = 220
    max_weight = 50
    items = [Item(10, 60), Item(20, 100), Item(30, 120)]
    actual = knapsack_top_down(items, max_weight)
    pprint(f"Items: {items}, Max Weight: {max_weight}")
    print(f"Expected: {expected}, Actual: {actual}\n")


def test_knapsack_bottom_up_return_items():
    # Test case 1
    expected = 100
    max_weight = 5
    items = [Item(5, 60), Item(1, 30), Item(2, 70), Item(3, 30)]
    chosen_items, items_weight = knapsack_bottom_up_return_items(items, max_weight)

    print(f"Expected weight: {expected}, Actual: {items_weight}")
    print(f"Result - Chosen items: {chosen_items}\n")


    # Test case 2
    expected = 220
    max_weight = 50
    items = [Item(10, 60), Item(20, 100), Item(30, 120)]
    chosen_items, items_weight = knapsack_bottom_up_return_items(items, max_weight)
    
    print(f"Expected weight: {expected}, Actual: {items_weight}")
    print(f"Result - Chosen items: {chosen_items}\n")


def test_knapsack_bottom_up_space_optimized():
    # Test case 1
    expected = 100
    max_weight = 5
    items = [Item(5, 60), Item(1, 30), Item(2, 70), Item(3, 30)]
    actual = knapsack_bottom_up_space_optimized(items, max_weight)
    pprint(f"Items: {items}, Max Weight: {max_weight}")
    print(f"Expected: {expected}, Actual: {actual}\n")


    # Test case 2
    expected = 220
    max_weight = 50
    items = [Item(10, 60), Item(20, 100), Item(30, 120)]
    actual = knapsack_bottom_up_space_optimized(items, max_weight)
    pprint(f"Items: {items}, Max Weight: {max_weight}")
    print(f"Expected: {expected}, Actual: {actual}\n")


test_knapsack_bottom_up_space_optimized()