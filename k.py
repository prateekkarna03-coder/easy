class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union (self,x,y):
        px, py = self.find(x), self.find(y)
        if px != py :
            self.parent[px] = py
            return True
        return False
    
def kruskal_mst(edges,n):
    edges.sort(key= lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    for u, v, w in edges:
        if uf.union(u,v):
            mst.append((u,v,w))
    return mst


edges_list = [(0,1,2), (0,2,3), (1,2,1), (1,3,4), (2,3,2), (2,4,5), (2,4,3)]
mst = kruskal_mst(edges_list, 5)
total = sum (w for _, _, w in mst)
print("Kruskal's MST: ", mst)
print("Total Cost: ", total)
        