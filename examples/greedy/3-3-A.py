# 숫자 카드 게임
import time
starttime=time.time()

n,m=map(int, input().split())

result=0
for i in range(n):
    data=list(map(int, input().split()))
    data.sort()
    min_value=data[0]
    result=max(min_value,result)

endtime=time.time()
print(endtime-starttime)

print(result)
