"""This module contains an implementation of the Rabin Karp algorithm.


source: https://www.youtube.com/watch?v=3KXsyZFHidk&t=1s

Notes
-------
- Utilizes modular hashing to calculate hash values for strings
- The modular hash functions mods by the large random prime, P, generated
in order to always keep the hash value within the range of 0 to P - 1. This
prevents integer overflow (although this isn't a problem in Python) and lets
you compute the modular hash for arbitrarily large keys one digit or character
at a time


Steps 

Step 1:
Precompute the value of base ^ (pattern_length - 1) % prime. This is so that you
can always quickly remove the first character in the sliding window during the search
step without having to compute this every time. 

For example, if the string was 415926 and you wanted to go from 41592 to 15926, 
you would end up doing (41592 - (4 * 10 ^ 4)) * 10 + 6. Here, 10 is the base and the pattern
length is 5. Since you know you will be muliplying every integer you want to remove by 10,000,
you can just compute it up front. The modulo is just to prevent integer overflow for languages
where that is an issue.


Step 2:
Compute the hash value of the pattern and of the first 'M' characters of the text string,
where 'M' is the length of the pattern. If the hash values match, compare the actual strings
themselves (they could match because of a collision of hash values). If the strings are the same
then the match occurs starting at index 0

Step 3:
If no match was found at index 0, then perform a search of the remainder of the text string
using a sliding window technique. At each step, subtract the hash value of the first character 
in the window from the text hash and then expand the window by one and add the hash value of the newly
added character to the text hash. If the text hash equals the pattern hash perform, compare the 
actual strings against each other in order to guard against a possible collision of hash values.

In the subtraction step, the reason you need to add the prime to the text hash before subtracting
the value of the first character in the window is to guard against the chance of the hash value being
really small. This would cause the subtraction of the hash value of the first character to produce a
negiatve number, which would make the modulo operatino return an incorrect value.

The order of operations for the subtraction step is:
    - Multiply rolling hash by the first character
    - Mod that result by the large prime
    - Add the current text hash and the large prime
    - Subtract the modded result from the sum of the text hash and the large prime
    - Finally mod by the large prime again to`

"""


# Las Vegas version

# time complexity: O(n + m), where 'n' is the length of the text and 'm' is the
# length of the pattern
# space complexity: O(1)
def rabin_karp(pattern, text, base=256):
    """Implementation of the Rabin-Karp string match algorithm.
    Returns the index of the first occurrence of the given pattern
    in the large text.
    """
    # Handle edge cases
    if pattern == "" or text == "" or len(pattern) > len(text):
        return -1
    pattern_length = len(pattern)
    prime = generate_large_random_prime() # represents the 'hash table' size

    rolling_hash = 1  # precompute base ^ (pattern_length - 1) % prime
    for index in range(1, pattern_length):
        rolling_hash = (base * rolling_hash) % prime
    
    # Calculate pattern hash and the hash of the first 'M' characters
    # of the text string, where 'M' is the length of the pattern
    pattern_hash = calculate_hash(pattern, pattern_length, base, prime)
    text_hash = calculate_hash(text, pattern_length, base, prime)

    # If there is a match betweeb both the hash and the strings, you can
    # return early
    if pattern_hash == text_hash:
        if pattern == text[0:pattern_length]:
            return 0
    return search(pattern, text, text_hash, pattern_hash, rolling_hash, prime, base)


def generate_large_random_prime():
    return 997


def calculate_hash(string, pattern_length, base, prime):
    pattern_hash = 0
    for index in range(pattern_length):
        pattern_hash = (base * pattern_hash + ord(string[index])) % prime
    return pattern_hash


def search(pattern, text, text_hash, pattern_hash, rolling_hash, prime, base):
    text_length = len(text)
    pattern_length = len(pattern)
    for index in range(pattern_length, text_length):
        # subtract character from start of substring
        text_hash = (
            text_hash + prime - rolling_hash * ord(text[index - pattern_length]) % prime
        ) % prime

        # add next character to end of substring
        text_hash = (text_hash * base + ord(text[index])) % prime
        if pattern_hash == text_hash:
            start_of_pattern = index - pattern_length + 1
            if pattern == text[start_of_pattern : index + 1]:
                return start_of_pattern
    return -1




