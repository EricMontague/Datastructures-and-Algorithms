"""This file contains notes about the concept of hashing and hash tables.

Sources
---------
https://algs4.cs.princeton.edu/34hash/



Hashing
------
- Any search algorithm or data structure that uses hashing consists of two separate
parts, computing a hash function, and collision resolution

- A hash function is any function that takes in an arbitrary key and maps it to a
range of fixed-sized values

- A good hash function uniformly distributes keys within the fixed-size range of values

- Keys to a hash function can be (nearly) any type of data (integers, strings, floats, objects etc.),
although this depends on the programming language

- There a three primary requirements for implementing a good hash function for
a given data type:
    - The function should be deterministic: Equals keys must produce the same hash value
    - The function should be efficient to compute
    - It should uniformly distribute the keys

Hash Tables
---------
- A hash table is a data structure that allows you to associate any arbitrary
key with a value
- The underlying data structure in a hash table is an array, that can hold
'M' key-value pairs, one pair at each index from 0 to M - 1
- The load factory of a hash table is N/M, where 'N' is the number of key-value 
pairs stored in the table and 'M' is the size of the table


Hashing Integers
- The most commonly used method for hashing integers is modular hashing (see example below) 
-In modular hashing, you choose the array size 'M' to be prime, and, for any positive integer key
'k', compute the remainder when dividing 'k' by 'M'. 
- This is effective because it is  easy to compute and will disperse the keys evenly 
between 0 and M - 1


Hashing Floats
- If the keys are real numbers between 0 and 1, you can just multiply by M and round down
to the nearest integer to get an index between 0 and M - 1. 
- The flaw with this however, is that it gives more weight to the most significant bits
of the keys; the least significant bits play no role.
- One way to address this is to use modular hashing on the binary representation of the keys
(this is what Java does)


Hashing Strings
- If your key is a string, you can simply treat it as a huge integer and perform
modular hashing (see example below). 


Compound Keys
- If the key type has multiple integer fields, we can typically mix them together in
the way described for string keys. See the example of hashing a US phone number below


Handling Collisions
-------------------
- A collision is what happens when two different keys, when passed to a hash function,
produce the same value.
- Collision resolution is the strategy for handling the case for when this occurs. Below
are some common strategies for resolving collisions in a hash table


Hashing with Separate Chaining

- Instead of storing each key-value pair at an index in the array underlying the hash table,
you can store a linked list at each index.
- Each node in the linked list stores a key-value pair that hashes to that index
- 'M' should be sufficiently large so that the lists are sufficiently short to enable efficient
search through a two-step process: hash to find the list that could contain the key,
then sequentially search through that list for the key
- In a separate-chaining hash table with 'M' lists and 'N' keys, the probability that the number
of keys in a list is wihtin a small constant factor of N/M is extremely close to 1. This assumes
an ideal hash function (uniformly distributes the keys)
- In a separate-chaining hash table with 'M' lists and 'N' keys, the number of 
compares (equality tests) for search and insert is proportional to N/M


Hashing with Linear Probing (a type of open addressing method )

- Store 'N' key-value pairs in a table of size M > N, relying on empty entries in the table
to help with collission resolution.
- When there is a collision, then you just check the next entry in the table (by increment the index)
- There are four possible outcomes:
    - Key equal to search key: search hit
    - Empty position (null key at indexed position): search miss
    - Key not equal to search key: Try next entry
    - Tombestone (a key-value that used to exist was deleted): Try next entry
- The tombstone is a flag or object that you insert into a slot of the hash table when you are performing
a deletion of a key-value pair. You need to do this rather than setting the index to null to prevent
false negatives (search misses that actually aren't misses) when searching for a key 

- The performance of this technique is dependent on the load factor (N/M), we it is interpreted differently
- For separate chaining, the load factory is the average number of items per list and is generally
larger than 1
- However, for open addressing, the load factory is the percentage of table positions that are occupied;
it MUST be less than 1 (M should be greater than N)
- In a linear probing hash table of size 'M' with N = load_factor * M keys, the average number of probes
is about 1/2 * (1 + 1/ (1 - load_factor)) for search hists and about 1/2 * (1 + 1/ (1 - load_factor) ^ 2)
for search misses or inserts

"""


# Modular hashing for positive integers
def hash_function_integers(key, table_size):
    """Given a key and the size of the hash table, return
    a hash value between the range 0 to M - 1, where M is the
    given table size. The key is assumed to be an integer
    """
    return key % table_size


# Modular hashing for strings
def hash_function_strings(key, table_size):
    """Given a key and the size of the hash table, return
    a hash value between the range 0 to M - 1, where M is the
    given table size. The key is assumed to be a string
    """
    small_prime = 31
    hash_value = 0
    for index in range(len(key)):
        hash_value = (small_prime * hash_value + ord(key[index])) % table_size
    return hash_value


# Modular hashing for a compound key given as a phone number
def hash_function_phone_number(key, table_size):
    """Given a key and the size of the hash table, return
    a hash value between the range 0 to M - 1, where M is the
    given table size. The key is assumed to be a phone number
    in the format of 123-456-7890 as a string
    """
    area, exchange, extension = map(int, key.split("-"))
    small_prime = 31
    hash_value = (
        ((area * small_prime + exchange) % table_size) * small_prime + extension
    ) % table_size
    return hash_value
