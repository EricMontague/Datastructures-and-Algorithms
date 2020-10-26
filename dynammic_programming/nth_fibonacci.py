"""This module contains algorithms to compute the nth fibonacci number.

Recurrence Relation
-------------------

fib(n) = 0, if n == 0
fib(n) = 1, if n == 1 or n = =2
fib(n) = fib(n - 1) + fib(n - 2), if n > 2


Time complexity Analysis of Top Down Memoized version
-----------------------------------------------------
- fib(n) only recurses the first time it's called, since its
result will be stored in the memo table
- The memoized calls will take constant time
- The number of non-memoized calls is 'n', and each takes constant time
- So the time complexity O(n)

"""

# The below functions assume that all inputs will be valid and that n
# will never be less than 0


# time complexity: O(2 ^ n), where 'n' is the parameter given
# space complexity: O(n)
def naive_fibonacci(n):
    if n == 0:
        fibonacci = 0
    elif n == 1 or n == 2:
        fibonacci = 1
    else:
        fibonacci = naive_fibonacci(n - 1) + naive_fibonacci(n - 2)
    return fibonacci


# time complexity: O(n)
# space complexity: O(n)
def fibonacci_top_down(n):
    memo = {}
    return compute_fibonacci(n, memo)


def compute_fibonacci(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        fibonacci = 0
    elif n == 1 or n == 2:
        fibonacci = 1
    else:
        fibonacci = compute_fibonacci(n - 1, memo) + compute_fibonacci(n - 2, memo)
    memo[n] = fibonacci
    return memo[n]


# time complexity: O(n)
# space complexity: O(n)
def fibonacci_bottom_up(n):
    memo = {0: 0, 1: 1, 2: 1}
    if n <= 2:
        return memo[n]
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


# time complexity: O(n)
# space complexity: O(1)
# Since you only need the last two subproblem's solutions, you can just keep track
# of them in two variables instead of wasting space with a memo table
def fibonacci_bottom_up_space_efficient(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    last = 1
    second_to_last = 1
    for i in range(3, n + 1):
        current = last + second_to_last
        second_to_last = last
        last = current
    return last

