def is_clique(vertices, adj):
    m = len(vertices)
    for i in range(m):
        for j in range(i+1, m):
            u, v = vertices[i], vertices[j]
            if adj[u][v] == 0:
                return False
    return True

def max_clique_backtrack(n,adj,vertices,i,max_clique):
    if len(vertices) > len(max_clique[0]):
        max_clique[0] = vertices[:]

    for j in range(i+1, n+1):
        vertices.append(j)
        if is_clique(vertices, adj):
            max_clique_backtrack(n, adj, vertices, j, max_clique)
        vertices.pop()

def find_maximum_clique(n, edges):
    adj = [[0]*(n+1) for _ in range(n+1)]
    for u, v in edges:
        adj[u][v] = 1
        adj[v][u] = 1
    vertices = []
    max_clique =[[]]
    max_clique_backtrack(n, adj, vertices, 0, max_clique)
    return max_clique[0]

if __name__ == "__main__":
    n = 5
    edges = [
        [1,2],
        [2,3],
        [3,1],
        [3,4],
        [4,5],
        [5,3]
    ]
    maximum = find_maximum_clique(n, edges)
    print("Maximum Clique: ", maximum)