# 커리큘럼 - 위상 정렬

from collections import deque
import copy

v=int(input()) # 듣고자 하는 강의의 수 = 노드 개수
indegree=[0]*(v+1) # 진입 차수 0으로 초기화
graph=[[] for i in range(v+1)]
# 각 강의 시간을 0으로 초기화
time=[0]*(v+1)

# 방향 그래프의 모든 간선 정보 입력받기
for i in range(1,v+1):
    data=list(map(int,input().split()))
    time[i]=data[0] # 입력받은 첫번째 수는 시간 정보
    for x in data[1:-1]:
        indegree[i]+=1 # 진입 차수 증가
        graph[x].append(i) # 선수 강의 정보 저장

# 위상 정렬 함수
def topology_sort():
    result=copy.deepcopy(time)
    q=deque()

    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now=q.popleft()
        # 해당 원소와 연결된 노드들의 진입 차수 -1
        for i in graph[now]:
            result[i]=max(result[i],result[now]+time[i])
            indegree[i]-=1
            # 새롭게 진입 차수가 0이 된 노드를 큐에 삽입
            if indegree[i]==0:
                q.append(i)

    # 위상 정렬 결과 출력
    for i in range(1,v+1):
        print(result[i])

topology_sort()