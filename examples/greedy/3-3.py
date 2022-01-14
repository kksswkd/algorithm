# 숫자 카드 게임
import time
starttime=time.time()

n,m=map(int, input().split())

result=0
for i in range(n):
    data=list(map(int, input().split())) # m개의 수 n번 입력받기
    min_value=min(data) # 해당 줄에서 min 찾기
    result=max(result, min_value) # 해당 줄의 min과 result 중 max 찾기

endtime=time.time()
print(endtime-starttime)

print(result)
