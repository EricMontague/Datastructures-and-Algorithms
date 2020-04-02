"""This script contains a solution to a common singly linked list problem:
Find the value that is 'n' from the end in a singly linked list.
"""

#Note: The last node is counted as 1
def value_n_from_end(head, n):
    """Given the head of a singly linked list,
    return the value of the node that is 'n'
    from the end of the list.
    """
    first = head
    second = head
    for num in range(n - 1):
        if second is None:
            return second
        second = second.next
    
    while second.next is not None:
        first = first.next
        second = second.next
    return first.data
    