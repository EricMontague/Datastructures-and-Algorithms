"""This module contains an implementation of the Rabin Karp algorithm."""


# Las Vegas version


def rabin_karp(pattern, text, base=256):
    """Implementation of the Rabin-Karp string match algorithm.
    Returns the index of the first occurrence of the given pattern
    in the large text.
    """

    pattern_length = len(pattern)
    prime = generate_large_random_prime()

    rolling_hash = 1  # base ^ (pattern_length - 1) % prime
    for index in range(1, pattern_length):
        rolling_hash = (base * rolling_hash) % prime
    pattern_hash = calculate_hash(pattern, pattern_length, base, prime)
    return search(pattern, text, pattern_hash, rolling_hash, prime, base)


def generate_large_random_prime():
    return 997


def calculate_hash(string, pattern_length, base, prime):
    pattern_hash = 0
    for index in range(pattern_length):
        pattern_hash = (base * pattern_hash + ord(string[index])) % prime
    return pattern_hash


def search(pattern, text, pattern_hash, rolling_hash, prime, base):
    text_length = len(text)
    pattern_length = len(pattern)
    text_hash = calculate_hash(text, pattern_length, base, prime)
    if pattern_hash == text_hash:
        if pattern == text[0:pattern_length]:
            return 0
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

