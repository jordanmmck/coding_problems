# Heaps

- efficient way of getting the smallest/largest element on demand
- insert and remove are both very efficient (log n)

## Binary Heap

- a heap in the form of a BT, often used for PQs
`Shape Property`: Should be a complete BT (all levels filled, last level goes left to right)
`Heap Property`: the parent is >= (or <=) it's children depending on if this is min/max heap

## Binomial Heap

- similar to Bheap but supports quick merging of two heaps
- implemented as a collection of binomial trees
`binomial tree`: binomial tree of order 0 is a single node, btree of order k has a root whose children are roots of btrees of orders k-1, k-2, ..., 2, 1, 0 in this order.
`runtime (find min)`: Θ( log n )
`runtime (delete min)`: Θ( log n )
`runtime (insert)`: Θ( 1 )
`runtime (merge)`: Θ( log n )

## Fibonacci Heap

- collection of heap ordered trees
- better amortized running time than binomial heap and binary heap
- can help improve runtime of Dijkstra etc
`runtime (find min)`: Θ( 1 )
`runtime (delete min)`: Θ( log n )
`runtime (insert)`: Θ( 1 )
`runtime (merge)`: Θ( 1 )

## Heap Operations

### Insert

1. add element to bottom
2. trickle up
`runtime (binary heap)`: Θ( log n )

### Remove

1. replace root with last element at bottom
2. trickle down
`runtime (binary heap)`: Θ( log n )
