# import math
# def floyd_warshall(graph):
#     n= len(graph)
#     dist= [[math.inf]*n for _ in range(n)]
#     for i in range(n):
#         dist[i][i] = 0
#         for j in range(n):
#             if graph[i][j] != -1:
#                 dist[i][j] = graph[i][j]

#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if dist[i][k] + dist[k][j] < dist[i][j]:
#                     dist[i][j] = dist[i][k] + dist[k][j]

#     return dist


# import math

# def floyd_warshall(graph):
#     n = len(graph)

#     dist = [[math.inf]*n for _ in range(n)]

#     for i in range(n):
#         dist[i][i]= 0 

#         for j in range(n):
#             if graph[i][j] != -1:
#                 dist[i][j] = graph[i][j]
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):

#                 if dist[i][k] + dist[k][j] < dist[i][j]:
#                     dist[i][j]= dist[i][k] + dist[k][j]

#     return dist


# import math

# def floyd_warshall(graph):

#     n = len(graph)
#     dist= [[math.inf]*n for _ in range(n)]

#     for i in range(n):
#         dist[i][i]= 0

#         for j in range(n):
#             if dist[i][j] != -1:
#                 dist[i][j] = graph[i][j]

#     for k in range(n):
#         for i in range(n):
#             for j in range(n):

#                 if dist[i][j]> dist[i][k]+ dist[k][j]:
#                     dist[i][j]= dist[i][k]+ dist[k][j]
#     return dist




# import math
# def floyd_warshall(graph):
#     n= len(graph)
#     dist = [[math.inf]*n for _ in range(n)]
    
#     for i in range(n):
#         dist[i][i] = 0
        
#         for j in range(n):
#             if dist[i][j] != -1:
#                 dist[i][j]= graph[i][j]

#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
                
#                 if dist[i][j]> dist[i][k] + dist[k][j]:
#                     dist[i][j] = dist[i][k] + dist[k][j]

#     return dist

# graph = [ 
#         [0, 5, -1, 6, -1],
#         [-1, 0, 1, -1, 7],
#         [3, -1, 0, 4, -1],
#         [-1, -1, 2, 0, 3],
#         [2, -1, -1, 5, 0]
#     ] 

# result = floyd_warshall(graph)
# print("Shortest Paths: ")

# for row in result:
#     print([int (x) if x != math.inf else "inf" for x in row])



# import math
# def floyd_warshall(graph):
#     n = len(graph)
#     dist = [[math.inf]*n for _ in range(n)]

#     for i in range(n):
#         dist[i][i] = 0
        
#         for j in range(n):
#             if dist[i][j] != -1:
#                 dist[i][j] = graph[i][j]


#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
                
#                 if dist[i][j]> dist[i][k] + dist[k][j]:
#                     dist[i][j] =  dist[i][k] + dist[k][j]                    
#     return dist

# graph = [
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4]
# ]

# result = floyd_warshall(graph)
# print("Shortest Paths: ")
# for row in result:
#     print([int(x) if x != math.inf else "inf" for x in row])
    
    
    
    
    
    

# import math
# def floyd_warshall(graph):
#     n = len(graph)
#     dist = [[math.inf]*n for _ in range(n)]

#     for i in range(n):
#         dist[i][i] = 0
        
#         for j in range(n):
#             if dist[i][j] != -1:
#                 dist[i][j] = graph[i][j]

#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if dist[i][j] > dist[i][k] + dist[k][j]:
#                     dist[i][j] = dist[i][k] + dist[k][j]                   
#     return dist
# graph = [
#     [0,1,2,3,4],
#     [0,1,2,3,4],
#     [0,1,2,3,4],
#     [0,1,2,3,4]
# ]
# result = floyd_warshall(graph)
# print("Shortest Paths: ")

# for row in result:
#     print([int(x) if x != math.inf else "inf" for x in row])


import math

def floyd_warshalll(graph):
    n = len(graph)
    dist = [[math.inf]*n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
        
        for j in range(n):
            if dist[i][j] != -1:
                dist[i][j] = graph[i][j]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                
                if dist[i][j]> dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]
    return dist

graph = [
    [0,1,2,3,4],
    [0,1,2,3,4],
    [0,1,2,3,4],
    [0,1,2,3,4]
]
result = floyd_warshalll(graph)
print("Shortest Paths: ")

for row in result:
    print([int(x) if x != math.inf else "inf" for x in row])