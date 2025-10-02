#Problem: Maximum Flow (Edmonds-Karp Algorithm)

#Problem Statement:
#Given a directed graph with capacities on edges, find the maximum flow from a source node s to a sink node t.

#Example:

#graph = {
   # 0: {1: 16, 2: 13},
   # 1: {2: 10, 3: 12},
   # 2: {1: 4, 4: 14},
   # 3: {2: 9, 5: 20},
   # 4: {3: 7, 5: 4},
   # 5: {}
#}
#source = 0
#sink = 5
#Output: 23







from collections import deque

def bfs(residualGraph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        u = queue.popleft()
        for v, capacity in residualGraph[u].items():
            if v not in visited and capacity > 0:
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
                queue.append(v)
    return False

def edmondsKarp(graph, source, sink):
    residualGraph = {u: dict(v) for u, v in graph.items()}
    parent = {}
    maxFlow = 0
    
    while bfs(residualGraph, source, sink, parent):
        # Find minimum residual capacity along the path
        pathFlow = float('inf')
        s = sink
        while s != source:
            pathFlow = min(pathFlow, residualGraph[parent[s]][s])
            s = parent[s]
        
        # Update residual capacities
        v = sink
        while v != source:
            u = parent[v]
            residualGraph[u][v] -= pathFlow
            residualGraph[v].setdefault(u, 0)
            residualGraph[v][u] += pathFlow
            v = u
        
        maxFlow += pathFlow
    
    return maxFlow

# Example usage
graph = {
    0: {1: 16, 2: 13},
    1: {2: 10, 3: 12},
    2: {1: 4, 4: 14},
    3: {2: 9, 5: 20},
    4: {3: 7, 5: 4},
    5: {}
}
source = 0
sink = 5
print("Maximum Flow:", edmondsKarp(graph, source, sink))
