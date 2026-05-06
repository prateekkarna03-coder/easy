import heapq
from collections import defaultdict

def dijkstra(graph, start):
    dist = defaultdict(lambda: float("inf"))
    dist[start] = 0

    pq = [(0, start)]
    prev = {}

    while pq:
        du, u = heapq.heappop(pq)

        if du > dist[u]:
            continue

        for v, w in graph[u].items():
            alt = dist[u] + w

            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))

    return dist, prev

graph = {
    0: {1:2, 2:3},
    1: {0:2, 2:1, 3:4},
    2: {0:3, 1:1, 3:2, 4:5},
    3: {1:4, 2:2, 4:3},
    4: {0:5, 3:3}
}

dist, prev = dijkstra(graph, 0)
print("Distances from A: ", {chr(65+k): dist[k] for k in dist})