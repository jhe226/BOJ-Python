from collections import deque


N, M, V = map(int, input().split())

nodes = []

for n in range(M):
    nodes.append(list(map(int, input().split())))

graph = [[] for _ in range(N+1)]
for node in nodes :
    graph[node[0]].append(node[1])
    graph[node[1]].append(node[0])

graph = list(map(sorted, graph))
visited = [False] * (N + 1)

result = []

def dfs(node, visited, result):
    visited[node] = True
    result.append(node)
    for i in graph[node]:
        if not visited[i]:
            dfs(i, visited, result)
    return result



def bfs(start) :
    visited = [False] * (N + 1)
    
    queue = deque([start])
    visited[start] = True
    
    result = []
    while queue :
        node = queue.popleft()
        result.append(node)
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    return result


for node in dfs(V, visited, result):
    print(node, end = ' ')
print()

for node in bfs(V):
    print(node, end = ' ')
print()
