""" This file contains notes about bloom filters

Sources
--------
https://en.wikipedia.org/wiki/Bloom_filter#Counting_Bloom_filters




Notes
------

- A bloom filter is a space-efficient, probabilistic data structure,
conceived by  Burton Howard Bloom, that is used to test whether an element 
is a member of a set (Wikipedia)

- False positive matches are possible, but false negatives are not. In other
wrods, a query returns either 'possibly in set' or 'definitely not in set'

- Elements can be added to the set, but not removed. It would be impossible
to remove an element from a simple bloom filter because there is no way to 
tell which of the 'k' bits it maps to should be cleared.

- Removing an element may produce false negatives in the query results of the bloom filter

- A one-time removal of an element from a bloom filter can be simulated by having a second
bloom filter that contains items that have been removed.

- However, false positives in the second filter become false negatives in the composite filter,
which may be undesirable. Re-adding the removed item to the first filter is impossible because 
that would mean you would have to remove it from the second filter.

- The more items added, the larger the probability of false positives.

- This data structure was created for applications where the amount of source data
would require an impractically large amount of memory if "conventional" error-free
hashing techniques were applied.

- When the false positive rate gets too high, the bloom filter can be regenerated


Algorithm description
-----------------
- A bloom filter is a bit array of 'm' bits, all set to 0.

- There must be 'k' different hash functions defined, each
of which maps or hashes some set element to one of the 'm' array
positions, generating a uniformly random distribution

- Typically, 'k' is a small constant which depends on the desired false
error rate, 'E', while 'm' is proportional to 'k' and the number of elements
to be added


Insert Method
--------------
- To add an element to the bloom filter, pass the element to each
of the 'k' hash functions to get 'k' array positions. Set the bits
at all of theses positions to 1


Exists Method
--------------

- Pass the given element to each of the 'k' hash functions to get 'k'
array positions. If any of the bits at these positions is 0, the
element in definitely not in the bloom filter.

- If it were, then all the bits would have been set to 1 when
it was inserted.

- If all bits are 1, then either the element is in the bloom filter, or
the bits have by chance been set to 1 during the insertion of other elements,
resulting in a false positive

- In a simple bloom filter, there is no way to distinguish between the two cases,
but more advanced techniques can address this problem




Space and time advantages
--------------------------
- The time it takes to insert an element or check whether an element
is in the bloom filter is O(k), where 'k' is the number of hash functions, which
is constant with respect to the number of elements in the filter

- It is also very space efficient for the use cases where the size of your dataset
cannot fit into memory, or the amount of memory consumed by each element in your
dataset is relatively large



Probability of false positives
----------------------------------




Applications of Bloom filters
-------------------------------

Cache filtering:
- CDNs deploy web caches around the word to cache and serve web content to users with
greater performance and reliability
- Bloom filters can be used to efficiently determine which objects to
store in a web cache
- Nearly 3/4 of the urls accessed from a typical web cache are "one-hit-wonders"
that are accessed by users only once and never again
- This clearly is a waste of disk resources to store one-hit-wonders in a web cache,
since they will never be accessed again
- To prevent one-hit-wonders, a Bloom filter is used to keep track of all URLs that are
accessed by users. A web object is cached only when it has been accessed at least once before
(or whatever number suits your needs)
- This significantly reduces the disk write workload, since one-hit-wonders
are never written to the disk cache
- This also saves cache space on disk, increasing the cache hit rates
- Note that this can also be applied to an in-memory cache as well
"""