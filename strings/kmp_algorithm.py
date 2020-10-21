"""This module contains my implementation of the Knuth-Morris-Pratt pattern
matching algorithm. The algorithm finds the first occurrence of
a pattern in a larger string and returns its index.
"""


# time complexity: O(n + m), where 'm' is the length of the pattern and
# 'n' is the length of the string

# space complexity: O(m)
def kmp_algorithm(pattern, string):
    # Pattern can't be an empty string
    if pattern == "":
        return -1
    # Build LPS table for the pattern string
    longest_prefix_suffix_table = build_longest_prefix_suffix_table(pattern)

    # define pointers
    string_pointer = 0
    pattern_pointer = 0
    start = string_pointer
    # Loop as long as there are characters in the string remaining
    # to consider and as long as the pattern is not longer than
    # the remaining characters in the string
    while string_pointer < len(string) and len(pattern) <= len(string) - start:

        # Move both pointers forward as long as the characters they
        # rest at match
        while (
            string_pointer < len(string)
            and pattern_pointer < len(pattern)
            and string[string_pointer] == pattern[pattern_pointer]
        ):
            string_pointer += 1
            pattern_pointer += 1

        # If pattern pointer is at end of the pattern string,
        # then a match was found
        if pattern_pointer == len(pattern):
            return start

        # Backtrack the pattern pointer if it's > 0
        # If it's equal to 0, then there are no characters to backtrack to
        # and you have to just increment the string pointer
        if pattern_pointer > 0:
            pattern_pointer = longest_prefix_suffix_table[pattern_pointer - 1]
        else:
            string_pointer += 1
        start += 1

    # Pattern not found in string
    return -1


def build_longest_prefix_suffix_table(pattern):
    """Return a list named longest_prefix_suffix_table (lps for short),
    where lps[i] equals the length of the longest suffix that is also a prefix
    from indicies 0 to 'i' inclusive.
    """
    longest_prefix_suffix_table = [0]
    slow = 0
    fast = 1

    # Fast pointer will reach the end of the pattern
    # before the slow pointer
    while fast < len(pattern):

        # If the characters are equal, then the longest suffix that is
        # also a prefix from indices 0 -> fast (inclusive) == slow + 1
        while fast < len(pattern) and pattern[slow] == pattern[fast]:
            longest_prefix_suffix_table.append(slow + 1)
            slow += 1
            fast += 1

        # You've finished evaluating the entire pattern, so break
        if fast == len(pattern):
            break
        # Mismatched characters, so the longest suffix that is also
        # a prefix from indicies 0 -> fast (inclusive) is 0
        longest_prefix_suffix_table.append(0)

        # Move slow pointer back to the beginning
        slow = 0
        fast += 1
    return longest_prefix_suffix_table


result = kmp_algorithm("aaab", "aaaaab")
print(result)
