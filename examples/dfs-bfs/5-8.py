# bfs 너비 우선 탐색 + 큐
from collections import deque

def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    # 큐가 빌 때까지 반복
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

graph=[
    [],
    [2,3,8], # 1에 연결된 노드들
    [1,7], # 2에 연결된 노드들
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7] # 8에 연결된 노드들
]

visited=[False]*9

bfs(graph, 1, visited)
