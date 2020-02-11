# Solving Problems

- examplify: write out a simple example of the problem
- similarity: is problem similar to another? Modify existing solution
- simplify & generalize: find simply solution, generalize
- base case & build: solve for the base case...
- rand structure: just go through data structures and see what works

### Choosing the right Alg

`straight coding`: step by step instructions given
`BFS`: number of step or shortest path with certain constraints
`flood fill`: like BFS but no path asked for (find all reachable areas)
`brute-force/backtracking`: find every possible config/subset of items

- `greedy`: make locally optimum choice at each stage
- `hill climbing`: start with solution, incrementally improve
- `heuristic`: not optimal or perfect, but sufficient to help in most cases
- `exact algorithm`: algorithm that always solves problem to optimallity
- `dynamic programming`:
- `memoization`: storing expensive results for later re-use

## Space Time trade-off

- try using auxiliary data structure -- what could I store that would save time?
- example: do something in a single pass over an array O(n) time using a hash table O(n) space VS doing something in multiple passes O(n^2) without using any extra space O(1)

## Tips

- always consider hash tables!
- if arrays involved, try sorting
- if search related try binary search
- start brute force, look for repeated work to remove
- use two pointers (move at diff rates, directions)
- if tree/graph traversal, consider stacks, also recursion

- two pointers (slow and fast / one only advances when the other hits some condition / one moves then the other jumps to some spot)

- divide and conquer: Does solving the problem for size (N – 1) make solving it for size N any easier? If so, try to solve recursively and/or with dynamic programming. (Using the max/min function can help a lot in recursive or dynamic programming problems.)

A lot of problems can be treated as graph problems and/or use breadth-first or depth-first traversal.

If you have a lot of strings, try putting them in a prefix tree / trie.

Any time you repeatedly have to take the min or max of a dynamic collection, think heaps. (If you don’t need to insert random elements, prefer a sorted array.)

When you have a solution, pull out some small part of it and write that code.
Don't try to just write it all in one go.
Write a part, make sure it is right, then onto the next one.

Don't make assumptions.
"The inner loop will have to run k times"
Are you sure? Try the edge cases to verify.