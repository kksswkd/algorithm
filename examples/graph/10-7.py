# 도시 분할 계획 - 신장 트리
# 방법: 두개의 신장 트리를 만들고 비용이 가장 큰 간선을 제거

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,x)
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

edges=[]
result=0

for i in range(v+1):
    parent[i]=i

for i in range(e):
    a,b,cost=map(int, input().split())
    # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설
    edges.append((cost,a,b))

# 간선을 비용순으로 정렬
edges.sort()
last=0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

for edge in edges:
    cost,a,b=edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost # 총 비용
        last=cost

print(result-last)