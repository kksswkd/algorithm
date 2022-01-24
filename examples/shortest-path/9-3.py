# 플로이드 위셜

INF=int(1e9)

n=int(input())
m=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b]=0

# 거리 테이블
for _ in range(m):
    a,b,c=map(int, input().split())
    graph[a][b]=c

# 점화식에 따라 플로이드 위셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

