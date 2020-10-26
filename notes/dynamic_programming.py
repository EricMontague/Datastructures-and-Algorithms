"""This file contains my notes about dynamic programming.

Sources
-----------
https://www.youtube.com/watch?v=OQ5jsbhAv_M&t=1124s

- Invented by Richard Bellman (same person as in the Bellman-Ford algorithm)
- A general, powerful algorithm design technique
- Can also be thought of as an exhaustive search
- Can also be thought of as careful brute force
- Great for optimization problems, e.g. Shortest paths, algorithm problems that involve
minimizing or maximizing outcomes
- The basic idea is to take a problem, split it into subproblems, solve those subproblems,
and then re-use the solutions to those subproblems to solve the original problem
- One technique for solving dynamic programming problems is to try all possible solutions
and then pick the best one (can work well for optimization problems where you are trying to
find some minimum or maximum)
- Subproblem dependencies must be acyclic for memoization to work


Recursion and Memoization (Top down):
- Caching the solutions to subproblems in some data structure (usually and array or hash table)
in order to prevent yourself from doing duplicate work and recomputing already solved subproblems
- Resuse these solutions to these subproblems to solve the original problem
- Typically the running time of a memoized DP algorithm can be calculated as 
time = number of subproblems * time /subproblem



Bottom Up:
- Same number of computations as the top down approach
- You are essentially performing a topological sort of the subproblem
dependency DAG
- You can often save more space when writing a bottom up solution
than when using a top down one

"""
