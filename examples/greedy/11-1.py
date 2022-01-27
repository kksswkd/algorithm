# 모험가 길드

n=int(input()) # 모험가의 수
data=list(map(int, input().split()))
data.sort()

result=0 # 그룹의 수
cnt=0 # 그룹에 포함된 모험가의 수

for i in data:
    cnt+=1
    if cnt>=i:
        result+=1
        cnt=0

print(result)