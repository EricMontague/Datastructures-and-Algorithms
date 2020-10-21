"""This module contains an implementation of a naive pattern
matching algorithm. It will return the starting index of the
first occurence of a pattern within a larger string.
"""


# time complexity: O(n * m), where 'm' is the length of the pattern
# and 'n' is the length of the large string
# space complexity: O(1)
def search(pattern, string):

    # Pattern can't be an empty string
    if pattern == "":
        return -1

    start = 0
    string_pointer = 0

    # Also handles edge cases where you receive an empty string as well as
    # When the length of the pattern is greater than the remaining substring to search.
    # This includes when the pattern is longer than the given string itself
    while string_pointer < len(string) and len(pattern) <= len(string) - start:
        # Set pattern pointer to 0 before each search attempt
        pattern_pointer = 0

        # Move the string pointer forward until the character it rests at
        # is the same as the first character of the pattern
        while string_pointer < len(string) and string[string_pointer] != pattern[0]:
            string_pointer += 1

        # Save the starting point of this match to return later
        start = string_pointer

        # Move both pointers forward as long as the characters they rest at match
        while (
            string_pointer < len(string)
            and pattern_pointer < len(pattern)
            and string[string_pointer] == pattern[pattern_pointer]
        ):
            string_pointer += 1
            pattern_pointer += 1

        # If the pattern pointer has reached the end of the pattern, then
        # we've found a match
        if pattern_pointer == len(pattern):
            return start

        # String pointer should start one index after where the last search
        # started from
        string_pointer = start + 1

    # pattern was not found in string
    return -1

