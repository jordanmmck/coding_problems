# Graphs

## Concept

- collection of nodes and edges
- can be described by 2 sets, G = (V,E)
- connected graph must have at least v-1 edges
- maximum edges is v(v-1)/2

## Representations

### Adjacency List

- better for sparse graph

### Adjacency Matrix

- Make n by n matrix of 0/1s indicating presence of edges
- `Laplacian Matrix` has info about the degrees of vertices
- `Distance Matrix` has length value of shortest path between the given vertices

### Graph Algorithms

~~~ Minimum Spanning Tree (MST, MWST)

`MST`: Like connecting cities with telephone lines. If each edge has a distinct weight then there will be only one MWST.
`Cycle Property`: For any cycle in the graph, the most expensive edge in that cycle must not be in MWST.
`Cut Property`: for any cut that could be made in the graph, if there is a cheapest edge on that cut then this must be in MWST.

+++ Borůvka's (grow many individual trees)
-requires that all edge weights are distinct
1. Visit each vertex adding their cheapest outgoing edge
2. There will now be some connected components
3. Go through these components and add the cheapest outgoing edge from the whole component. Repeat until done.
`runtime`: O(E log V)

+++ Prim's (grow tree out from small seed)
1. Start at any vertex
2. Choose cheapest edge from existing tree to outside
`runtime (adj matrix)`: O(V^2)
`runtime (binary heap and adj list)`: O(E log V)
`runtime (fib heap and adj list)`: O(E + V log V)

+++ Kruskal (add cheapest edges until all connected)
1. Check the cheapest of all edges, if it connects two trees then add it, repeat
`runtime`: O(E log V)

~~~ DFS
-for trees: pre order, in order, post order
`runtime (worst)`: O(V+E)

~~~ BFS
`runtime (worst)`: O(V+E)

~~~ Shortest path between Nodes (single source shortest path)
Given some source node, produce for each other node the shortest path to get there. This produces a shortest path tree.

+++ Bellman-Ford
-handles negative weights, AND negative cycle
for i in (0,V-1):
    for u in V:
        for v,w in adj(u):
            dist[v]=min(dist[v],dist[u]+w)

+++ Dijkstra
-can't handle negative CYCLE
-faster than bellman-ford in theory
// empty pq
PQ = []
dist={a:inf, b:inf, ...}
start at some vertex, throw all edges into pq. pq is small priority
dist={a:0, b:inf, ...}
once you arrive at a certain vertex then you have the shortest path to it
stuff added to q must go after things with same weight
like BFS but with a pq instead of queue

~~~ Path Finding
+++ A*

### Network Flow

~~~ Max flow Min cut theorem

+++ Ford Fulkerson
